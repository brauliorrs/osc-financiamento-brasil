from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Estrutura das OSCs no Brasil", layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED = BASE_DIR / "data" / "processed"

CADASTRO = PROCESSED / "cadastro_mestre_oscs.parquet"

st.title("Painel inicial — Cadastro mestre das OSCs")

if not CADASTRO.exists():
    st.warning("Rode antes: python -m src.pipeline")
    st.stop()

df = pd.read_parquet(CADASTRO)

ufs = sorted(df["uf"].dropna().astype(str).unique().tolist()) if "uf" in df.columns else []
uf_sel = st.sidebar.multiselect("UF", ufs, default=ufs[:10] if len(ufs) > 10 else ufs)

if uf_sel and "uf" in df.columns:
    df_f = df[df["uf"].astype(str).isin(uf_sel)].copy()
else:
    df_f = df.copy()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de OSCs", f"{len(df_f):,}".replace(",", "."))
col2.metric("UFs no recorte", df_f["uf"].nunique() if "uf" in df_f.columns else 0)
col3.metric("Municípios no recorte", df_f["municipio"].nunique() if "municipio" in df_f.columns else 0)
col4.metric("Naturezas jurídicas", df_f["natureza_juridica"].nunique() if "natureza_juridica" in df_f.columns else 0)

if "uf" in df_f.columns:
    por_uf = (
        df_f.groupby("uf", dropna=False)
        .size()
        .reset_index(name="total_oscs")
        .sort_values("total_oscs", ascending=False)
    )
    fig_uf = px.bar(por_uf, x="uf", y="total_oscs", title="OSCs por UF")
    st.plotly_chart(fig_uf, use_container_width=True)

if "situacao_cadastral" in df_f.columns:
    por_situacao = (
        df_f.groupby("situacao_cadastral", dropna=False)
        .size()
        .reset_index(name="total_oscs")
        .sort_values("total_oscs", ascending=False)
    )
    fig_sit = px.bar(
        por_situacao,
        x="situacao_cadastral",
        y="total_oscs",
        title="OSCs por situação cadastral"
    )
    st.plotly_chart(fig_sit, use_container_width=True)

area_cols = [c for c in df_f.columns if c.startswith("area_")]
if area_cols:
    totais_area = df_f[area_cols].fillna(0).sum().reset_index()
    totais_area.columns = ["area", "total_oscs"]
    totais_area = totais_area.sort_values("total_oscs", ascending=False)

    fig_area = px.bar(
        totais_area,
        x="area",
        y="total_oscs",
        title="OSCs por área temática"
    )
    st.plotly_chart(fig_area, use_container_width=True)

if "natureza_juridica" in df_f.columns:
    por_natureza = (
        df_f.groupby("natureza_juridica", dropna=False)
        .size()
        .reset_index(name="total_oscs")
        .sort_values("total_oscs", ascending=False)
        .head(15)
    )
    fig_nat = px.bar(
        por_natureza,
        x="natureza_juridica",
        y="total_oscs",
        title="Top 15 naturezas jurídicas"
    )
    st.plotly_chart(fig_nat, use_container_width=True)

if "matriz_filial" in df_f.columns:
    por_matriz = (
        df_f.groupby("matriz_filial", dropna=False)
        .size()
        .reset_index(name="total_oscs")
        .sort_values("total_oscs", ascending=False)
    )
    fig_matriz = px.bar(
        por_matriz,
        x="matriz_filial",
        y="total_oscs",
        title="OSCs por matriz/filial"
    )
    st.plotly_chart(fig_matriz, use_container_width=True)

st.subheader("Amostra do cadastro mestre")
st.dataframe(df_f.head(1000), use_container_width=True)