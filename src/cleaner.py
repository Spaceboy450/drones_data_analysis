from .abstractor import AbstractCleaner
import pandas as pd

class Cleaner(AbstractCleaner):
    def __init__(self, region, duration, date):
        self.region = region
        self.duration = duration
        self.date = date

    def cleaning(self, data):
        clean_data = data.drop_duplicates().copy()

        clean_data[self.region] = clean_data[self.region].str.upper().str.strip()

        # clean_data[self.date] = pd.to_datetime(clean_data[self.date], errors='coerce')

        clean_data = clean_data.query('duration > 0')

        clean_data = clean_data.dropna(subset=[self.region, self.duration])

        return clean_data

# cleaner = Cleaner('source_city', 'duration', 'arrival_time')
#
#
# df = pd.read_csv('/Users/sheergambler/PycharmProjects/drones data/data/raw_data/airlines_flights_data.csv')
#
# print(cleaner.cleaning(df))

