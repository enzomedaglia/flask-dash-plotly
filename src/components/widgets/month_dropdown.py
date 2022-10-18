"""

"""
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from typing import List
import pandas as pd


from src.data.loader import DataSchema
from src.components import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_months: List[str] = data[DataSchema.MONTH].tolist()
    unique_months = sorted(set(all_months))

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [Input(ids.YEAR_DROPDOWN, "value"), Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks")]
    )
    # _ is the value of n_clicks
    def update_months(years: List[str], _: int) -> List[str]:
        filtered_data = data.query("year in @years")
        return sorted(set(filtered_data[DataSchema.MONTH].tolist()))

    return html.Div(
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[{"label": month, "value": month} for month in unique_months],
                value=unique_months,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            )
        ]
    )
