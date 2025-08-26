import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# =======================
# Configuração inicial
# =======================
st.set_page_config(page_title="Dashboard Profissional - Pedro Faim", layout="wide")

# Estilo global (CSS customizado)
st.markdown("""
    <style>
    /* Fundo e texto */
    .main {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stApp {
        background-color: #0E1117;
    }
    h1, h2, h3, h4, h5 {
        color: #00C896;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #00C896;
    }
    /* Caixas de estatísticas */
    .metric-card {
        background-color: #1F2937;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 0px 10px rgba(0,200,150,0.3);
    }
    .metric-value {
        font-size: 22px;
        font-weight: bold;
        color: #00C896;
    }
    .metric-label {
        font-size: 14px;
        color: #FAFAFA;
    }
    </style>
""", unsafe_allow_html=True)

# =======================
# Carregando Dataset de CSV
# =======================
@st.cache_data
def carregar_dados():
    caminho_base = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(caminho_base, "linguagens_popularidade.csv")
    df = pd.read_csv(caminho_arquivo)
    return df

df = carregar_dados()

# =======================
# Menu de navegação
# =======================
abas = ["Home", "Formação e Experiência", "Skills", "Análise de Dados"]
aba = st.sidebar.radio("📌 Navegação", abas)

# =======================
# HOME
# =======================
if aba == "Home":
    st.title("👨‍💻 Pedro Henrique Faim dos Santos")
    st.subheader("Estudante de Engenharia de Software | FIAP | 4º Semestre")
    st.write("Bem-vindo ao meu Dashboard Profissional! 🚀")
    st.info("**Objetivo:** Atuar como Estagiário em Desenvolvimento, contribuindo com projetos de software enquanto desenvolvo minhas habilidades técnicas e profissionais.")

# =======================
# FORMAÇÃO E EXPERIÊNCIA
# =======================
elif aba == "Formação e Experiência":
    st.header("🎓 Formação Acadêmica")
    st.write("- Engenharia de Software – FIAP (Cursando 4º semestre)")
    
    st.header("💼 Experiência Profissional")
    with st.container():
        st.subheader("Grupo Primova – Estagiário em Desenvolvimento (2024-2025)")
        st.write("- Desenvolvimento em **Java, Node.js, UI**")
        st.write("- Bancos de dados relacionais (**Oracle, MySQL**)")
        st.write("- Python (**Pandas, NumPy, Matplotlib, SciPy**)")
        st.write("- Contato com **React e Angular**")
    
    st.divider()
    with st.container():
        st.subheader("Exército Brasileiro (2023-2024)")
        st.write("- Gestão administrativa, planilhas e documentos")
        st.write("- Contato com **Python, SQL, HTML, CSS, JavaScript, C++, Arduino**")

# =======================
# SKILLS
# =======================
elif aba == "Skills":
    st.header("🛠️ Skills Técnicas")
    st.success("- Python (Pandas, NumPy, Matplotlib, SciPy)\n- Java, Node.js, React, Angular\n- SQL (Oracle, MySQL)\n- HTML, CSS, JavaScript\n- C++, Arduino")
    
    st.header("🤝 Soft Skills")
    st.info("- Proatividade, Organização, Relacionamento Interpessoal\n- Foco em resultados e aprendizado constante")
    
    st.header("🌍 Idiomas")
    st.warning("- Inglês Intermediário (Open English)")

