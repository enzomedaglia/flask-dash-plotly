"""

"""
from unicodedata import category
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from typing import List
import pandas as pd


from src.data.loader import DataSchema
from src.components import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_categories: List[str] = data[DataSchema.CATEGORY].tolist()
    unique_categories: List[str] = sorted(set(all_categories))

    @app.callback(
        Output(ids.CATEGORY_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")
        ]
    )
    # _ is the value of n_clicks
    def select_all_categories(years: List[str], months: List[str], _: int) -> List[str]:
        filtered_data = data.query("year in @years and month in @months")
        return sorted(set(filtered_data[DataSchema.CATEGORY].tolist()))

    return html.Div(
        children=[
            html.H6("Category"),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=[{"label": category, "value": category} for category in unique_categories],
                value=unique_categories,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                n_clicks=0,
            )
        ]
    )
