from bs4 import BeautifulSoup
import requests
from datetime import datetime
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

URL = "https://www.billboard.com/charts/hot-100/"
travel_date = input("Enter the date you want to travel to (YYYY-MM-DD): ")
playlist_name = f"{travel_date} Billboard 100"

response = requests.get(f"{URL}/{travel_date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.select(".o-chart-results-list-row-container ul li h3")
song_names = [song.text.strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private playlist-read-private",
        cache_path="token.txt"
    )
)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]
print(f"User {user_name} is logged in.")

try:
    for play_list_i in sp.current_user_playlists()['items']:
        if playlist_name in play_list_i['name']:
            print("The playlist already exists.")
            break
    else:
        song_uris = []
        for song in song_names:
            year = datetime.strptime(travel_date, "%Y-%m-%d").year
            try:
                uri = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)['tracks']['items'][0]['uri']
                song_uris.append(uri)
            except Exception as e:
                print(f"Error occurred while getting uri of a song: {e}")

        try:
            playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False,
                                               description=f"Top 100 songs from {travel_date}")
        except Exception as e:
            print(f"Error occurred while creating playlist: {e}")
        else:
            sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
            print("Playlist has been successfully created.")
except Exception as e:
    print(f"Error occurred: {e}")

