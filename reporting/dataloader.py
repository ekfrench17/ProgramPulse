import pandas as pd
from pathlib import Path
import numpy as np

handled = 'handled'
not_handled = 'not handled'

dialpad_category_map = {
    # handled categories
    'forwarded':handled,
    'incoming':handled,
    'other':handled,
    'outgoing':handled,
    'callback_connected':handled,
    # not handled categories
    'abandoned': not_handled,
    'missed': not_handled,
    'cancelled':not_handled,
    'callback_unconnected':not_handled,
    'callback_cancelled':not_handled
}

class DataLoader:
    def __init__(self,folder_path,source):
        self.folder = Path(folder_path)
        if source == 'care_calls':
            self.df = self.__create_table(source)
        elif 'nbly' in self.folder.name.lower() or 'emap' in self.folder.name.lower():
            self.df = self.__create_nbly_transaction_frame()
        else:
            self.df = self.__create_table(source)
            if 'clio' in self.folder.name.lower():
                if 'Gender*' in self.df.columns:
                    self.df = self.df.drop(columns="Gender*")

    def __create_table(self,source):
        file_path = self.__get_file_paths()
        try:
            if file_path[0].suffix == '.xlsx':
                df = pd.read_excel(file_path[0])
            elif file_path[0].suffix == '.csv':
                df = pd.read_csv(file_path[0])
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

        drop_cols = [col for col in df.columns if "Unnamed" in col]
        if drop_cols:
            df.drop(columns=drop_cols,inplace=True)
        
        # check if file has multiple date entered columns
        if self.__needs_final_date_column(df):
            df = self.__fix_date_column(df)

        # check for submittable file to delete first row
        if source == 'sbmtl':
            df = df.drop(index=0)

        # check if dialpad file to filter for category
        if(source.lower() == 'care_calls'):
            df = self.__load_dialpad_helper(df)
        
        if(source.lower() == 'be'):
            df = self.__load_be_helper(df)


        return df
    
    def __create_nbly_transaction_frame(self):
        file_paths = self.__get_file_paths()

        # Read all files and store them in a list
        dataframes = []
        for file_path in file_paths:
            source_name = file_path.stem.split('_Transactions')[0]

            try:
                if file_path.suffix == '.xlsx':
                    df = pd.read_excel(file_path)
                elif file_path.suffix == '.csv':
                    df = pd.read_csv(file_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue # skip this file and move to the next one

            drop_cols = [col for col in df.columns if "Unnamed" in col]
            if drop_cols:
                df.drop(columns=drop_cols,inplace=True)

            # apply function to filter for Category, Type, and add columns
            df = self.__create_df_helper(df,source_name)
            
            dataframes.append(df)
        
        if len(dataframes) == 1:
            return dataframes[0]
        
        combined = pd.concat(dataframes,ignore_index=True)
        #combined = combined.drop_duplicates()
        return combined
    
    def __get_file_paths(self):
        file_path_list = [file for file in self.folder.iterdir() 
                          if file.is_file() and (file.suffix == '.xlsx' or file.suffix == '.csv')]
        if not file_path_list:
            raise FileNotFoundError(f"No .xlsx or .csv files found in folder")
        
        return file_path_list
    
    def __needs_final_date_column(self,df):
        date_entered = [col for col in df.columns if 'date entered' in col.lower()]
        if len(date_entered) > 1:
            return True
        return False
    
    def __fix_date_column(self,df):
        date_entered_cols = [col for col in df.columns if 'date entered' in col.lower()]

        if not date_entered_cols:
            return df  # Return unchanged if no matching columns
        
        # Convert each column to datetime, handling errors
        for col in date_entered_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce')

       # Create 'Date_Final' by finding the first non-null datetime across the columns
        df['Date_Final'] = df[date_entered_cols].bfill(axis=1).iloc[:, 0]
        
        df = df.drop(columns=date_entered_cols)

        return df
    
    def __create_df_helper(self,df,source_name=None):
        """Helper function for nbly dataframe creation"""
        if 'Category' not in df.columns:
            return df
        
        df = df.copy()

        df['Category'] = df['Category'].apply(lambda x: x.strip() if isinstance(x, str) else x)
        
        # Remove project delivery funds and legal services transactions
        """df = df[(df['Category'] != 'Project Delivery ') &
                                                ~((df['Category'] == 'Legal Services - Fee') |
                                                (df['Category'] == 'Legal Services - Administrative '))]"""
        df = df.loc[~((df['Category'] == 'Project Delivery') | 
                  (df['Category'] == 'Legal Services - Fee') |
                  (df['Category'] == 'Legal Services - Administrative') |
                  (df['Category'] == 'Housing Counseing'))]

        if source_name != None:
            # Add a column for the source (agency) of transactions
            #df['Full_Source_name'] = source_name
            df.loc[:, 'Full_Source_name'] = source_name

            # Create a column to filter for TRAG or ERA
            #df["Source"] = np.where("TRAG" in source_name,"TRAG","ERA")
            df.loc[:, 'Source'] = np.where("TRAG" in source_name, "TRAG", "ERA")

        # Keep only initial funding and change order types of funding
        #df = df[(df['Type']=='Initial Funding') | (df['Type']=='Change Order')]
        df = df.loc[(df['Type'] == 'Initial Funding') | (df['Type'] == 'Change Order')]

        # Return cleaned table of transactions to be merged with other files
        return df
    
    def __load_dialpad_helper(self,df):
        # only use call center calls
        df = df.loc[df['target_kind']=='CallCenter']

        # add a column to quickly analyze call outcome
        df.loc[:,'handle_type'] = df['category'].map(dialpad_category_map)

        return df
    
    def __load_be_helper(self,df):
        # sum benefits and awards columns into one column
        df = df.replace(['(blank)','(No value)'], np.nan)
        df["Amount"] = df["Total Back Benefits (Amount)"].astype(float) + df["Annual Forward Benefits Expected"].astype(float)
        return df