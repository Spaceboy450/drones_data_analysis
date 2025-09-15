import os
from plotly.subplots import make_subplots
from .visualizer import BaseVisualizer

class Dashboarder():
    def __init__(self):
        self.setup_plotly_theme()
        self.chart_creator = BaseVisualizer(self.colors)

    def setup_plotly_theme(self):
        self.colors = {
            'primary': '#1f77b4',
            'secondary': '#ff7f0e',
            'accent': '#2ca02c',
            'background': '#f8f9fa',
            'text': '#2c3e50'
        }

        self.font_family = '"Baloo Bhaijaan", "Arial Rounded MT Bold", "Comic Sans MS", "Inter", sans-serif'
        self.font_size = 16

    def create_interactive_dashboard(self, data, x_col, y1_col, y2_col):

        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Среднее время полета по городам',
                'Количество полетов по городам',
                'Распределение времени полета',
                'Топ-10 городов по количеству полетов (но в датасете пока 5)'
            ),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "box"}, {"type": "pie"}]],
            vertical_spacing=0.15,
            horizontal_spacing=0.1
        )

        fig.add_trace(
            self.chart_creator.create_avg_time_bar(data, x_col, y1_col),
            row=1, col=1
        )

        fig.add_trace(
            self.chart_creator.create_flight_count_bar(data, x_col, y2_col),
            row=1, col=2
        )

        box_charts = self.chart_creator.create_flight_time_box(data, x_col, y1_col)
        for box_chart in box_charts:
            fig.add_trace(box_chart, row=2, col=1)

        fig.add_trace(
            self.chart_creator.create_top_cities_pie(data, x_col, y2_col),
            row=2, col=2
        )

        self._apply_layout_settings(fig)

        return fig

    def _apply_layout_settings(self, fig):

        fig.update_layout(
            title=dict(
                text='📊 Дашборд анализа полетов по городам',
                x=0.5,
                font=dict(size=24,
                          color=self.colors['text'],
                          family=self.font_family,
                          weight='bold')
            ),
            height=900,
            showlegend=False,
            plot_bgcolor=self.colors['background'],
            paper_bgcolor=self.colors['background'],
            font=dict(family=self.font_family, size=self.font_size, color=self.colors['text'])
        )

        fig.update_xaxes(
            title_text='Среднее время полета (мин)',
            row=1, col=1,
            title_font=dict(family=self.font_family, size=14)
        )
        fig.update_yaxes(
            title_text='Город',
            row=1, col=1,
            title_font=dict(family=self.font_family, size=14)
        )

        fig.update_xaxes(
            title_text='Город',
            row=1, col=2,
            title_font=dict(family=self.font_family, size=14)
        )
        fig.update_yaxes(
            title_text='Количество полетов',
            row=1, col=2,
            title_font=dict(family=self.font_family, size=14)
        )

        fig.update_xaxes(
            title_text='Город',
            row=2, col=1,
            title_font=dict(family=self.font_family, size=14)
        )
        fig.update_yaxes(
            title_text='Время полета (мин)',
            row=2, col=1,
            title_font=dict(family=self.font_family, size=14)
        )

        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(current_dir, '..', 'data', 'dashboard', 'plots.json')
        data_path = os.path.normpath(data_path)
        fig.write_json(data_path)