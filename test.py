import unittest
import config
import spotipy
import youtube_dl
import youtube_api	
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_api import YoutubeDataApi

# TODO: modularize the login and authentication
# Set the API keys
spotify_client_id = config.SPOTIFY_CLIENT_ID
spotify_client_secret = config.SPOTIFY_API_SECRET
youtube_data_api_key = config.YOUTUBE_API_SECRET
youtube_dl_options = config.YOUTUBE_DL_OPTIONS
	
# Authenticate		
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(spotify_client_id, spotify_client_secret))	
yt = YoutubeDataApi(youtube_data_api_key) 
	
class TestPlaylistDownloader(unittest.TestCase):

	def test_video_id(self):
		# Test 1
		video_id = yt.search('Rick Astley Never Gonna Give You Up', max_results=5)[0]['video_id']
		self.assertEqual(video_id, 'dQw4w9WgXcQ', '@method test_video_id TEST 1: Video ID Error.') 
		
		# Test 2
		video_id = yt.search('Michael Jackson Billie Jean', max_results=5)[0]['video_id']
		self.assertEqual(video_id, 'Zi_XLOBDo_Y', '@method test_video_id TEST 2: Video ID Error.')
		
		# Test 3
		video_id = yt.search('ACDC Highway to Hell', max_results=5)[0]['video_id']
		self.assertEqual(video_id, 'l482T0yNkeo', '@method test_video_id TEST 3: Video ID Error.')


	def test_playlist_uri(self):
		# Test playlist is public
		test_playlist_uri = "spotify:playlist:2zOyW0j0ndJ9jfNQKTdGry"
		playlist = sp.playlist_tracks(test_playlist_uri, fields='items.track.album.artists, items.track.name')	
		
		tracks = []
		for track in playlist['items']:
			track_info = {
            			'artist': track['track']['album']['artists'][0]['name'],
            			'track_name': track['track']['name'],
            		}
			tracks.append(track_info)
		
		self.assertEqual(tracks[0]['artist'] + " " + tracks[0]['track_name'], "AC/DC Highway to Hell", "@method test_playlist_uri TEST 1: Playlist URI Error")
		self.assertEqual(tracks[1]['artist'] + " " + tracks[1]['track_name'], "Michael Jackson Billie Jean", "@method test_playlist_uri TEST 2: Playlist URI Error")
		self.assertEqual(tracks[2]['artist'] + " " + tracks[2]['track_name'], "Rick Astley Never Gonna Give You Up", "@method test_playlist_uri TEST 3: Playlist URI Error") 

if __name__=='__main__':
	unittest.main()
	
