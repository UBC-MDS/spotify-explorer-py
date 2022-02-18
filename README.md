# spotify-explorer-py

Spotify explorer is a python dashboard implemented in Dash in order to help business analysts, product content managers visualize and understand the current trends in the music industry. 

## Dashboard description

The app contains a landing page that shows 4 graphs 
- Ranking of top artists by average popularity score filtered by Genre 
    * Here the user can select a particular `genre` of music by using the drop down list for genre located on the left hand side of the dashboard. 
- Popularity Trend of Specific Artists across time
    * The user on choosing a specific artist from a different down drop list, will be provided with a line chart of the artist's avergae popularity score over the years.
- Popularity Distribution of Specific Artists 
    * Based on the artist chosen from the previous drop down list, this plot will show the distribution of the Artist's popluarity score. This helps the user identify the artists that have many number of popular songs.
- Popular Song Characteristics
    * A seperate drop down list for song characteristics help users choose from a list of attributes such as `loudness`, `danceability`, etc. The plot then shows the relationship of the chosen attribute with popularity through a scatter plot.

All plots have interactivity embedded which help users zoom in, crop and hover around data points.

## Proposed Design Layout

<img width="919" alt="Screenshot 2022-02-18 at 3 30 19 AM" src="https://user-images.githubusercontent.com/37771404/154680473-13514b7a-c765-4a8e-bc2b-1775e0df5d4d.png">





## Contributors
- Christopher Alexander 
- Jennifer Hoang
- Thea Wenxin
- Michelle 
