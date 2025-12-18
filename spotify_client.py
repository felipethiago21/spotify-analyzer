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
        cache_path=None  # 🔴 IMPORTANTE: sem cache no Streamlit Cloud
    )

    # 🔐 Se não houver token, força login manual
    token_info = auth_manager.get_cached_token()

    if not token_info:
        auth_url = auth_manager.get_authorize_url()
        st.markdown(
            f"""
            ### 🔐 Login necessário
            Para visualizar seus dados do Spotify, faça login:

            👉 [Clique aqui para entrar com o Spotify]({auth_url})
            """
        )
        st.stop()

    return spotipy.Spotify(auth_manager=auth_manager)
