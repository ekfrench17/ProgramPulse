import pandas as pd

class DataTransform:
    def __init__(self,data,source=None):
        self.df = data
        self.source = source

    def transform_sbmtl(self):
        # Ensure that self.df is set before using method
        if not hasattr(self, 'df'):
            raise ValueError("Dataframe (df) not set!")
        
        # Create list of awards columns
        awards_columns = [col for col in self.df.columns if "Individual Awards" in col]

        # List of payment date columns
        date_cols = [col for col in self.df.columns if "Payment Dates" in col]
        
        # Melt the payment dates and individual awards columns to long format
        payment_dates_long = self.df[date_cols].melt(var_name='Payment_Type', value_name='Payment_Date')
        individual_awards_long = self.df[awards_columns].melt(var_name='Award_Type', value_name='Individual_Award')

        # Add the Submission Id column to the long format DataFrame
        submission_id = self.df['Submission Id'].repeat(len(payment_dates_long) // len(self.df)).reset_index(drop=True)

        # Combine the melted columns into a single long format DataFrame
        long_df = pd.DataFrame({
            'Submission_Id': submission_id,
            'Payment_Date': payment_dates_long['Payment_Date'],
            'Individual_Award': individual_awards_long['Individual_Award'],
        })

        demographics = self.df.drop(columns=awards_columns+date_cols)
        """demographics = self.df[['Submission Id', 'Review Stage', 'Full Name',
       'First Name', 'Last Name', 'Date of birth', 'Language', 'Email_Primary',
       'Email_Alternate', 'Phone_Primary', 'Phone_Alternate',
       'primary address (address 1)', 'primary address: Address 2', 'City',
       'Region', 'Zip Code', 'Country', 'Apartment or Unit Number',
       'Household Income Level', 'Race', 'Ethnicity', 'Gender',
       'Household_Size']]"""
        
        demographics = demographics.rename(columns={'Submission Id':'Submission_Id'})
        
        long_df = long_df.merge(demographics,on="Submission_Id",how="left")

        self.df = long_df

        return self
    
    def merge_nbly(self):
        "Merge the demographics dataframe onto the transactions dataframe"
        df = self.df[0]
        demographics_df = self.df[1]
        self.df = df.merge(demographics_df,on="Case_Id",how="left")
        return self
    
    def transform(self):
        if self.source == None:
            pass
        elif self.source == 'nbly' or self.source =='emap':
            self.merge_nbly()
        elif self.source == 'sbmtl':
            self.transform_sbmtl()
        else:
            pass
        
        return self.df