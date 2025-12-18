import os
import spotipy
import streamlit as st
import streamlit.components.v1 as components
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    scope = "user-top-read"

    auth_manager = SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        cache_path=".spotify_cache",
        open_browser=False
    )

    # 1️⃣ Se já existe token
    token_info = auth_manager.get_cached_token()
    if token_info:
        return spotipy.Spotify(auth_manager=auth_manager)

    # 2️⃣ Se voltou do Spotify com ?code=
    query_params = st.query_params
    if "code" in query_params:
        auth_manager.get_access_token(query_params["code"])
        st.query_params.clear()
        st.rerun()

    # 3️⃣ Tela de login (HTML REAL)
    auth_url = auth_manager.get_authorize_url()

    components.html(
        f"""
        <div style="text-align:center; margin-top:120px;">
            <h2>🔐 Login necessário</h2>
            <p>Conecte sua conta do Spotify para ver seus dados</p>

            <a href="{auth_url}" target="_top" style="text-decoration:none;">
                <button style="
                    background-color:#1DB954;
                    color:white;
                    padding:14px 28px;
                    border:none;
                    border-radius:30px;
                    font-size:16px;
                    cursor:pointer;
                ">
                    🎧 Entrar com Spotify
                </button>
            </a>
        </div>
        """,
        height=280
    )

    st.stop()
