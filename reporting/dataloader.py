import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self,folder_path):
        self.folder = Path(folder_path)

    def create_table(self):
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

            if 'Category' in df.columns and len(df['Category'].unique()) > 0:
                df['source_name'] = source_name
            
            dataframes.append(df)
        
        if len(dataframes) == 1:
            return dataframes[0]
        
        return pd.concat(dataframes,ignore_index=True)
    
    def __get_file_paths(self):
        file_path_list = [file for file in self.folder.iterdir() 
                          if file.is_file() and (file.suffix == '.xlsx' or file.suffix == '.csv')]
        if not file_path_list:
            raise FileNotFoundError(f"No .xlsx or .csv files found in folder")
        
        return file_path_list
