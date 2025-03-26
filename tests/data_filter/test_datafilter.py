import pandas as pd
import pytest
from reporting.datafilter import DataFilter

@pytest.fixture
def sample_sdata():
    """Fixture to read sample s data from CSV file for filter tests."""
    return pd.read_csv('./tests/data_filter/long_df_stest.csv')

class TestDataFilter:

    ### Test cases for initialization ###
    def test_init(self,sample_sdata):
        filter = DataFilter(sample_sdata)

        # Test if df is a pandas DataFrame
        assert isinstance(filter.df, pd.DataFrame), "The object is not a DataFrame"

    ### Test cases for filtering by date ###

    ### Test cases for filtering by county ###