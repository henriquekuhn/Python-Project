import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

DIR = os.getcwd() + "/Day 46 - Spotify Playlist"
os.chdir(DIR)

load_dotenv()

SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#date = "1990-05-27"
year = date.split("-")[0]
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
#response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#print(song_names)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Henrique Cafruni Kuy", 
    )
)
user_id = sp.current_user()["id"]

n = 0
song_uri = [] 
#Searching Spotify for songs by title
for song in song_names:
    result = sp.search(q=f'{song[0]} {year}', type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
        print(f'Track {n+1} added...')
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    else:
        n += 1

print("All tracks added")        

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)