import os
import pandas as pd
from .abstractor import AbstractProcessor
from functools import wraps

def log_processing(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Начало обработки в {self.__class__.__name__}")
        result = func(self, *args, **kwargs)
        print(f"Завершение обработки. Загружено {len(result)} строк")
        return result
    return wrapper

def handle_file_errors(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден в директории {self.path}")
            return pd.DataFrame()
        except pd.errors.EmptyDataError:
            print("Ошибка: Файл пуст")
            return pd.DataFrame()
    return wrapper

class BasicLoader(AbstractProcessor):
    def __init__(self, path):
        self.path = path

    def get_data(self, extension):
        return [file for file in os.listdir(self.path) if file.endswith(extension)]


class CsvLoader(BasicLoader):
    @handle_file_errors
    @log_processing
    def processing(self):
        csv_files = []
        for csv in self.get_data('.csv'):
            full_path = os.path.join(self.path, csv)
            data = pd.read_csv(full_path)
            csv_files.append(data)

        return pd.concat(csv_files, ignore_index=True)


class ExcelDataLoader(BasicLoader):
    @handle_file_errors
    @log_processing
    def processing(self, sheet_name=0):
        excel_files = []
        for file in self.get_data(('.xls', '.xlsx')):
            full_path = os.path.join(self.path, file)
            df = pd.read_excel(full_path, sheet_name=sheet_name)
            excel_files.append(df)
        return pd.concat(excel_files, ignore_index=True)