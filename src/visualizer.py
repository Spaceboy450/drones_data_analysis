import plotly.graph_objects as go
import plotly.express as px


class BaseVisualizer:
    def __init__(self, colors):
        self.colors = colors

    def create_avg_time_bar(self, data, x_col, y1_col):
        return go.Bar(
            y=data[x_col],
            x=data[y1_col],
            orientation='h',
            name='Среднее время',
            marker_color=self.colors['primary'],
            hovertemplate='<b>%{y}</b><br>Среднее время: %{x:.1f} мин<extra></extra>'
        )

    def create_flight_count_bar(self, data, x_col, y2_col):
        return go.Bar(
            x=data[x_col],
            y=data[y2_col],
            name='Количество полетов',
            marker_color=self.colors['secondary'],
            hovertemplate='<b>%{x}</b><br>Количество: %{y}<extra></extra>'
        )

    def create_flight_time_box(self, data, x_col, y1_col):
        boxes = []
        for city in data[x_col]:
            boxes.append(
                go.Box(
                    y=data[y1_col],
                    name=city,
                    boxpoints=False
                )
            )
        return boxes

    def create_top_cities_pie(self, data, x_col, y2_col):
        top_cities = data.nlargest(5, y2_col)
        return go.Pie(
            labels=top_cities[x_col],
            values=top_cities[y2_col],
            name='Доля полетов',
            hole=0.4,
            marker_colors=px.colors.qualitative.Set3,
            hovertemplate='<b>%{label}</b><br>Доля: %{percent}<br>Количество: %{value}<extra></extra>'
        )