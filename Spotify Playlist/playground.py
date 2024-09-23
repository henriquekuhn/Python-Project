import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "ee60e7f323a94126909bc594722aea14"
SPOTIFY_SECRET = "d24720242a114ed8b476894c558058e6"

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
print(sp.current_user())