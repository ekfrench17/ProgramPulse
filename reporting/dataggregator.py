# Create unique dataframes

import pandas as pd

class DataAggregator:
    def __init__(self, df):
        self.df = df

    def make_unique(self,id_column,award_col):
        """function to return a dataframe where each row is unique based on ID column"""
        unique_demo = self.df.drop_duplicates(subset="Submission_Id")

        unique_df = self.df[[id_column,award_col]].groupby(id_column).sum(award_col)

        if "Household_Size" in self.df.columns:
            unique_df = unique_df.merge(unique_demo[[id_column,"Household_Size"]],on=id_column,how="left")

        #id_count = self.df[[id_column]].nunique()
        #unique_rows = unique_df.shape[0]

        #assert id_count == unique_rows,f"Expected {id_count} rows, but got {unique_rows}"

        return unique_df