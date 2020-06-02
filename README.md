# Spotify Playlist Downloader
A robust way to download any number of playlists from Spotify with just one command.

Table of Contents
==
<!--ts-->
  * [Getting Started](#getting-started)
  * [Spotify API Key](#spotify-api-key)
  * [Youtube Data API Key](#youtube-data-api-key)
  * [How to Run](#how-to-run)
<!--te-->

Getting Started
==
Spotify Playlist Downloader utilizes the Spotify API, Youtube Data API, and the Youtube-DL module. The progam uses the Spotify API to access Spotify playlists. The Youtube Data API is used to search for each song on each playlist on Youtube. Lastly, Youtube-DL downloads the audio from the Youtube video.
<!--br-->
To install dependencies:

```
pip install -r requirements.txt
```

Spotify API Key
==
To get the Spotify API key, login to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login) and create a new app. After which, you should be prompted with the 
option to generate an API key for your new app.

Youtube Data API Key
==
To get the Youtube Data API key, create a project in the [Google Developer Console](https://console.developers.google.com/). After which, you should see the option to generate a new API key for your project.

How to Run
==
Before running, copy all the Spotify playlist URI's from each playlist. You can do this by right-clicking the playlist, hovering over the `Share >` option, and clicking `Copy Playlist URI`. Copy as many as you'd like.

<!--br-->
To run the program:

```
python main.py uri_1 uri_2 uri_3 .. ..
```
