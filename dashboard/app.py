from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Financiamento publico das OSCs", layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED = BASE_DIR / "data" / "processed"
PUBLIC_DATA = Path(__file__).resolve().parent / "data"
REPO_URL = "https://github.com/brauliorrs/osc-financiamento-brasil"
DOI_URL = "https://doi.org/10.5281/zenodo.19103098"

ARQUIVOS_CANDIDATOS = [
    PROCESSED / "base_financiamento_publico_oscs.parquet",
    PROCESSED / "base_financiamento_publico_oscs_transferegov.parquet",
    PROCESSED / "pagamentos_transferegov_padronizados.parquet",
]
ARQ = next((arquivo for arquivo in ARQUIVOS_CANDIDATOS if arquivo.exists()), None)
DEMO_ARQ = PUBLIC_DATA / "painel_amostra_transferegov.parquet"


def coalescer_colunas(df: pd.DataFrame, destino: str, candidatos: list[str]) -> pd.DataFrame:
    if destino in df.columns:
        return df
    existentes = [col for col in candidatos if col in df.columns]
    if not existentes:
        return df
    serie = df[existentes[0]]
    for col in existentes[1:]:
        serie = serie.combine_first(df[col])
    df = df.copy()
    df[destino] = serie
    return df


def formatar_moeda(valor: float | int | None) -> str:
    if valor is None or pd.isna(valor):
        return "N/D"
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


@st.cache_data(show_spinner=False)
def carregar_base() -> tuple[pd.DataFrame | None, str]:
    if ARQ is not None:
        return pd.read_parquet(ARQ), ARQ.name
    if DEMO_ARQ.exists():
        return pd.read_parquet(DEMO_ARQ), DEMO_ARQ.name
    return None, ""


@st.cache_data(show_spinner=False)
def carregar_agregado(nome: str) -> pd.DataFrame | None:
    candidatos = [PROCESSED / nome, PUBLIC_DATA / nome]
    for caminho in candidatos:
        if caminho.exists():
            return pd.read_parquet(caminho)
    return None


st.title("Painel V2.1 - Financiamento publico direto das OSCs")

df, fonte = carregar_base()
if df is None:
    st.warning("Nao foi possivel localizar dados para o painel.")
    st.markdown("Repositorio: " + REPO_URL)
    st.markdown("DOI: " + DOI_URL)
    st.stop()

df = coalescer_colunas(df, "uf", ["uf", "uf_x", "uf_y"])
df = coalescer_colunas(df, "municipio", ["municipio", "municipio_x", "municipio_y"])

ufs = sorted(df["uf"].dropna().astype(str).unique().tolist()) if "uf" in df.columns else []
anos = sorted(df["ano"].dropna().astype(int).unique().tolist()) if "ano" in df.columns else []

st.sidebar.header("Filtros")
uf_sel = st.sidebar.multiselect("UF", ufs, default=ufs[:10] if len(ufs) > 10 else ufs)
ano_sel = st.sidebar.multiselect("Ano", anos, default=anos)
ranking_limite = st.sidebar.slider("Top municipios / OSCs", min_value=5, max_value=30, value=10, step=5)

df_f = df.copy()
if uf_sel and "uf" in df_f.columns:
    df_f = df_f[df_f["uf"].astype(str).isin(uf_sel)]
if ano_sel and "ano" in df_f.columns:
    df_f = df_f[df_f["ano"].isin(ano_sel)]

valor_total = df_f["valor_pago"].fillna(0).sum() if "valor_pago" in df_f.columns else None
osc_identificadas = df_f["nome_osc"].notna().sum() if "nome_osc" in df_f.columns else 0
osc_unicas = df_f["cnpj"].dropna().astype(str).nunique() if "cnpj" in df_f.columns else 0

if fonte == DEMO_ARQ.name:
    st.info("Esta versao publica utiliza uma amostra da base integrada e agregados consolidados para demonstracao do painel.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Registros na visualizacao", f"{len(df_f):,}".replace(",", "."))
col2.metric("Valor pago na amostra", formatar_moeda(valor_total))
col3.metric("Pagamentos com OSC identificada", f"{osc_identificadas:,}".replace(",", "."))
col4.metric("CNPJs unicos", f"{osc_unicas:,}".replace(",", "."))

por_uf = carregar_agregado("financiamento_publico_por_uf.parquet")
if por_uf is not None:
    if uf_sel and "uf" in por_uf.columns:
        por_uf = por_uf[por_uf["uf"].astype(str).isin(uf_sel)]
    fig_uf = px.bar(por_uf, x="uf", y="valor_pago", title="Valor pago por UF")
    st.plotly_chart(fig_uf, use_container_width=True)

if {"ano", "valor_pago"}.issubset(df_f.columns):
    por_ano = (
        df_f.groupby("ano", dropna=False)["valor_pago"]
        .sum(min_count=1)
        .reset_index()
        .sort_values("ano")
    )
    fig_ano = px.line(por_ano, x="ano", y="valor_pago", markers=True, title="Evolucao anual do valor pago")
    st.plotly_chart(fig_ano, use_container_width=True)

col_esq, col_dir = st.columns(2)
with col_esq:
    por_municipio = carregar_agregado("financiamento_publico_por_municipio.parquet")
    if por_municipio is not None:
        if uf_sel and "uf" in por_municipio.columns:
            por_municipio = por_municipio[por_municipio["uf"].astype(str).isin(uf_sel)]
        top_municipios = por_municipio.head(ranking_limite).copy()
        top_municipios["rotulo"] = top_municipios["municipio"].astype(str) + " / " + top_municipios["uf"].astype(str)
        fig_municipio = px.bar(top_municipios, x="valor_pago", y="rotulo", orientation="h", title=f"Top {ranking_limite} municipios por valor pago")
        fig_municipio.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_municipio, use_container_width=True)

with col_dir:
    por_area = carregar_agregado("financiamento_publico_por_area.parquet")
    if por_area is not None:
        por_area = por_area.copy()
        por_area["area"] = por_area["area"].astype(str).str.replace("area_", "", regex=False).str.replace("_", " ", regex=False).str.title()
        fig_area = px.bar(por_area, x="area", y="valor_pago", title="Valor pago por area tematica")
        st.plotly_chart(fig_area, use_container_width=True)

concentracao = carregar_agregado("concentracao_recursos_por_osc.parquet")
if concentracao is not None:
    if uf_sel and "uf" in concentracao.columns:
        concentracao = concentracao[concentracao["uf"].astype(str).isin(uf_sel)]
    top_concentracao = concentracao.head(ranking_limite)
    hover_cols = [c for c in ["nome_osc", "nome_convenente", "uf", "quantidade_pagamentos", "participacao_pct", "participacao_acumulada_pct"] if c in top_concentracao.columns]
    fig_concentracao = px.bar(top_concentracao, x="cnpj", y="valor_pago", title=f"Top {ranking_limite} OSCs/convenentes por valor pago", hover_data=hover_cols)
    fig_concentracao.update_layout(xaxis={"tickangle": -45})
    st.plotly_chart(fig_concentracao, use_container_width=True)

st.caption(f"Fonte carregada: {fonte}")
st.subheader("Amostra da base integrada")
st.dataframe(df_f.head(1000), use_container_width=True)