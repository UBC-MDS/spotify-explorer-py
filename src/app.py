# author: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin
# date: 2022-03-01

import altair as alt
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import layout_components as lc

alt.data_transformers.disable_max_rows()

# Intial read data for prototype
df = pd.read_csv("data/raw/spotify.csv")
# print(df.head())


def artist_popularity_hist():
    pass


def top_artists():
    pass


def artist_popularity_trend():
    pass


def popular_non_popular_line():
    pass


app = Dash(
    __name__,
    title="Spotify Explorer",
    external_stylesheets=[dbc.themes.MORPH],
    suppress_callback_exceptions=True,
)
server = app.server

app.layout = html.Div([lc.navbar, lc.container], style={"backgroundColor": "#eeeeef"})


@app.callback(Output("tab-content", "children"), [Input("tabs", "active_tab")])
def switch_tab(tab_id):
    if tab_id == "tab-1":
        return lc.get_artist_section()
    elif tab_id == "tab-2":
        return lc.get_popularity_section()
    return html.P("This shouldn't ever be displayed...")


if __name__ == "__main__":
    app.run_server(debug=True)
