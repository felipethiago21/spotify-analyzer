import os
import spotipy
import streamlit as st
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    scope = "user-top-read"

    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        open_browser=False,  # 🔴 IMPORTANTE no Streamlit Cloud
    )

    # 🔐 Se ainda não existe token válido, força login
    if not auth_manager.validate_token(auth_manager.cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()

        st.markdown("## 🔐 Login necessário")
        st.markdown(
            f"""
            👉 [Clique aqui para entrar com o Spotify]({auth_url})
            """
        )
        st.stop()

    # ✅ Token válido → cria cliente Spotify
    return spotipy.Spotify(auth_manager=auth_manager)
