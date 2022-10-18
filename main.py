<<<<<<< HEAD
"""

"""
from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_transaction_data

# GLOBALS
DATA_PATH = "./data/transactions.csv"


def main() -> None:
    # load data into app
    data = load_transaction_data(DATA_PATH)
    # initialize the app, define stylesheet
    app = Dash(external_stylesheets=[BOOTSTRAP])
    # Page Title in Browser
    app.title = "Financial Dashboard"
    # define app layout
    app.layout = create_layout(app, data)
    # Run app
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
=======
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
>>>>>>> 03d50657ce781f0edd070cb95879d1afe512d424
