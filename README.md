# 🎵 Spotify Analyzer

Aplicação web desenvolvida em **Python + Streamlit** que analisa suas preferências musicais no Spotify, exibindo **top músicas** e **top artistas** de acordo com diferentes períodos de escuta.

---

## 🚀 Funcionalidades

- 🔐 Autenticação via Spotify (OAuth)
- 📅 Filtro por período de escuta:
  - Últimas 4 semanas
  - Últimos 6 meses
  - Todo o tempo
- 🎧 Top músicas mais ouvidas
- 🎤 Top artistas mais ouvidos
- 📊 Visualizações interativas com Plotly
- 🌙 Interface limpa e responsiva (dark theme)

---

## 📊 Sobre a métrica de popularidade

> ⚠️ **Importante:**  
> A *popularidade* exibida não representa o número exato de streams.

Ela é um **índice do Spotify (0–100)** que considera:
- Volume de reproduções
- Recência dos streams
- Tendência de consumo

Ou seja, músicas mais recentes e mais ouvidas tendem a ter valores maiores.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **Streamlit**
- **Spotipy (Spotify Web API)**
- **Pandas**
- **Plotly Express**

---

## 📂 Estrutura do projeto

```text
spotify-analyzer/
│
├── app.py                 # Aplicação Streamlit
├── spotify_client.py      # Autenticação Spotify (OAuth)
├── data_processing.py     # Coleta e tratamento de dados
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Documentação
