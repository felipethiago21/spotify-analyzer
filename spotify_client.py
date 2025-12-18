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
        open_browser=False,
        cache_handler=None,  # 🔴 ESSENCIAL NO STREAMLIT CLOUD
    )

    try:
        sp = spotipy.Spotify(auth_manager=auth_manager)
        # força chamada simples para validar token
        sp.current_user()
        return sp

    except Exception:
        auth_url = auth_manager.get_authorize_url()

        st.markdown("## 🔐 Login necessário")
        st.markdown(
            f"👉 [Clique aqui para entrar com o Spotify]({auth_url})"
        )
        st.stop()
