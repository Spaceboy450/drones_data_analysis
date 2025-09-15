from .abstractor import AbstractCleaner
from functools import wraps
# import pandas as pd

def log_cleaning(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Начало очистки данных в {self.__class__.__name__}")
        result = func(self, *args, **kwargs)
        print(f"Завершение очистки")
        return result

    return wrapper

class Cleaner(AbstractCleaner):
    @log_cleaning

    def __init__(self, region, duration, date):
        self.region = region
        self.duration = duration
        self.date = date

    # def __call__(self):
    #     print('Начнем очистку датасета')

    def cleaning(self, data):
        clean_data = data.drop_duplicates().copy()

        clean_data[self.region] = clean_data[self.region].str.upper().str.strip()

        # clean_data[self.date] = pd.to_datetime(clean_data[self.date], errors='coerce')

        clean_data = clean_data.query('duration > 0')

        clean_data = clean_data.dropna(subset=[self.region, self.duration])

        return clean_data
