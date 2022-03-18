# Reflections

### Our implementations so far
Our Spotify Explorer app contains 4 main plots that are helpful for exploring trends and insights involving artists, genres, song characteristics and popularity. Since we are mainly focused on helping music companies like Spotify discover potential in artists, popularity is a key metric that we are showing in our plots in relation to artists and music found on Spotify. We divided our dashboard into two main sections under separate tabs, the first tab consisting 3 plots that reveal insights on top ten popular artists by genre (barplot), how popular an artist is over time (trend plot), and each individual artist's own distribution of popularity (histogram). The second tab focuses solely on song characteristics and its interaction with popularity by 2 classes: popular and not-popular through segregation via median popularity. This section reveals interesting distribution patterns on song characteristics from different genres via a distribution plot. We developed 2 versions of this same app: on Python and R.


### What has yet to be implemented
What has not been implemented yet is to incorporate interactivity between the plots in the first section since they are all focused on artist and their popularity. We planned to include the interactions, because that would be insightful and engaging for the user. However, since we used the `altair` package as our plotting package for the Python app, there were some limitations and restrictions that altair has on interactions between plots so we were not able to implement those interactions (or at least within the limited time, find a good solution). We will however continue keeping an eye out for potential solutions to this issue and hopefully be able to implement it sometime in the near future.


### Feedback received for our app
* **Has it been easy to use your app?**

We received positive feedback from peers and mentors on the ease of use of our app, mainly because the design is simple and intuitive, and has elements of coherence. There was no complaints of difficulty in using the app so far. We do note that at the point when feedback was provided, there were some feedback on improving the explanation of plots so users can understand them better. We have thus implemented these feedback in our milestone 4 version of the apps, and included sidebar explanations, a navbar "about" section, and clearer titles for plots.

* **Are there recurring themes in your feedback on what is good and what can be improved?**

With regards to improvements, we received suggestions about providing further explanations on how the graphs were made, such as thresholds selected as definition of popularity for the song characteristics plot. We added descriptions to explain how popular and non-popular classes are divided on the sidebar. Also, the red line on the histogram plot could also be defined more clearly, and we added that to the title of the plot as well. Other feedback on improvements also included to change the logo from Spotify's official logo to another one due to copyright issues, so we designed our very own logo and replaced it with that. Our mentor also pointed out that the background of our plots can be differentiated better than just pure white so we made changes aesthetically to the plots too.

* **What differences are there between the DashR and DashPy app?**

The DashPy app was our main focus, so there are more aesthetic modifications in that app as compared to the DashR app. So the main differences are plot design and aesthetics. The DashPy app also has an added feature at the navbar which is an 'about' section, giving users more context of the data source and types.

* **Is there any insights that you have found particularly valuable during your dashboard development?**

This was a fun and challenging dashboard to build, because we had to use bootstrap components which was completely new to most of us, and incorporate many R/Python visualization packages to help us achieve this end product. Overall, we have gained alot of experience and knowledge from this process in terms of understanding the differences between R and Python visualization development work, particularly using Dash. It has definitely sharpened our design and coding skills, as well as team work skills at the same time. 
