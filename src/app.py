# author: Christopher Alexander, Jennifer Hoang, Michelle Wang, Thea Wenxin
# date: 2022-03-01

import altair as alt
import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import layout_components as lc

alt.data_transformers.disable_max_rows()

# Read raw data
df = pd.read_csv("data/raw/spotify.csv", parse_dates=["track_album_release_date"])
df.dropna(inplace=True)

# Set up app frontend
app = Dash(
    __name__,
    title="Spotify Explorer",
    # MORPH - another stylesheet
    external_stylesheets=[dbc.themes.MINTY],
    suppress_callback_exceptions=True,
)

server = app.server

app.layout = html.Div([lc.navbar, lc.container], style={"backgroundColor": "#eeeeef"})

# Tabs ----------


@app.callback(Output("tab-content", "children"), [Input("tabs", "active_tab")])
def switch_tab(tab_id):
    if tab_id == "tab-1":
        return lc.get_artist_section()
    elif tab_id == "tab-2":
        return lc.get_popularity_section()
    return html.P("This shouldn't ever be displayed...")


# Plots -------------

## Plot1
@app.callback(Output("artist_genre_bar_id", "srcDoc"), Input("genre", "value"))
def top_artists(genre):
    top10_data = (
        df.query("playlist_genre == @genre")
        .groupby(["track_artist"])
        .mean("track_popularity")
        .nlargest(10, "track_popularity")
        .reset_index()
    )
    click = alt.selection_multi()

    chart = (
        alt.Chart(top10_data)
        .mark_bar()
        .encode(
            x=alt.X(
                "track_popularity", axis=alt.Axis(title="Average Track Popularity")
            ),
            y=alt.Y("track_artist", sort="-x", axis=alt.Axis(title="Artist")),
            opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
            tooltip="track_popularity",
        )
        .add_selection(click)
    )
    return chart.to_html()


## Plot2
@app.callback(Output("artist_trend_plot", "srcDoc"), Input("artist_selection", "value"))
def artist_trend_plot(track_artist="Ed Sheeran"):

    trend_data = df.query("track_artist == 'Ed Sheeran' ")

    if track_artist != "Ed Sheeran":
        trend_data = df.query("track_artist == @track_artist")

    c1 = (
        alt.Chart(trend_data)
        .mark_line()
        .encode(
            alt.X(
                "track_album_release_date", axis=alt.Axis(title="Album release date")
            ),
            alt.Y("mean(track_popularity)", axis=alt.Axis(title="Popularity")),
        )
    )

    chart = c1 + c1.mark_point()
    # chart.properties(height=300, width=350, background='#eeeeef')
    return chart.to_html()


## Plot3
def artist_popularity_hist():
    pass


## Plot4
@app.callback(
    Output("pop_unpop_id", "srcDoc"),
    Input("genres", "value"),
    Input("xcol-widget", "value"),
)
def popular_non_popular_line(genre, feat):
    data_pop = df
    data_pop["Duration (min)"] = data_pop["duration_ms"] / 60000
    data_pop["Popularity class"] = np.where(
        data_pop["track_popularity"] <= data_pop["track_popularity"].median(),
        "Not popular",
        "Popular",
    )
    data_pop["Genres"] = data_pop["playlist_genre"].replace(
        ["edm"], ["electronic dance music"]
    )
    data_pop_query = data_pop.query("Genres == @genre")
    chart = (
        alt.Chart(
            data_pop_query,
            title=f"Distribution of {feat} over Popular and Not popular songs in {genre}",
        )
        .mark_line(interpolate="monotone")
        .encode(
            alt.X(feat, bin=alt.Bin(maxbins=30), title=f"{feat.title()}"),
            y="count()",
            color="Popularity class",
        )
        .configure_axis(labelFontSize=14, titleFontSize=14)
        .configure_legend(titleFontSize=14)
        .configure_title(fontSize=18)
    )

    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug=True)