# =======================
# ANÁLISE DE DADOS
# =======================
elif aba == "Análise de Dados":
    st.title("📊 Análise de Dados - Popularidade de Linguagens de Programação")
    st.write("O dataset apresenta a **popularidade de linguagens de programação (2020-2025)** baseada em índices de mercado como TIOBE e Stack Overflow Surveys.")

    # ---- 1. Visualização dos Dados
    st.subheader("1. Visualização dos Dados")
    st.dataframe(df.head())

    # ---- 2. Estatísticas Descritivas
    st.subheader("2. Estatísticas Descritivas")
    st.dataframe(df.describe())

    # ---- 3. Medidas Centrais (Cards Bonitos)
    st.subheader("3. Medidas Centrais (Ano mais recente - 2025)")
    df_2025 = df[df["Ano"] == 2025]
    media = df_2025["Popularidade (%)"].mean()
    mediana = df_2025["Popularidade (%)"].median()
    moda = df_2025["Popularidade (%)"].mode()[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{media:.2f}%</div><div class='metric-label'>Média</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{mediana:.2f}%</div><div class='metric-label'>Mediana</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{moda:.2f}%</div><div class='metric-label'>Moda</div></div>", unsafe_allow_html=True)

    # ---- 4. Dispersão
    st.subheader("4. Dispersão")
    variancia = df_2025["Popularidade (%)"].var()
    desvio = df_2025["Popularidade (%)"].std()
    st.write(f"**Variância:** {variancia:.2f} | **Desvio Padrão:** {desvio:.2f}")

    # ---- Distribuição
    st.subheader("Distribuição da Popularidade em 2025")
    st.write("Histograma e KDE mostram a distribuição da popularidade das linguagens, indicando concentração e variações extremas.")
    fig, ax = plt.subplots()
    sns.histplot(df_2025["Popularidade (%)"], kde=True, ax=ax, color="#00C896")
    ax.set_facecolor("#0E1117")
    st.pyplot(fig)

    # ---- Boxplot
    st.subheader("Boxplot da Popularidade em 2025")
    st.write("O boxplot evidencia outliers e a mediana das linguagens em 2025.")
    fig, ax = plt.subplots()
    sns.boxplot(y=df_2025["Popularidade (%)"], color="#00C896", ax=ax)
    ax.set_facecolor("#0E1117")
    st.pyplot(fig)

    # ---- 5. Evolução ao longo do tempo
    st.subheader("5. Evolução ao longo do tempo")
    st.write("Gráfico de linha mostrando a evolução da popularidade de cada linguagem de 2020 a 2025.")
    fig, ax = plt.subplots(figsize=(10,5))
    paleta = sns.color_palette("Set2", n_colors=len(df["Linguagem"].unique()))
    for i, lang in enumerate(df["Linguagem"].unique()):
        subset = df[df["Linguagem"] == lang]
        ax.plot(subset["Ano"], subset["Popularidade (%)"], marker="o", label=lang, color=paleta[i])
    ax.set_facecolor("#0E1117")
    plt.legend()
    plt.ylabel("Popularidade (%)")
    plt.xlabel("Ano")
    st.pyplot(fig)

    # ---- 6. Correlação entre linguagens
    st.subheader("6. Correlação entre linguagens")
    st.write("Heatmap mostrando como a popularidade das linguagens se correlaciona entre si.")
    df_pivot = df.pivot(index="Ano", columns="Linguagem", values="Popularidade (%)")
    corr = df_pivot.corr()
    st.dataframe(corr)
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    st.pyplot(fig)

    # ---- 7. Intervalo de Confiança
    st.subheader("7. Intervalo de Confiança (95%) - Popularidade em 2025")
    mean = np.mean(df_2025["Popularidade (%)"])
    sem = stats.sem(df_2025["Popularidade (%)"])
    ic = stats.t.interval(0.95, len(df_2025)-1, loc=mean, scale=sem)
    st.success(f"Média: {mean:.2f}% | IC 95%: {ic[0]:.2f}% até {ic[1]:.2f}%")

    # ---- 8. Teste de Hipótese
    st.subheader("8. Teste de Hipótese")
    st.write("Hipótese: **Python é significativamente mais popular que Java em 2025**")
    python_pop = df_2025[df_2025["Linguagem"] == "Python"]["Popularidade (%)"].values
    java_pop = df_2025[df_2025["Linguagem"] == "Java"]["Popularidade (%)"].values
    t_stat, p_value = stats.ttest_ind(python_pop, java_pop, equal_var=False)
    st.write(f"**t-statistic:** {t_stat:.4f} | **p-value:** {p_value:.4f}")
    if p_value < 0.05:
        st.success("✅ Resultado: Rejeitamos H0. Python é estatisticamente mais popular que Java.")
    else:
        st.error("❌ Resultado: Não há diferença estatística significativa entre Python e Java.")
