SPOTIFY_CLIENT_ID = ""
SPOTIFY_API_SECRET = ""
YOUTUBE_API_SECRET = ""

YOUTUBE_DL_OPTIONS = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}