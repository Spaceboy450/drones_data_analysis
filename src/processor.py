class Aggregator:
    def __init__(self, region_column, duration_column):
        self.region_column = region_column
        self.duration_column = duration_column

    def aggregator(self, df_clean):
        df_aggregated = df_clean.groupby(self.region_column, as_index=False).agg({
            self.duration_column: ['mean', 'count']
        })

        df_aggregated.columns = [self.region_column, 'mean_flight_duration', 'lights_counts']

        return df_aggregated