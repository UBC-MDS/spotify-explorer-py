# author: Christopher Alexander, Jennifer Hoang, Michelle, Thea Wenxin
# date: 2022-03-01

import altair as alt
import pandas as pd
from dash import Dash, dcc, html, Input, Output

# Intial read data for prototype    
df = pd.read_csv("../data/raw/spotify.csv")
print(df.head())