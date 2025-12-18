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

    # 🔐 SE NÃO TEM TOKEN → MOSTRA BOTÃO
    if not token_info:
        st.markdown(
            """
            <div style="text-align: center; margin-top: 80px;">
                <h2>🎵 Spotify Analyzer</h2>
                <p>Faça login para visualizar suas estatísticas musicais</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🎧 Entrar com Spotify"):
            auth_url = auth_manager.get_authorize_url()
            st.markdown(
                f"""
                <meta http-equiv="refresh" content="0; url={auth_url}">
                """,
                unsafe_allow_html=True
            )
            st.stop()

        st.stop()

    return spotipy.Spotify(auth_manager=auth_manager)
