from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Financiamento publico das OSCs", layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED = BASE_DIR / "data" / "processed"

ARQUIVOS_CANDIDATOS = [
    PROCESSED / "base_financiamento_publico_oscs.parquet",
    PROCESSED / "base_financiamento_publico_oscs_transferegov.parquet",
    PROCESSED / "pagamentos_transferegov_padronizados.parquet",
]
ARQ = next((arquivo for arquivo in ARQUIVOS_CANDIDATOS if arquivo.exists()), None)



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


st.title("Painel V2.1 - Financiamento publico direto das OSCs")

if ARQ is None:
    st.warning("Rode antes: python -m src.pipeline")
    st.stop()

df = pd.read_parquet(ARQ)
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

col1, col2, col3, col4 = st.columns(4)
col1.metric("Registros", f"{len(df_f):,}".replace(",", "."))
col2.metric("Valor pago total", formatar_moeda(valor_total))
col3.metric("Pagamentos com OSC identificada", f"{osc_identificadas:,}".replace(",", "."))
col4.metric("CNPJs unicos", f"{osc_unicas:,}".replace(",", "."))

if {"uf", "valor_pago"}.issubset(df_f.columns):
    por_uf = (
        df_f.groupby("uf", dropna=False)["valor_pago"]
        .sum(min_count=1)
        .reset_index()
        .sort_values("valor_pago", ascending=False)
    )
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
    if {"municipio", "uf", "valor_pago"}.issubset(df_f.columns):
        top_municipios = (
            df_f.groupby(["municipio", "uf"], dropna=False)["valor_pago"]
            .sum(min_count=1)
            .reset_index()
            .sort_values("valor_pago", ascending=False)
            .head(ranking_limite)
        )
        top_municipios["rotulo"] = top_municipios["municipio"].astype(str) + " / " + top_municipios["uf"].astype(str)
        fig_municipio = px.bar(
            top_municipios,
            x="valor_pago",
            y="rotulo",
            orientation="h",
            title=f"Top {ranking_limite} municipios por valor pago",
        )
        fig_municipio.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_municipio, use_container_width=True)

with col_dir:
    area_cols = [c for c in df_f.columns if c.startswith("area_")]
    if area_cols and "valor_pago" in df_f.columns:
        registros_area = []
        for col in area_cols:
            marcador = pd.to_numeric(df_f[col], errors="coerce").fillna(0)
            registros_area.append(
                {
                    "area": col.replace("area_", "").replace("_", " ").title(),
                    "valor_pago": df_f.loc[marcador > 0, "valor_pago"].sum(min_count=1),
                }
            )
        por_area = pd.DataFrame(registros_area).sort_values("valor_pago", ascending=False)
        fig_area = px.bar(por_area, x="area", y="valor_pago", title="Valor pago por area tematica")
        st.plotly_chart(fig_area, use_container_width=True)

if {"cnpj", "valor_pago"}.issubset(df_f.columns):
    chaves = [c for c in ["cnpj", "nome_osc", "nome_convenente", "uf"] if c in df_f.columns]
    concentracao = (
        df_f.groupby(chaves, dropna=False)["valor_pago"]
        .agg(["sum", "size"])
        .reset_index()
        .rename(columns={"sum": "valor_pago", "size": "quantidade_pagamentos"})
        .sort_values("valor_pago", ascending=False)
        .head(ranking_limite)
        .reset_index(drop=True)
    )
    total_concentracao = concentracao["valor_pago"].sum()
    if pd.notna(total_concentracao) and total_concentracao != 0:
        concentracao["participacao_pct"] = concentracao["valor_pago"] / total_concentracao * 100
    else:
        concentracao["participacao_pct"] = 0.0

    fig_concentracao = px.bar(
        concentracao,
        x="valor_pago",
        y="cnpj",
        orientation="h",
        title=f"Top {ranking_limite} OSCs/convenentes por valor pago",
        hover_data=[c for c in ["nome_osc", "nome_convenente", "uf", "quantidade_pagamentos", "participacao_pct"] if c in concentracao.columns],
    )
    fig_concentracao.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_concentracao, use_container_width=True)

st.caption(f"Fonte carregada: {ARQ.name}")
st.subheader("Amostra da base integrada")
st.dataframe(df_f.head(1000), use_container_width=True)