import pandas as pd


def gerar_indicadores_basicos(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    saidas = {}

    if "uf" in df.columns:
        saidas["oscs_por_uf"] = (
            df.groupby("uf", dropna=False)
            .size()
            .reset_index(name="total_oscs")
            .sort_values("total_oscs", ascending=False)
        )

    if {"uf", "municipio"}.issubset(df.columns):
        saidas["oscs_por_municipio"] = (
            df.groupby(["uf", "municipio"], dropna=False)
            .size()
            .reset_index(name="total_oscs")
            .sort_values("total_oscs", ascending=False)
        )

    if "situacao_cadastral" in df.columns:
        saidas["oscs_por_situacao"] = (
            df.groupby("situacao_cadastral", dropna=False)
            .size()
            .reset_index(name="total_oscs")
            .sort_values("total_oscs", ascending=False)
        )

    if "natureza_juridica" in df.columns:
        saidas["oscs_por_natureza_juridica"] = (
            df.groupby("natureza_juridica", dropna=False)
            .size()
            .reset_index(name="total_oscs")
            .sort_values("total_oscs", ascending=False)
        )

    if "matriz_filial" in df.columns:
        saidas["oscs_por_matriz_filial"] = (
            df.groupby("matriz_filial", dropna=False)
            .size()
            .reset_index(name="total_oscs")
            .sort_values("total_oscs", ascending=False)
        )

    # Indicadores por áreas temáticas
    area_cols = [c for c in df.columns if c.startswith("area_")]
    if area_cols:
        totais_area = df[area_cols].fillna(0).sum().reset_index()
        totais_area.columns = ["area", "total_oscs"]
        totais_area = totais_area.sort_values("total_oscs", ascending=False)
        saidas["oscs_por_area"] = totais_area

    subarea_cols = [c for c in df.columns if c.startswith("subarea_")]
    if subarea_cols:
        totais_subarea = df[subarea_cols].fillna(0).sum().reset_index()
        totais_subarea.columns = ["subarea", "total_oscs"]
        totais_subarea = totais_subarea.sort_values("total_oscs", ascending=False)
        saidas["oscs_por_subarea"] = totais_subarea

    return saidas