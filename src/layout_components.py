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
    '''
    2 columns 
    1col - Widgets 
    2col - with 2 rows where first row is 1 column and other row is 2 columns 
    '''
    pass
    # section = html.Div(
    #     [
    #         dbc.Row(
    #             [

    #             ]
    #         )
    #     ]

    # )

def get_popularity_section():
    '''
    2 columns 
    1col - Widgets 
    2col - with 2 rows where first row is 1 column and other row is 2 columns 
    '''
    pass


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
                        dbc.Col(dbc.NavbarBrand("Spotify Explorer",
                        className="py-10")),
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
            [f"(C) Copyright MIT License: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin. ",
             f"Last time updated on {formatted_date}."],
            # style=FOOTER_STYLE,
        ),
    ]
)