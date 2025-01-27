import pandas as pd
from pathlib import Path

class DataLoader():
    def __init__(self,folder_path):
        self.folder = Path(folder_path)
        self.file_path = self.get_file_path()

    def get_file_path(self):
        files_list = [f for f in self.folder.iterdir() if f.is_file()]
        if not files_list:
            raise FileNotFoundError(f"No files found in folder")
        
        file_name = files_list[0].name
        file_path = self.folder / file_name
        return str(file_path)

    def upload_file(self,type="csv"):
        if(type=="xlsx"):
            df = pd.read_excel(self.file_path)
        else:
            df = pd.read_csv(self.file_path)

        drop_cols = []
        for col in df.columns:
            if "Unnamed" in col:
                drop_cols.append(col)

        if drop_cols:
            df.drop(columns=drop_cols,inplace=True)
            
        return df

