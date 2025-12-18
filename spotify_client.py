import os
import spotipy
import streamlit as st
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    scope = "user-top-read"

    auth_manager = SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        open_browser=False,
        cache_path=".spotify_cache"
    )

    token_info = auth_manager.get_cached_token()

    if not token_info:
        auth_url = auth_manager.get_authorize_url()

        st.markdown("## 🔐 Login necessário")
        st.markdown(
            f"👉 [Clique aqui para entrar com o Spotify]({auth_url})"
        )
        st.stop()

    return spotipy.Spotify(auth_manager=auth_manager)
