# CPS4003-Programming-Project
# This program analyses a dataset of YouTube trending videos and allows users to view statistics, generate visualisations, and export results. The application processes data from a CSV file and provides both a text-based interface and a graphical user interface (GUI) for interaction.

How the Program Works

Program Starts by running main.py which will automatically bootup the GUI
The YouTube trending videos dataset (youtube_trending_videos.csv) is loaded into memory.
The graphical user interface (GUI) is then launched with the loaded data.

When the program starts, a graphical user interface (GUI) opens. The interface is divided into a menu panel on the left and a content area on the right. Users interact with the program by clicking buttons and switching between tabs.



---Home---
Returns the user to the welcome screen, can be used to return to home.



---Show Videos---
Displays the total number of unique videos and total number of unique channels in the dataset.



---Show Categories---
This option shows how videos are distributed across categories and contains 3 tabs:

- List View Tab
Displays a list of all category IDs.

- Pie Chart Tab
Displays a pie chart visualising the distribution of videos across categories.

- Category metrics Tab
Shows relevent category metrics for each tab and can be exported



---Find Video---

Allows the user to search for a video by video ID or title.
If a match is found, all details of the video are displayed.
Includes an Export to JSON button, which saves the selected video’s data as a JSON file.



---Show Top 10---
This section displays the most popular videos based on different engagement metrics and contains multiple tabs:

- Views Tab
Shows the top 10 videos ranked by view count.
Export button will export the currently selected top 10 list to a CSV file.

- Likes Tab
Shows the top 10 videos ranked by number of likes.
Export button will export the currently selected top 10 list to a CSV file.

- Comments Tab
Shows the top 10 videos ranked by comment count.
Export button will export the currently selected top 10 list to a CSV file.



---Show Histograms---
This option visualises engagement data using histograms and contains four tabs:

- Views Tab
Displays a histogram showing the distribution of video views.

- Likes Tab
Displays a histogram showing the distribution of video likes.

- Comments Tab
Displays a histogram showing the distribution of video comments.



---Trending Analysis---
This option shows a line graph for tranding videos across the top 5 categories across 3 days