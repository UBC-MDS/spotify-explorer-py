# Spotify Explorer App

Spotify Explorer is a data visualization dashboard app (built on Dash) displaying insights and trends on Spotify's music, artists and song types. This app is made for anyone who's keen in discovering what lies underneath a vast data collected on Spotify's platform, be they music enthusiasts or music business executives.

## The App

You can access the dashboard app here: [Spotify Explorer](https://spotify-explorer-pop.herokuapp.com/)
## Motivation and Purpose

Our purpose for developing this app can be branched into 2 main goals: to help others discover more about the artists, genres they care about and to help the music industry solve business problems with data. As music enthusiasts ourselves, we wanted to help fellow music fans understand more about their favourite artists, genres and song types. Furthermore, the app would be beneficial for music industry professionals who want to make business decisions on which artists and genres to develop their business in.

Below are just a couple of potential problem-solving scenarios to achieve these objectives:

- Music listeners may want to dive more into new music with a specific genre. Our app can display top popular atists belonging to that genre and listeners can try out listening to those artists, thereby discovering new music they may like.

- Business executives can use our tool to find trends in popularity of artists over the past few years, and decide whether to pursue contract extension with specific artists (based on the artist's performance). If they're interested to zoom into any specific artist, the histogram plot would be able to tell them what the distribution of popularity looks like for that artist. For example, if they prefer to pursue an artist with less variability in popularity, they can infer that from the plot.

## Dashboard description

The app contains 2 tabs that shows a total of four plots with sidebar widgets allowing users to control filtering 
options for the plots.

- **Top artists with an average popularity score (filtered by Genre)** <br>
Here the user can select a particular `genre` of music by using the drop down list for genre located on the left hand side of the dashboard. The plot shows the artist and their corresponding popularity score for the specific genre.
- **Popularity Trend of Specific Artists across time (filtered by Artist)** <br>
The user on choosing a specific artist from a different down drop list, will be provided with a line chart of the artist's average popularity score over the years.
- **Popularity Distribution of Specific Artists (filtered by Artist)** <br>
Based on the artist chosen from the previous drop down list, this plot will show the distribution of the Artist's popularity score. This helps the user identify the artist's popularity score across their songs.
- **Popular Song Characteristics (filtered by Genre)** <br>
Finally, a seperate drop down list for song characteristics help users choose from a list of attributes such as `loudness`, `danceability`, etc. The plot then shows the relationship of the chosen attribute with `popularity` through a scatter plot.


## App Design

<img width="919" src="./img/dashboard_gif.gif">

## If you want to help further develop the app
1. Fork [the repository](https://github.com/UBC-MDS/spotify-explorer-py/)
2. Set up conda environment as follows
```
$ conda env create -f spotify.yml
```
3. To run the app locally, run the following command from the root of this repository   
   `python src/app.py`
4. Create an issue on this repo to inform the Team about the changes/improvements you want to make. See **Contributing** section below for more details.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/spotify-explorer-py/blob/main/CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## App Contributors

- Christopher Alexander 
- Jennifer Hoang
- Thea Wenxin
- Michelle 

## License

`spotify-explorer-py` was created by Christopher Alexander, Jennifer Hoang, Thea Wenxin and Michelle Wang. It is licensed under the terms of the [MIT License](https://github.com/UBC-MDS/spotify-explorer-py/blob/main/LICENSE).

