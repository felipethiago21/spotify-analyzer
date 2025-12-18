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
    )

    # 🔎 Captura parâmetros da URL
    query_params = st.query_params
    code = query_params.get("code")

    # 🔁 Se veio código do Spotify, troca por token
    if code:
        auth_manager.get_access_token(code, as_dict=False)
        st.query_params.clear()
        st.rerun()

    # 🔐 Se não tem token válido → login
    token = auth_manager.get_cached_token()
    if not token or not auth_manager.validate_token(token):
        auth_url = auth_manager.get_authorize_url()

        st.markdown("## 🔐 Login necessário")
        st.markdown(
            f"👉 [Clique aqui para entrar com o Spotify]({auth_url})"
        )
        st.stop()

    return spotipy.Spotify(auth_manager=auth_manager)
