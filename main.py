from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout


def main () -> None:
    # initialize the app, define stylesheet
    app = Dash(external_stylesheets=[BOOTSTRAP])
    # Page Title in Browser
    app.title = "Medal dashboard"
    # define app layout
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
