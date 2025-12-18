import pandas as pd
import warnings

# Ignora avisos futuros do pandas para evitar poluição no log
warnings.filterwarnings("ignore", category=FutureWarning)


def get_top_tracks(sp, limit=30, time_range="medium_term"):
    """
    Busca as músicas mais ouvidas do usuário no Spotify
    e retorna os dados em um DataFrame do pandas.
    """

    # Chamada à API do Spotify para obter as top tracks do usuário
    response = sp.current_user_top_tracks(
        limit=limit,
        time_range=time_range
    )

    # Lista que irá armazenar os dados das músicas
    tracks = []

    # Percorre cada música retornada pela API
    for item in response["items"]:
        tracks.append({
            # ID único da música no Spotify
            "id": item["id"],

            # Nome da música
            "Música": item["name"],

            # Nome do primeiro artista associado à música
            "Artista": item["artists"][0]["name"],

            # Popularidade da música no Spotify (0 a 100)
            "Popularidade": item["popularity"]
        })

    # Converte a lista de músicas em um DataFrame
    return pd.DataFrame(tracks)


def get_top_artists(sp, limit=20, time_range="medium_term"):
    """
    Busca os artistas mais ouvidos do usuário no Spotify
    e retorna os dados em um DataFrame do pandas.
    """

    # Chamada à API do Spotify para obter os top artistas do usuário
    response = sp.current_user_top_artists(
        limit=limit,
        time_range=time_range
    )

    # Lista que irá armazenar os dados dos artistas
    artists = []

    # Percorre cada artista retornado pela API
    for item in response["items"]:
        artists.append({
            # Nome do artista
            "Artista": item["name"],

            # Popularidade do artista no Spotify (0 a 100)
            "Popularidade": item["popularity"],

            # Quantidade total de seguidores do artista
            "Seguidores": item["followers"]["total"]
        })

    # Converte a lista de artistas em um DataFrame
    return pd.DataFrame(artists)
