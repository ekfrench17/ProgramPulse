import pandas as pd
import re
import numpy as np
from normalization import (column_mapping, ethnicity_mapping, race_mapping, gender_mapping,
                            language_mapping, income_mapping)


class DataCleaner:
    def __init__(self,df):
        self.df = df
        self = self.replace_empty_values()

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
    
    def clean_awards_cols(self):
        awards_cols = [col for col in self.df.columns if "award" in col.lower()]
        for col in awards_cols:
            self.df[col] = self.df[col].apply(self.__convert_to_float)
        return self

    def clean_date_cols(self):
        date_cols = [col for col in self.df.columns if "date" in col.lower()]
        for col in date_cols:
            # Assuming sbmtl_df is your DataFrame and date_cols[0] is the column name
            self.df[col] = pd.to_datetime(self.df[col], errors='coerce')

            # extract only the date part (yyyy-mm-dd):
            self.df[col] = self.df[col].dt.date
        return self

    def clean_phone_cols(self):
        def clean_phone(phone_number):
            """Helper function to convert a column from string to phone format
            as an integer with no dashes, spaces, parentheses, etc., and removes
            the country code '1' if the number has 11 digits."""

            # Handle missing or NaN values
            if isinstance(phone_number, float) and pd.isna(phone_number):
                return None  # Return None for NaN to maintain consistency

            # Ensure the input is a string
            if isinstance(phone_number, str):
                # Remove non-digit characters using regex
                phone_number = re.sub(r'\D', '', phone_number)  # \D matches any non-digit character
            elif isinstance(phone_number, (int, float)):  # If the input is numeric, convert it to string
                phone_number = str(int(phone_number))  # Ensure it's an integer, then convert to string

            # If the phone number has 11 digits and starts with '1', remove the leading '1'
            if len(phone_number) == 11 and phone_number.startswith('1'):
                phone_number = phone_number[1:]  # Remove the country code '1'

            # Check if the number is now 10 digits long and consists only of digits
            if len(phone_number) == 10 and phone_number.isdigit():
                return int(phone_number)  # Return the cleaned phone number as an integer
            else:
                return None  # If the number is not valid (e.g., incorrect length or non-digit characters), return None
        
        phone_cols = [col for col in self.df.columns if 'phone' in col.lower()]
        
        for col in phone_cols:
            self.df[col] = self.df[col].apply(clean_phone)
        
        return self

    def replace_empty_values(self):
        # Replace '(blank)' with NaN for all columns in the DataFrame
        self.df.replace('(blank)', np.nan, inplace=True)
        return self

    def __convert_to_float(self,value):
        """Removes non-digit characters from a string and converts it to a float.
        Used for calculating award columns in TRUA dataframe."""

        # If value is a string, remove spaces and non-numeric characters except for the decimal point
        if isinstance(value, str):
            # Remove any non-numeric characters except for the decimal point
            cleaned_value = "".join(filter(lambda x: x.isdigit() or x == ".", value))

            # Try to convert to float, return None if invalid format
            try:
                return float(cleaned_value)
            except ValueError:
                return None  # Return None if the string is not a valid float (e.g., 'abc')

        # Handle NaN (using pandas' isna function)
        elif pd.isna(value):
            return None  # If not a number, return None

        # Handle numeric types (int, float) by ensuring they're returned as floats
        elif isinstance(value, (int, float)):
            return float(value)

        # If none of the above conditions match, return None
        return None