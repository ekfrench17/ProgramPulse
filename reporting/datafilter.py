# Module for filtering by different criteria

import pandas as pd

class DataFilter:
    def __init__(self,df):
        self.df = df

    def filter_date(self,date_col,time_frame):
        """
        Filters the rows of a DataFrame based on a specified date range.

        Args:
            date_col (str): The name of the column containing date values.
            time_frame (list of str or datetime-like): The start date for the filter (inclusive), The end date for the filter (inclusive)

        Returns:
            pandas.DataFrame: A new DataFrame containing only the rows where the date in
                            `date_col` falls within the specified `start_date` and `end_date`.

        Notes:
            - The `date_col` is converted to a pandas datetime format before filtering.
            - Both `start_date` and `end_date` should be compatible with pandas datetime objects,
            such as strings in 'YYYY-MM-DD' format or actual `datetime` objects.
            - The function includes rows with dates exactly equal to `start_date` and `end_date`.
        """
        # Ensure that self.df is set before using method
        if not hasattr(self, 'df'):
            raise ValueError("Dataframe (df) not set!")
        
        # ensure date column is in datetime format
        self.df[date_col] = pd.to_datetime(self.df[date_col])

        # convert start and end date strings to datetime
        start_date = time_frame[0]
        end_date = time_frame[1]

        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)

        # filter dataframe for specified date range
        filtered_df = self.df[(self.df[date_col] >= start_dt) & (self.df[date_col] <= end_dt)]

        return filtered_df        

    def filter_county(self,county_col,county_list):
        """Function to filter a dataframe to return only individuals from a specified list of counties
        @param county_col: str column name for the dataframe where county data is stored
        @param county_list: list list of counties to be included in the filter
        returns: a filtered dataframe only including rows with individuals from the counties specified"""

        # Ensure that self.df is set before using method
        if not hasattr(self, 'df'):
            raise ValueError("Dataframe (df) not set!")
        
        filtered_df = self.df[self.df[county_col].isin(county_list)]
        return filtered_df