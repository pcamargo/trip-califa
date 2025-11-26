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
             "Visite a praia e o histórico Hotel del Coronado. Ótimo para um passeio relaxante e fotos."),
            ("🏛️", "**Maritime Museum**", "Um museu marítimo com vários navios históricos e um submarino."),
            ("🤠", "**Old Town San Diego State Historic Park**", "Explore a história da cidade, com apresentações, mercados e arquitetura antiga."),
            ("💡", "**Gaslamp Quarter**", "Um bairro histórico com vida noturna animada, restaurantes e bares."),
            ("🎢", "**Belmont Park**", "Um parque de diversões histórico na praia Mission Beach com atrações como montanha-russa de madeira e simuladores de surf."),
            ("🧱", "**Legoland California**", "Um parque temático focado em blocos de montar, ótimo para crianças e para quem gosta de parques de diversões."),
            ("🐠", "**Birch Aquarium at Scripps**", "Um aquário com um túnel de observação subaquática onde se pode ver tubarões e raias nadando acima e ao redor."),
            ("🛍️", "**Compras no Outlet**", "Visite o outlet de San Diego para fazer compras em lojas com marcas famosas.")
        ]
    },
    f"🌁 San Francisco & Bay Area ({DIAS_SF} Dias)": {
        "icon": "🌁",
        "dias": get_dates(SF_START, DIAS_SF),
        "destaques": [
            ("🌉", "**Ponte Golden Gate**", "Atravesse a pé, de bicicleta ou de carro para vistas incríveis. Um ícone da cidade."),
            ("🔑", "**Ilha de Alcatraz**", "Faça um passeio de balsa para a antiga prisão. O tour de áudio é excelente. **Compre ingressos com 3-4 meses de antecedência!**"),
            ("🦁", "**Fisherman's Wharf & Pier 39**", "Veja os leões-marinhos, visite o curioso e gratuito Musée Mécanique (Pier 45) e experimente os pães da Boudin Bakery."),
            ("🚡", "**Passeio de Teleférico (Cable Car)**", "Uma forma clássica e divertida de se locomover e conhecer a cidade. Visite o Cable Car Museum para saber mais."),
            ("🔬", "**California Academy of Sciences**", "Um museu incrível com planetário, aquário, floresta tropical e um telhado verde."),
            ("🐠", "**Aquarium of the Bay**", "Localizado no Pier 39, é uma ótima opção para quem gosta de vida marinha."),
            ("🚶", "**Explore os Bairros**", "Caminhe por áreas icônicas como Chinatown, Little Italy e faça um free walking tour para conhecer a história local."),
            ("🌲", "**Muir Woods & Sausalito**", "Faça uma excursão para ver as sequoias gigantes e a charmosa cidade costeira de Sausalito."),
            ("🍷", "**Napa Valley**", "Se houver tempo, faça uma viagem de um dia para a famosa região vinícola para degustação de vinhos."),
            ("🎉", "**Festivais e Eventos**", "Verifique a programação da cidade. San Francisco sempre tem festivais e eventos ao ar livre acontecendo.")
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
            ("✨", "**Disneyland & California Adventure**", "O resort inclui os dois parques. Foco principal: Star Wars: Galaxy's Edge e Avengers Campus."),
            ("🧙", "**Universal Studios Hollywood**", "Prioridade: **Super Nintendo World** e **Harry Potter**, além do famoso Studio Tour."),
            ("🍓", "**Knott's Berry Farm**", "Considerado o primeiro parque temático dos EUA, com montanhas-russas emocionantes e atrações clássicas."),
            ("🎢", "**Six Flags Magic Mountain**", "Para os amantes de adrenalina, é o parque com o maior número de montanhas-russas do mundo."),
            ("🛍️", "**Downtown Disney**", "Área de compras, restaurantes e entretenimento anexa à Disney, com lojas como World of Disney."),
            ("🎡", "**Santa Monica Pier**", "Píer icônico com roda gigante, jogos e o parque de diversões à beira-mar."),
            ("🏖️", "**Praia de Balboa**", "A uma curta distância de Anaheim, possui um píer charmoso e atraente."),
            ("🔭", "**Griffith Observatory**", "Vistas incríveis de L.A. e do Letreiro de Hollywood. Ótima parada, especialmente ao entardecer."),
            ("⭐", "**Hollywood Blvd**", "Calçada da Fama e TCL Chinese Theatre (passeio rápido, mas obrigatório)."),
            ("🐠", "**Aquarium of the Pacific**", "Um grande aquário localizado em Long Beach, com foco na vida marinha do Pacífico."),
            ("⚓", "**Battleship USS Iowa Museum**", "Explore um navio de guerra histórico que serviu os EUA por décadas.")
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
