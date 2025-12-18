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

    # 1️⃣ Já tem token salvo
    token_info = auth_manager.get_cached_token()
    if token_info:
        return spotipy.Spotify(auth_manager=auth_manager)

    # 2️⃣ Voltou do Spotify com ?code=
    query_params = st.query_params
    if "code" in query_params:
        auth_manager.get_access_token(query_params["code"])
        st.query_params.clear()
        st.rerun()

    # 3️⃣ Tela de login
    auth_url = auth_manager.get_authorize_url()

    components.html(
        f"""
        <div style="
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            height:60vh;
            color:white;
            font-family:Arial;
        ">
            <h2>🔐 Login necessário</h2>
            <p>Conecte sua conta do Spotify para ver seus dados</p>

            <button
                onclick="window.top.location.href='{auth_url}'"
                style="
                    background-color:#1DB954;
                    color:white;
                    padding:14px 30px;
                    border:none;
                    border-radius:30px;
                    font-size:16px;
                    cursor:pointer;
                    margin-top:20px;
                "
            >
                🎧 Entrar com Spotify
            </button>
        </div>
        """,
        height=320
    )

    st.stop()
