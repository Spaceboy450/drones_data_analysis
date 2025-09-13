import os
# import matplotlib.pyplot as plt
from src.loader import CsvLoader
from src.cleaner import Cleaner
from src.processor import Aggregator
from src.dashboarder import Dashboarder
# from src.visualizer import BaseVisualizer

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '..', 'drones data','data', 'raw_data')
data_path = os.path.normpath(data_path)

loader = CsvLoader(data_path)
df = loader.processing()

cleaner = Cleaner('source_city', 'duration', 'date')
clean_data = cleaner.cleaning(df)

aggregator = Aggregator('source_city', 'duration')
data = aggregator.aggregating(clean_data)

# print(data)
# vizualizer = BaseVisualizer()
# bars_fig, bars_ax = vizualizer.create_barplots(data,
#                                         'source_city',
#                                         'mean_flight_duration',
#                                         'flights_counts')
# pie_fig, pie_ax = vizualizer.pie_charts(data,
#                                         'source_city',
#                                         'flights_counts')
#
# plt.show()

dashboard = Dashboarder()
fig1 = dashboard.create_interactive_dashboard(data, 'source_city', 'mean_flight_duration', 'flights_counts')
fig1.show()