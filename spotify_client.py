import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    scope = "user-top-read"

    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        open_browser=True,          # 🔴 ESSENCIAL NO STREAMLIT CLOUD
        cache_path=".spotify_cache" # cache local
    )

    return spotipy.Spotify(auth_manager=auth_manager)

