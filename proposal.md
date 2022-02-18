
# Proposal

### Motivation and purpose

- Our role: Spotify data science team
- Target audience: Spotify content team

The goal of the Spotify Explorer dashboard is to highlight current music trends and identify the most popular artists on Spotify. By summarizing the popularity and song characteristics of Spotify’s most popular artists in various genres, our dashboard can assist the Spotify Content Team with decisions related to building partnerships with artists and creating new exclusive content, as well as curating more engaging playlists that can attract new users and continue to appeal to existing users. Our dashboard will showcase the most popular artists on Spotify, their evolving popularity over time, the overall distribution of their song popularity, as well as the song characteristics associated with the type of music that they produce.


### Description of the data

Our dashboard will be visualizing a dataset describing Spotify's music data. This dataset was derived from TidyTuesday, an open-source dataset website which can be found [here](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21/readme.md). The dataset contains over 30,000 rows of data and provides useful information about music artists `track_artist`, popularity of tracks `track_popularity` which is a numeric value on a range from 0 (least popular) to 100 (most popular), genres of which the music belong `playlist_genre` such as pop or rock, `track_album_release_date` from 1950s to 2020 and interesting song/audio characteristics such as `loudness` and `key`. As our aim is to understand music popularity trends in artists and genres, our dashboard will focus primarily on data columns `track_popularity` and `track_artist` as well as `playlist_genre`. These variables are useful in providing insights on which artists and genres are rising in trend and allows Spotify executives to make better-informed decisions.

### Research questions and usage scenarios

The research questions are what feature characteristics of a song are strongly related to its popularity. Which artists are popular these years? What are the characteristics of their songs?
The target users for our dashboard are business analysts, product content managers, and the Music Mission Product Insights Team from Spotify. They will use our dashboard to explore the current trend of popularity of different singers and to make decisions on building partnerships with artists. For example, Lucy is a Music Content Manager, her daily work is to collect music content with high popularity and establish business relationships with target artists. To find popular songs, she needs to explore music with high popularity scores, and identify characteristics most relevant to those liked songs. When she uses our dashboard platform, she can clearly see the relationship between song features and popularity score, from which she's able to select songs based on their features. She will rank artists based on their popularity and find their popularity trend over the years to decide whether she needs to reach out to those artists for purchasing music license or cooperate with them to create unique content on the platform of Spotify. 






