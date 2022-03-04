# author: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin
# date: 2022-03-01

import pandas as pd
import numpy as np
from datetime import datetime
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


today = datetime.now()
formatted_date = today.strftime("%b %d, %Y")
SPOTIFY_LOGO = "assets/img/spotify-ex.png"
df = pd.read_csv("data/raw/spotify.csv", parse_dates=["track_album_release_date"])
df.dropna(inplace=True)

# Styling

NAV_STYLE = {
    "height": "50px",
    "fontSize": "large",
}

TAB_STYLE = {
    "marginBottom": 20,
    "height": "50px",
    "padding": "3px 0 0 320px",
    "color": "white",
    "fontSize": "medium",
}

FOOTER_STYLE = {
    "position": "fixed",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": "25px",
    "padding": "3px 0 0 5px",
    "backgroundColor": "green",
    "color": "white",
    "fontSize": "small",
}


# Layout for 2 tab sections:  get_artist_section(), get_popularity_section()

# layout for sidebar in Artists/Genres
def get_artist_section():
    """
    1 row x 2 columns
    1st col - Widgets
    2nd col - with 2 rows where first row has 1 column and other row has 2 columns
    """

    sidebar_widgets = dbc.Col(
        children=[
            html.H2("Overview", className="display-30"),
            html.H6(
                "Welcome! This is a dashboard displaying trends in popularity of artists, \
                genres and song types in Spotify. Happy exploring!",
                className="display-30",
            ),
            html.Br(),
            html.H5("Artist Genre:"),
            dcc.Dropdown(
                id="genre",
                value="pop",
                style={"border-width": "0", "width": "100%"},
                options=["edm", "latin", "pop", "r&b", "rap", "rock"],
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H5("Artist Name:"),
            dcc.Dropdown(
                id="artist_selection",
                value="Ed Sheeran",  # REQUIRED to show the plot on the first page load
                style={"border-width": "0", "width": "100%"},
                options=[
                    {"label": name, "value": name}
                    for name in df["track_artist"].unique().tolist()
                ],
            ),
        ],
        width=3,
    )
    # layout for plot_1 on row 1
    plot_1_settings = dbc.Col(
        [
            html.H4("Top Artists by Genre", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="artist_genre_bar_id",
                style={
                    "width": "900px",
                    "height": "350px",
                    "border": "0px",
                    "padding-left": "60px",
                },
            ),
        ],
        style={
            "text-align": "center",
        },
    )
    # layout for plot_2 on row 2 col 1
    plot_2_settings = dbc.Col(
        [
            html.H4("Artist's Popularity Over Time", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="artist_trend_plot",
                style={
                    "width": "100%",
                    "height": "100%",
                    "border": "0px",
                    "padding-left": "20px",
                },
            ),
        ],
        style={
            "text-align": "center",
        },
    )
    # layout for plot_3 on row 2 col 2
    plot_3_settings = dbc.Col(
        [
            html.H4("Artist's popularity record", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="artist_pop_hist_id",
                style={
                    "width": "100%",
                    "height": "350px",
                    "border": "0px",
                },
            ),
        ],
        style={
            "text-align": "center",
        },
    )
    # layout for Artists/Genres section
    section = html.Div(
        [
            dbc.Row(
                children=[
                    sidebar_widgets,
                    dbc.Col(
                        children=[
                            dbc.Row(children=[plot_1_settings]),
                            dbc.Row(
                                children=[
                                    plot_2_settings,
                                    plot_3_settings,
                                ]
                            ),
                        ]
                    ),
                ]
            )
        ]
    )

    return section


# Song characteristics section
def get_popularity_section():
    """
    1 row
    2 columns
    1col - Widgets
    2col - Plot
    """
    # layout for sidebar in Song characteristics
    sidebar_widgets = dbc.Col(
        children=[
            html.H2("Explore music characteristics", className="display-30"),
            html.Br(),
            html.H5("Music Features:"),
            dcc.Dropdown(
                id="xcol-widget",
                style={"border-width": "0", "width": "100%"},
                options=[
                    {"label": "Danceability", "value": "danceability"},
                    {"label": "Energy", "value": "energy"},
                    {"label": "Loudness", "value": "loudness"},
                    {"label": "Acousticness", "value": "acousticness"},
                    {"label": "Speechiness", "value": "speechiness"},
                    {"label": "Instrumentalness", "value": "instrumentalness"},
                    {"label": "Liveness", "value": "liveness"},
                    {"label": "Valence", "value": "valence"},
                    {"label": "Tempo", "value": "tempo"},
                    {"label": "Duration (min)", "value": "Duration (min)"},
                ],
                value="danceability",
            ),
            html.Br(),
            html.H5("Music Genres:"),
            dcc.Dropdown(
                id="genres",
                style={"border-width": "0", "width": "100%"},
                options=[
                    {
                        "label": "Electronic dance music",
                        "value": "electronic dance music",
                    },
                    {"label": "Pop", "value": "pop"},
                    {"label": "Rap", "value": "rap"},
                    {"label": "Rock", "value": "rock"},
                    {"label": "Latin", "value": "latin"},
                    {"label": "R&B", "value": "r&b"},
                ],
                value="electronic dance music",
            ),
            html.Iframe(
                id="widget_id2",
                style={
                    "width": "20%",
                    "height": "100px",
                    "border": "0px",
                },
            ),
        ],
        width=3,
    )
    # layout for plot_4 in Song characteristics
    plot_4_settings = dbc.Col(
        [
            html.H3(
                "Song characteristics distribution between two popularity classes",
                className="display-30",
            ),
            html.Iframe(
                id="pop_unpop_id",
                style={
                    "width": "100%",
                    "height": "450px",
                    "padding-left": "80px",
                    "border": "0px",
                },
            ),
        ],
        style={
            "width": "100%",
            "height": "520px",
            "border": "0px",
        },
    )

    section = html.Div([dbc.Row(children=[sidebar_widgets, plot_4_settings])])

    return section


# Tabs


def get_tab_section():
    tab_section = html.Div(
        [
            dbc.Tabs(
                [
                    dbc.Tab(label="Artists/Genres", tab_id="tab-1"),
                    dbc.Tab(label="Song characteristics", tab_id="tab-2"),
                ],
                id="tabs",
                active_tab="tab-1",
                style=TAB_STYLE,
            ),
            html.Div(id="tab-content"),
        ]
    )
    return tab_section


# Navbars (top) and footer (bottom)
# layout for top
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=SPOTIFY_LOGO, height="50px")),
                        dbc.Col(dbc.NavbarBrand("Spotify Explorer", className="py-10")),
                    ],
                    align="center",
                    className="g-0",
                    style=NAV_STYLE,
                )
            )
        ]
    )
)
# layout for footer
container = dbc.Container(
    [
        html.Br(),
        get_tab_section(),
        html.Footer(
            [
                f"(C) Copyright MIT License: Christopher Alexander, Jennifer Hoang, Michelle Wang, Thea Wenxin. ",
                f"Last time updated on {formatted_date}.",
            ],
            style=FOOTER_STYLE,
        ),
    ]
)
