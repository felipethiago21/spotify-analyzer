import streamlit as st
import plotly.express as px

# Importa o cliente autenticado do Spotify
from spotify_client import get_spotify_client

# Importa funções responsáveis pelo processamento dos dados
from data_processing import get_top_tracks, get_top_artists


# ================= CONFIGURAÇÃO DA PÁGINA =================
st.set_page_config(
    page_title="Spotify Analyzer",
    layout="wide"
)

st.title("🎵 Spotify Data Analyzer")


# ================= FILTRO DE PERÍODO =================
periodo = st.selectbox(
    "📅 Selecione o período",
    [
        "Últimas 4 semanas",
        "Últimos 6 meses",
        "Todo o tempo"
    ]
)

st.caption(
    "Os dados abaixo refletem suas preferências_attach de escuta no Spotify, "
    "de acordo com o período selecionado."
)

period_map = {
    "Últimas 4 semanas": "short_term",
    "Últimos 6 meses": "medium_term",
    "Todo o tempo": "long_term"
}

time_range = period_map[periodo]


# ================= BUSCA DE DADOS =================
sp = get_spotify_client()

df_top_tracks = get_top_tracks(sp, limit=10, time_range=time_range)
df_artists = get_top_artists(sp, limit=10, time_range=time_range)

if df_top_tracks.empty:
    st.warning("Nenhuma música encontrada para o período selecionado.")
    st.stop()

if df_artists.empty:
    st.warning("Nenhum artista encontrado para o período selecionado.")
    st.stop()


# ================= TRATAMENTO DOS DADOS =================
df_top_tracks = df_top_tracks.sort_values("Popularidade")
df_artists = df_artists.sort_values("Popularidade")

top_track = df_top_tracks.iloc[-1]["Música"]
top_artist = df_artists.iloc[-1]["Artista"]


# ================= GRÁFICOS =================
col1, col2 = st.columns(2)


# -------- TOP MÚSICAS --------
with col1:
    st.header("🎧 Top músicas mais ouvidas")
    st.divider()

    fig_tracks = px.bar(
        df_top_tracks,
        x="Popularidade",
        y="Música",
        orientation="h",
        color="Popularidade",
        color_continuous_scale="Blues",
        labels={"Popularidade": "Popularidade da música"},
        height=450
    )

    fig_tracks.update_layout(
        coloraxis_showscale=False,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    fig_tracks.update_traces(
        hovertemplate="<b>%{y}</b><br>Popularidade: %{x}<extra></extra>"
    )

    st.plotly_chart(fig_tracks, width="stretch")

    st.markdown(
        f"<p style='text-align:center; color:#A0A0A0;'>🎵 Música mais ouvida: <b>{top_track}</b></p>",
        unsafe_allow_html=True
    )


# -------- TOP ARTISTAS --------
with col2:
    st.header("🎤 Top artistas mais ouvidos")
    st.divider()

    fig_artists = px.bar(
        df_artists,
        x="Popularidade",
        y="Artista",
        orientation="h",
        color="Popularidade",
        color_continuous_scale="Purples",
        labels={"Popularidade": "Popularidade do artista"},
        height=450
    )

    fig_artists.update_layout(
        coloraxis_showscale=False,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    fig_artists.update_traces(
        hovertemplate="<b>%{y}</b><br>Popularidade: %{x}<extra></extra>"
    )

    st.plotly_chart(fig_artists, width="stretch")

    st.markdown(
        f"<p style='text-align:center; color:#A0A0A0;'>🎤 Artista mais ouvido: <b>{top_artist}</b></p>",
        unsafe_allow_html=True
    )


# ================= AVISO GLOBAL =================
st.divider()

st.markdown(
    """
    <p style="text-align: center; font-size: 0.85rem; color: #9CA3AF;">
        ⚠️ A popularidade é um índice do Spotify (0–100) que considera
        volume e recência dos streams, não o total absoluto de reproduções.
    </p>
    """,
    unsafe_allow_html=True
)
