import pandas as pd
import re
from normalization import (column_mapping, ethnicity_mapping, race_mapping, gender_mapping,
                            language_mapping, income_mapping)


class DataCleaner:
    def __init__(self,df):
        self.df = df

    def normalize_column_names(self):
        """Normalize column names to standard names for race, ethnicity, gender, etc."""
        
        # Remove unwanted suffixes like ' (Merged Fields)' and ' (Form Attributes)'
        self.df.columns = self.df.columns.str.replace(r' \((Merged Fields|Form Attributes)\)', '', regex=True)

        
        # Map column names using the imported dictionaries
        def map_column(col):
            # Remove leading/trailing spaces
            new_col = col.strip()

            # Map columns based on the keyword
            for keyword, standard_name in column_mapping.column_map.items():
                if re.search(rf'{keyword}', new_col, re.IGNORECASE):
                    return standard_name

            # Map phone columns
            if 'phone' in new_col.lower():
                for key, value in column_mapping.phone_patterns.items():
                    if key in new_col.lower():
                        return value
                return 'Phone'

            # Map email columns
            if 'email' in new_col.lower():
                for key, value in column_mapping.email_patterns.items():
                    if key in new_col.lower():
                        return value
                return 'Email'

            return new_col  # Return column name if no changes were made

        # Apply the mapping function to each column and update the column names
        self.df.columns = [map_column(col) for col in self.df.columns]
        
        return self
    
    def clean_household_size(self, column_name="Household_Size", fill_value=2.35):
        """function to convert Household_Size to integers and fill empty values with the value 2.35"""
        self.df[column_name] = self.df[column_name].str.strip().replace({'6+': '6'})
        self.df[column_name] = pd.to_numeric(self.df[column_name], errors='coerce', downcast='integer')
        
        # Replace values greater than 19 with the fill_value (2.35) using boolean indexing
        self.df.loc[self.df[column_name] > 19, column_name] = fill_value
        
        self.df[column_name] = self.df[column_name].fillna(fill_value)  # Fill NaN values with 2.35
        return self