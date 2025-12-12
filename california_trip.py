import streamlit as st
import datetime
import requests

# --- Configuração da Página ---
st.set_page_config(
    page_title="Roteiro Califórnia",
    page_icon="🗺️",
    layout="centered"
)

# --- Cálculo de Datas e Distribuição ---
DIAS_TOTAIS = 24
DIAS_SD = 7
DIAS_SF = 5
DIAS_VIAGEM = 2  # Parada na Highway 1 / Monterey
DIAS_ANAHEIM_LA = DIAS_TOTAIS - DIAS_SD - DIAS_SF - DIAS_VIAGEM  # 24 - 7 - 5 - 2 = 10 dias

DATA_INICIO = datetime.date(2025, 12, 25)

# Distribuição das datas
def get_dates(start_date, duration):
    end_date = start_date + datetime.timedelta(days=duration - 1)
    return f"{start_date.strftime('%d/%b')} a {end_date.strftime('%d/%b')}"


SD_START = DATA_INICIO
SF_START = SD_START + datetime.timedelta(days=DIAS_SD)
HW1_START = SF_START + datetime.timedelta(days=DIAS_SF)
ANAHEIM_START = HW1_START + datetime.timedelta(days=DIAS_VIAGEM)

# --- Função para Previsão do Tempo ---
def get_weather_forecast(city_name):
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
    except (FileNotFoundError, KeyError):
        return "Chave de API não configurada."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br"
    }
    headers = {'Cache-Control': 'no-cache'}

    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Lança exceção para status de erro (4xx ou 5xx)
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"{temp:.0f}°C, {description.capitalize()}"
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            return "Erro: Chave de API inválida ou não ativada."
        if e.response.status_code == 404:
            return f"Cidade '{city_name}' não encontrada."
        return f"Erro HTTP: {e.response.status_code}"
    except requests.exceptions.RequestException:
        return "Erro de conexão com a API."
    except (KeyError, IndexError):
        return "Dados da previsão incompletos."


# --- Dados do Roteiro ---
roteiro_data = {
    f"☀️ San Diego ({DIAS_SD} Dias)": {
        "icon": "☀️",
        "dias": get_dates(SD_START, DIAS_SD),
        "cidade_api": "San Diego",
        "destaques": [
            ("🦁", "**San Diego Zoo & Balboa Park**", "Um dos melhores zoológicos do mundo."),
            ("🌊", "**La Jolla Cove & Seals**", "Passeio para ver leões marinhos e focas."),
            ("⚓", "**USS Midway Museum**", "Explore o gigantesco porta-aviões."),
            ("🏖️", "**Coronado Beach**", "Visite a praia e o histórico Hotel del Coronado."),
            ("🏛️", "**Maritime Museum**", "Museu com navios históricos e um submarino."),
            ("🤠", "**Old Town San Diego**", "Explore a história da cidade."),
            ("💡", "**Gaslamp Quarter**", "Bairro histórico com vida noturna animada."),
            ("🎢", "**Belmont Park**", "Parque de diversões na praia Mission Beach."),
            ("🧱", "**Legoland California**", "Parque temático focado em blocos de montar."),
            ("🐠", "**Birch Aquarium at Scripps**", "Aquário com túnel de observação subaquática."),
            ("🛍️", "**Compras no Outlet**", "Visite o outlet para compras de marcas famosas.")
        ]
    },
    f"🌁 San Francisco ({DIAS_SF} Dias)": {
        "icon": "🌁",
        "dias": get_dates(SF_START, DIAS_SF),
        "cidade_api": "San Francisco",
        "destaques": [
            ("🌉", "**Ponte Golden Gate**", "Atravessar a pé para vistas incríveis."),
            ("🔑", "**Ilha de Alcatraz**", "Passeio de balsa para a antiga prisão."),
            ("🦁", "**Fisherman's Wharf & Pier 39**", "Leões-marinhos e Musée Mécanique."),
            ("🚡", "**Passeio de Teleférico (Cable Car)**", "Forma divertida de conhecer a cidade."),
            ("🔬", "**California Academy of Sciences**", "Planetário, aquário e floresta tropical."),
            ("🚶", "**Explore os Bairros**", "Caminhar por Chinatown e Little Italy."),
            ("🌲", "**Muir Woods & Sausalito**", "Excursão para ver as sequoias gigantes."),
        ]
    },
    f"🛣️ Highway 1 (2 Dias)": {
        "icon": "🛣️",
        "dias": get_dates(HW1_START, DIAS_VIAGEM),
        "cidade_api": "Monterey",
        "destaques": [
            ("🐠", "**Monterey Bay Aquarium**", "Excelente parada no caminho para o sul."),
            ("🌉", "**Bixby Bridge (Big Sur)**", "A foto clássica da Highway 1."),
            ("🐘", "**Elefantes Marinhos em Piedras Blancas**", "Ponto de observação em San Simeon."),
            ("🏡", "**Carmel-by-the-Sea**", "Cidade charmosa para um almoço ou café.")
        ]
    },
    f"🎡 Anaheim, L.A. e Parques ({DIAS_ANAHEIM_LA} Dias)": {
        "icon": "🎬",
        "dias": get_dates(ANAHEIM_START, DIAS_ANAHEIM_LA),
        "cidade_api": "Anaheim",
        "destaques": [
            ("✨", "**Disneyland & California Adventure**", "Foco: Star Wars e Avengers Campus."),
            ("🧙", "**Universal Studios Hollywood**", "Prioridade: Super Nintendo World e Harry Potter."),
            ("🍓", "**Knott's Berry Farm**", "Primeiro parque temático dos EUA."),
            ("🎢", "**Six Flags Magic Mountain**", "Ideal para amantes de montanhas-russas."),
            ("🛍️", "**Downtown Disney**", "Área de compras e restaurantes."),
            ("🎡", "**Santa Monica Pier**", "Píer icônico com parque de diversões."),
            ("🔭", "**Griffith Observatory**", "Vistas de L.A. e do Letreiro de Hollywood."),
            ("⭐", "**Hollywood Blvd**", "Calçada da Fama e TCL Chinese Theatre."),
            ("🐠", "**Aquarium of the Pacific**", "Aquário em Long Beach."),
        ]
    }
}


# --- Função Principal para Renderização ---
def main():
    st.title("🗺️ Férias Califórnia")
    st.markdown("### 🗓️ 25 Dezembro a 17 Janeiro - 24 Dias")
    st.markdown("---")

    tabs = st.tabs(list(roteiro_data.keys()))

    for i, (cidade_key, info) in enumerate(roteiro_data.items()):
        with tabs[i]:
            st.header(f"{info['icon']} {cidade_key}")
            st.subheader(f"Período: {info['dias']}")

            # Usa a chave 'cidade_api' para a previsão do tempo
            cidade_para_previsao = info.get("cidade_api", "")
            if cidade_para_previsao:
                previsao = get_weather_forecast(cidade_para_previsao)
                st.info(f"**Tempo em {cidade_para_previsao}:** {previsao}")

            st.markdown("---")

            for emoji, titulo, descricao in info["destaques"]:
                with st.container(border=True):
                    st.markdown(f"### {emoji} {titulo}")
                    st.write(descricao)

            if "Highway 1" in cidade_key:
                st.warning("⚠️ **Logística:** Verifique as condições das estradas no inverno.")
            if "Anaheim" in cidade_key:
                st.info("💡 **Dica:** Focar 4-5 dias nos parques e o resto para explorar L.A.")


# --- Execução ---
if __name__ == "__main__":
    main()
