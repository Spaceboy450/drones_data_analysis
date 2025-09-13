import os
import pandas as pd
from .abstractor import AbstractProcessor

class BasicLoader(AbstractProcessor):
    def __init__(self, path):
        self.path = path

    def get_data(self, extension):
        return [file for file in os.listdir(self.path) if file.endswith(extension)]


class CsvLoader(BasicLoader):
    def processing(self):
        csv_files = []
        for csv in self.get_data('.csv'):
            full_path = os.path.join(self.path, csv)
            data = pd.read_csv(full_path)
            csv_files.append(data)

        return pd.concat(csv_files, ignore_index=True)


class ExcelDataLoader(BasicLoader):
    def processing(self, sheet_name=0):
        excel_files = []
        for file in self.get_data(('.xls', '.xlsx')):
            full_path = os.path.join(self.path, file)
            df = pd.read_excel(full_path, sheet_name=sheet_name)
            excel_files.append(df)
        return pd.concat(excel_files, ignore_index=True)