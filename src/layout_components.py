# author: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin
# date: 2022-03-01

import pandas as pd
from datetime import datetime
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


today = datetime.now()
formatted_date = today.strftime("%b %d, %Y")

SPOTIFY_LOGO = "assets/img/spotify-ex.png"


def get_artist_section():
    """
    1 row
    2 columns
    1col - Widgets
    2col - with 2 rows where first row is 1 column and other row is 2 columns
    """

    sidebar_widegets = dbc.Col(
        children=[
            html.H1("Sidebar widgets", className="display-30"),
            html.Iframe(
                id="widget_id",
                style={
                    "width": "20%",
                    "height": "100px",
                    "border": "0px",
                },
            ),
        ]
    )

    plot_1_settings = dbc.Col(
        [
            html.H1("Plot 1 with Artist/Genre", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="artist_genre_bar_id",
                style={
                    "width": "100%",
                    "height": "350px",
                    "border": "0px",
                },
            ),
        ]
    )

    plot_2_settings = dbc.Col(
        [
            html.H1("Plot 2 with Artist trend", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="artist_trend_id",
                style={
                    "width": "50%",
                    "height": "350px",
                    "border": "0px",
                },
            ),
        ]
    )

    plot_3_settings = dbc.Col(
        [
            html.H1("Plot 3 with Artist pop histogram", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="artist_pop_hist_id",
                style={
                    "width": "50%",
                    "height": "350px",
                    "border": "0px",
                },
            ),
        ]
    )

    section = html.Div(
        [
            dbc.Row(
                children=[
                    sidebar_widegets,
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


def get_popularity_section():
    """
    1 row
    2 columns
    1col - Widgets
    2col - Plot
    """
    sidebar_widegets = dbc.Col(
        children=[
            html.H1("Sidebar widgets", className="display-30"),
            html.Iframe(
                id="widget_id2",
                style={
                    "width": "20%",
                    "height": "100px",
                    "border": "0px",
                },
            ),
        ]
    )

    plot_4_settings = dbc.Col(
        [
            html.H1("Plot 4 for pop/unpop", className="display-30"),
            # Pseudo code for plot specfication, pleae modify
            html.Iframe(
                id="pop_unpop_id",
                style={
                    "width": "100%",
                    "height": "350px",
                    "border": "0px",
                },
            ),
        ]
    )

    section = html.Div([dbc.Row(children=[sidebar_widegets, plot_4_settings])])

    return section


def get_tab_section():
    tab_section = html.Div(
        [
            dbc.Tabs(
                [
                    dbc.Tab(label="Artist specific", tab_id="tab-1"),
                    dbc.Tab(label="Popular", tab_id="tab-2"),
                ],
                id="tabs",
                active_tab="tab-1",
            ),
            html.Div(id="tab-content"),
        ]
    )
    return tab_section


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=SPOTIFY_LOGO, height="70px")),
                        dbc.Col(dbc.NavbarBrand("Spotify Explorer", className="py-10")),
                    ],
                    align="center",
                    className="g-0",
                )
            )
        ]
    )
)

container = dbc.Container(
    [
        html.Br(),
        get_tab_section(),
        html.Footer(
            [
                f"(C) Copyright MIT License: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin. ",
                f"Last time updated on {formatted_date}.",
            ],
            # style=FOOTER_STYLE,
        ),
    ]
)
