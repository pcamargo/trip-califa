import streamlit as st
import datetime

# --- Configuração da Página ---
st.set_page_config(
    page_title="Roteiro Califórnia",
    page_icon="🗺️",
    layout="wide"
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

# --- Dados do Roteiro (Com base na nova distribuição) ---
roteiro_data = {
    f"☀️ San Diego ({DIAS_SD} Dias)": {
        "icon": "☀️",
        "dias": get_dates(SD_START, DIAS_SD),
        "destaques": [
            ("🦁", "**San Diego Zoo & Balboa Park**",
             "Um dos melhores zoológicos do mundo. Combine com um museu no Balboa Park (Ciências ou História Natural)."),
            ("🌊", "**La Jolla Cove & Seals**",
             "Passeio gratuito para ver leões marinhos e focas descansando na costa. Ótimo para fotos."),
            ("⚓", "**USS Midway Museum**",
             "Explore o gigantesco porta-aviões. Excelente para os 9 e 12 anos, com acesso a aviões e ponte de comando."),
            ("🏖️", "**Coronado Beach**",
             "Visite a praia e o histórico Hotel del Coronado. Ótimo para um passeio relaxante e fotos.")
        ]
    },
    f"🌁 San Francisco & Bay Area ({DIAS_SF} Dias)": {
        "icon": "🌁",
        "dias": get_dates(SF_START, DIAS_SF),
        "destaques": [
            ("🔑", "**Alcatraz Island**",
             "O tour de áudio é excelente para todas as idades. **Reserve com 3-4 meses de antecedência!**"),
            ("🧪", "**Exploratorium**",
             "Museu de ciências altamente interativo no Pier 15. Absolutamente envolvente para 9 e 12 anos."),
            ("🚡", "**Cable Car, Golden Gate & Pier 39**",
             "Passeio de bonde, bike na Golden Gate e os leões marinhos do Pier 39 (Fisherman's Wharf)."),
            ("🌲", "**Muir Woods Redwoods**", "Dirija até lá para ver as majestosas Sequoias (Redwoods).")
        ]
    },
    f"🛣️ Highway 1 (2 Dias)": {
        "icon": "🛣️",
        "dias": get_dates(HW1_START, DIAS_VIAGEM),
        "destaques": [
            ("🐠", "**Monterey Bay Aquarium**", "Excelente parada no caminho para o sul, perfeita para a família."),
            ("🌉", "**Bixby Bridge (Big Sur)**", "A foto clássica da Highway 1 para registrar a Road Trip."),
            ("🐘", "**Elefantes Marinhos**", "Parada obrigatória em **Piedras Blancas** (San Simeon) para observação."),
            ("🏡", "**Carmel-by-the-Sea**", "Cidade charmosa e aconchegante para um almoço ou café.")
        ]
    },
    f"🎡 Anaheim, L.A. e Parques ({DIAS_ANAHEIM_LA} Dias)": {
        "icon": "🎬",
        "dias": get_dates(ANAHEIM_START, DIAS_ANAHEIM_LA),
        "destaques": [
            ("✨", "**Disneyland & California Adventure**",
             "Foco principal. Priorize Star Wars: Galaxy's Edge e Avengers Campus."),
            ("🧙", "**Universal Studios Hollywood**",
             "Prioridade: **Super Nintendo World** e **Harry Potter**, além do famoso Studio Tour."),
            ("🔭", "**Griffith Observatory**", "Vistas de L.A. e do Letreiro de Hollywood. Ótima parada noturna."),
            ("🎢", "**Santa Monica Pier**", "Píer icônico com roda gigante, jogos e o parque de diversões à beira-mar."),
            ("⭐", "**Hollywood Blvd**", "Calçada da Fama e TCL Chinese Theatre (rápido, mas obrigatório).")
        ]
    }
}


# --- Função Principal para Renderização ---
def main():
    st.title("🗺️ Guia de Viagem: Califórnia")
    st.markdown("### 🗓️ Período: 25 de Dezembro de 2025 a 17 de Janeiro de 2026 (24 Dias)")
    st.markdown("---")

    # Cria as abas com base nas chaves do dicionário
    tabs = st.tabs(list(roteiro_data.keys()))

    for i, (cidade, info) in enumerate(roteiro_data.items()):
        with tabs[i]:
            st.header(f"{info['icon']} {cidade}")
            st.subheader(f"Período: {info['dias']}")
            st.markdown("---")

            # Itera sobre os destaques e cria os cartões
            for emoji, titulo, descricao in info["destaques"]:
                with st.container(border=True):
                    st.markdown(f"### {emoji} {titulo}")
                    st.write(descricao)

            # Adiciona notas importantes para cada seção
            if "Highway 1" in cidade:
                st.warning(
                    "⚠️ **Logística:** Este é o trecho de transição (carro). Verifique as condições climáticas e estradas de montanha no inverno.")
            if "Anaheim" in cidade:
                st.info(
                    "💡 **Dica de Prioridade:** Com 10 dias, foque 4-5 dias nos parques temáticos (Disney/Universal) e use o restante para explorar a cultura e as praias de L.A.")


# --- Execução ---
if __name__ == "__main__":
    main()
