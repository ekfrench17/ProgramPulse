import pandas as pd

def get_file_path(folder):
    pass

def upload_file(file_path,type="csv"):
    if(type=="xlsx"):
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)
    return df