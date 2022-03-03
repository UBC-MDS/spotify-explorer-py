# author: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin
# date: 2022-03-01

import altair as alt
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import layout_components as lc

alt.data_transformers.disable_max_rows()

# Read raw data
df = pd.read_csv("../data/raw/spotify.csv", parse_dates=['track_album_release_date'])
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
def top_artists():
    pass

## Plot2
@app.callback(
    Output('artist_trend_plot', 'srcDoc'),
    Input('artist_selection', 'value')
)

def artist_trend_plot(track_artist = 'Ed Sheeran'):
    
    trend_data = df.query("track_artist == 'Ed Sheeran' ")

    if track_artist != "Ed Sheeran":
        trend_data = df.query("track_artist == @track_artist")
        
    chart = alt.Chart(trend_data).mark_line().encode(
        alt.X('track_album_release_date', axis=alt.Axis(title="Album release date")),
        alt.Y('mean(track_popularity)', axis=alt.Axis(title="Popularity")))\
            .properties(height=250, width=350, background='#eeeeef')
        #tooltip=track_artist).interactive()
    return chart.to_html()

## Plot3
def artist_popularity_hist():
    pass

## Plot4
def popular_non_popular_line():
    pass










if __name__ == "__main__":
    app.run_server(debug=True)
