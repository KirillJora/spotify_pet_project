import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-recently-played"

load_dotenv()

client_id =os.getenv('CLIENT_ID')
client_secret =os.getenv('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri="http://localhost:9090/"  # This URI needs to be registered in your Spotify app settings
))

tracks = sp.current_user_recently_played()

for i, item in enumerate(tracks['items']):
    track = item['track']
    print(f"{i+1} - {track['artists'][0]['name']} - {track['name']}")


# auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(auth_manager=auth_manager)

# current_plays = sp.current_user_recently_played(limit = 50)

# print(current_plays)

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None