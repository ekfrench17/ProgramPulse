import pandas as pd
import pytest
from reporting.datafilter import DataFilter

@pytest.fixture
def sample_sdata():
    """Fixture to read sample s data from CSV file for filter tests."""
    return pd.read_csv('./tests/data_filter/long_df_stest.csv')

@pytest.fixture
def filter(sample_sdata):
    return DataFilter(sample_sdata)

@pytest.fixture
def date_filtered_df(filter):
    """Fixture to create date filtered dataframe for testing"""
    start_date = "2024-12-01"
    end_date = "2025-01-31"
    date_col = "Payment_Date"
    return filter.filter_date(date_col,[start_date,end_date])


class TestDataFilter:

    ### Test cases for initialization ###
    def test_init(self,sample_sdata):
        filter = DataFilter(sample_sdata)

        # Test if df is a pandas DataFrame
        assert isinstance(filter.df, pd.DataFrame), "The object is not a DataFrame"

        # Test if the DataFrame is not empty
        assert not filter.df.empty, "The DataFrame is empty"

        # Test if the DataFrame has the expected number of rows and columns
        assert filter.df.shape == (637, 25), f"Expected shape (3, 2), but got {filter.df.shape}"

    ### Test cases for filtering by date ###
    def test_filter_date_valid(self,sample_sdata,date_filtered_df):
        """"Test date filtering returns a valid dataframe"""

        # Test the object returned after filtering is a dataframe
        assert isinstance(date_filtered_df,pd.DataFrame), "The object returned is not a DataFrame"

        # Test if the DataFrame is not empty
        assert not date_filtered_df.empty, "The DataFrame is empty"

        # Test the dataframe returned is the expected shape
        expected_cols = sample_sdata.shape[1]
        output_cols = date_filtered_df.shape[1]
        assert expected_cols == output_cols, f"Expected {expected_cols} columns but got {output_cols}"

        expected_rows = date_filtered_df.shape[0]
        assert expected_rows == 24, f"Expected 24 rows, but got {expected_rows}"

    def test_filter_date_minmax(self,date_filtered_df):
        """Test the dates in the column are within the desired range"""
        # Test there are no empty dates
        count_empty_dates = date_filtered_df[pd.isna(date_filtered_df["Payment_Date"])]["Payment_Date"].count()
        assert count_empty_dates == 0, f"Empty rows in the date filtered frame returned."

        # Test range min and max
        assert date_filtered_df["Payment_Date"].min() >= pd.to_datetime("2024-12-01")
        assert date_filtered_df["Payment_Date"].max() <= pd.to_datetime("2025-01-31")

    ### Test cases for filtering by county ###