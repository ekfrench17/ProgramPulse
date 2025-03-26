# Unit testing for the class DataTransform

import pytest
import pandas as pd
from reporting.datatransform import DataTransform
import math

@pytest.fixture
def sample_wide_data():
    """Fixture to read sample wide data from CSV file for transformation tests."""
    return pd.read_csv('./tests/data_transform/anonymized_stest_data.csv')

@pytest.fixture
def transformer(sample_wide_data):
    """Fixture to return an instance of DataTransform."""
    return DataTransform(sample_wide_data)

class TestDataTransform:

    ## Test Cases for the method transform_sbmtl (ts) ##

    def test_ids_ts(self,sample_wide_data,transformer):
        """Transform the test data using the transform_sbmtl method"""
        transformer = transformer.transform_sbmtl()
        
        # The number of unique IDs in both wide and long dataframes should be the same
        assert transformer.df['Submission_Id'].nunique() == sample_wide_data['Submission Id'].nunique(), f"Expected unique 'Submission_Id' count to match original: {sample_wide_data['Submission Id'].nunique()}, " \
            f"but got {transformer.df['Submission_Id'].nunique()}"

    def test_missing_values_ts(self,sample_wide_data,transformer):
        """Test for missing values in important columns"""
        transformer = transformer.transform_sbmtl()

        # There should be no missing IDs
        county_empty_ids = transformer.df[pd.isna(transformer.df["Submission_Id"])]["Submission_Id"].count()
        assert county_empty_ids == 0, f"All rows in column 'Submission_Id' should have a value, but got {county_empty_ids} empty rows."

    
    def test_shape_ts(self,sample_wide_data,transformer):
        """Transform the test data using the transform_sbmtl method"""
        transformer = transformer.transform_sbmtl()

        expected_shape = (637, 25)

        assert transformer.df.shape[0] == expected_shape[0], f"Expected {expected_shape} rows, but got {transformer.df.shape}"
        assert transformer.df.shape[1] == expected_shape[1], f"Expected {expected_shape} columns, but got {transformer.df.shape}"

        # Count of awards = 86
        # Count of payment dates = 85
        
    def test_amount_ts(self,sample_wide_data,transformer):
        """Check the total amount in wide and long format match"""
        transformer = transformer.transform_sbmtl()
        
        expected_value = sample_wide_data["Total_Awards"].sum()
        transformed_value = transformer.df["Individual_Award"].sum()
        # total amount should be the same in both formats = $ 314,729.12
        assert math.isclose(transformed_value,expected_value,rel_tol=1e-8), f"Expected total awards sum {expected_value}, but got {transformed_value}"