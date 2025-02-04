import pandas as pd
import re

class DataCleaner:
    def __init__(self,df):
        self.df = df

    def normalize_column_names(self):
        """Normalize column names to standard names for race, ethnicity, gender, etc."""
        
        # Define a mapping for standard column names
        normalization_map = {
            'race': 'Race',
            'ethnicity': 'Ethnicity',
            'gender': 'Gender',
            'language': 'Language',
            'household_size': 'Household_Size',
            'email': 'Email',
            'phone': 'Phone'
        }
        
        # Iterate over the columns and rename based on keywords found
        new_columns = []
        for col in self.df.columns:
            new_col = col.strip()  # Remove any leading/trailing spaces
            
            # Check for relevant keywords and map them to the standard names
            for keyword, standard_name in normalization_map.items():
                if re.search(rf'\b{keyword}\b', new_col, re.IGNORECASE):
                    new_col = standard_name
                    break  # No need to check further if a match is found
                
            # For phone columns like "Primary Phone" or "Alternate Phone", 
            # map them to "Phone_Primary" or "Phone_Alternate"
            if re.search(r'\bphone\b', new_col, re.IGNORECASE):
                if "primary" in new_col.lower():
                    new_col = 'Phone_Primary'
                elif "alternate" in new_col.lower():
                    new_col = 'Phone_Alternate'
                else:
                    new_col = 'Phone'
            
            new_columns.append(new_col)
        
        # Assign the new column names
        self.df.columns = new_columns
        
        return self
    
    def optimize_household_size_column(self, column_name="Household_Size", fill_value=2.35):
        """function to convert Household_Size to integers and fill empty values with the value 2.35"""
        self.df[column_name] = self.df[column_name].replace({'6+': '6'})
        self.df[column_name] = pd.to_numeric(self.df[column_name], errors='coerce', downcast='integer')
        
        # Replace values greater than 19 with the fill_value (2.35) using boolean indexing
        self.df.loc[self.df[column_name] > 19, column_name] = fill_value
        
        self.df[column_name] = self.df[column_name].fillna(fill_value)  # Fill NaN values with 2.35
        return self