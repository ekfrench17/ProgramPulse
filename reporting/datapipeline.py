import pandas as pd
from .dataloader import DataLoader
from .datacleaner import DataCleaner
from .datafilter import DataFilter
from .datatransform import DataTransform
from .dataggregator import DataAggregator
import logging

logging.basicConfig(level=logging.INFO)

class DataPipeline:
    def __init__(self,source,source_path,time_frame=None,filters=None):
        self.source = source
        self.data_source = source_path
        self.time_frame = time_frame
        self.filters = filters
        self.data = None
        if self.source == 'nbly' or self.source == 'emap':
            self.date_col = 'Date'
            self.id_col = "Case_Id"
            self.award_col = "Amount"
        elif self.source == 'sbmtl':
            self.date_col = 'Payment_Date'
            self.id_col = 'Submission_Id'
            self.award_col = 'Individual_Award'
        elif self.source == 'clio':
            self.date_col = 'Close Date'
            self.id_col = "Client Id"
        elif self.source =='be':
            self.date_col ='Date_Final'
            self.id_col = 'Contact ID'
            self.award_col = 'Amount'
        elif self.source =='va':
            self.date_col ='Date entered'
            self.id_col = 'Contact ID'
            self.award_col = 'Amount in company currency'
        elif self.source == 'care_calls':
            self.date_col = "date_started"
            self.id_col = 'external_number'
        elif self.source == 'care_chats':
            self.date_col = 'Create date'
        else:
            # Date column for HubSpot sources
            self.date_col = 'Date entered'
            self.id_col = 'Contact ID'
    
    def load(self):
        """Load data to handle multiple file paths"""
        logging.info("Loading data...")
        load_list = []
        for source in self.data_source:
            loader = DataLoader(source)
            load_list.append(loader)
        if len(load_list) == 1:
            self.data = load_list[0].df
            return self
        
        else:
            self.data = [item.df for item in load_list]
            return self

    def clean(self):
        """Clean data to handle multiple dataframes"""
        logging.info("Cleaning dataframes...")
        if(isinstance(self.data,list)):
            cleaned_dfs = []
            for df in self.data:
                cleaner = DataCleaner(df)
                clean_df = cleaner.clean()
                cleaned_dfs.append(clean_df)
            self.data = cleaned_dfs
        else:
            cleaner = DataCleaner(self.data)
            self.data = cleaner.clean()
        return self

    def transform(self):
        logging.info("Transforming dataframes...")
        transformer = DataTransform(self.data,self.source)
        self.data = transformer.transform()
        return self

    def filter(self):
        logging.info("Filtering dataframe...")
        if self.time_frame == None and self.filters == None:
            return self
        filter = DataFilter(self.data)
        if self.time_frame != None:
            self.data = filter.filter_date(self.date_col,self.time_frame)
        if self.filters != None:
            # place holder for demographic filters
            pass
        return self

    def aggregate(self):
        logging.info("Creating unique dataframe...")
        aggregate = DataAggregator(self.data)
        if self.source == 'hs' or self.source == 'law':
            self.data = aggregate.make_unique_no_award(self.id_col)
        else:
            self.data = aggregate.make_unique_with_award(self.id_col,self.award_col)
    
    def check_df(self):
        # Make sure self.df is a DataFrame
        if not isinstance(self.data, pd.DataFrame):
            print("self.data is type",type(self.data))
            raise ValueError("Expected a DataFrame, got {type(self.data)} instead")

    def run_pipeline(self):
        self.load()
        self.clean()
        self.transform()
        self.filter()
        self.aggregate()
        return self