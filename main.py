import os
import re
import sys
import shutil
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_dl
from youtube_api import YoutubeDataApi
import config

# Set Configurations
spotify_client_id               = config.SPOTIFY_CLIENT_ID
spotify_client_secret           = config.SPOTIFY_API_SECRET
youtube_data_api_key              = config.YOUTUBE_API_SECRET
youtube_dl_options      = config.YOUTUBE_DL_OPTIONS

# Authenticate APIs
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(spotify_client_id, spotify_client_secret))
yt = YoutubeDataApi(youtube_data_api_key)

def main():
    playlist_uris = sys.argv[1:]
    for pl_uri in playlist_uris:
        if pl_uri is None: 
            print('No valid playlists uris were provided.')
            return
        download_tracks(get_tracks(sp.playlist_tracks(pl_uri, fields='items.track.album.artists, items.track.name')))
       
def download_tracks(tracks):
    for i in range(len(tracks)):
            video_id = yt.search(q=tracks[i]['artist'] + ' ' + tracks[i]['track_name'], max_results=5)[0]['video_id']
            with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
                ydl.download(['https://www.youtube.com/watch?v={}'.format(video_id)])

def get_tracks(playlist):
    tracks = []
    for track in playlist['items']:
        track_info = { 
            'artist': track['track']['album']['artists'][0]['name'], 
            'track_name': track['track']['name'],
            }
        tracks.append(track_info)
    return tracks
                 
def create_output_dir():
    if not os.path.exists('output'):
        os.makedirs('output')
        os.chdir('output')
    return

if __name__ == "__main__":
    create_output_dir()
    main()
