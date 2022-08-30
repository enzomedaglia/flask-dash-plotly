from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from typing import list

from . import ids

MEDAL_DATA = px.data.medals_long()

# each component has a render function, it gets the application, the callbacks are defined inside and return the Div.
# (similar to react components)
def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.NATION_DROPDOWN, "value")
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        # pandas looks in the scope
        filtered_data = MEDAL_DATA.query("nation in @nations")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")

        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)