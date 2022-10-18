"""

"""
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from typing import List
import pandas as pd

from src.data.loader import DataSchema
from src.components import ids

# each component has a render function, it gets the application, the callbacks are defined inside and return the Div.
# (similar to react components)
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_DROPDOWN, "value"),
        ]
    )

    def update_bar_chart(years: List[str], months: List[str], categories: List[str]) -> html.Div:
        # pandas looks in the scope
        filtered_data = data.query("year in @years and month in @months and category in @categories")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.AMOUNT,
                index=[DataSchema.CATEGORY],
                aggfunc="sum",
                fill_value=0
            )
            return pt.reset_index().sort_values(DataSchema.AMOUNT, ascending=False)

        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY,
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)