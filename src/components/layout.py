<<<<<<< HEAD
"""

"""
from dash import Dash, html
import pandas as pd

from src.components.charts import bar_chart, pie_chart
from src.components.widgets import category_dropdown, month_dropdown, year_dropdown


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    category_dropdown.render(app, data),
                ]
            ),
            bar_chart.render(app, data),
            pie_chart.render(app, data),
        ]
=======
from dash import Dash, html

from . import bar_chart, nation_dropdown

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    nation_dropdown.render(app)
                ]
            ),
            bar_chart.render(app)
        ]
>>>>>>> 03d50657ce781f0edd070cb95879d1afe512d424
    )