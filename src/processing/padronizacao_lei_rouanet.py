import pandas as pd

from src.analytics.indicadores import preparar_base_financiamento
from src.processing.padronizacao_transferencias import normalizar_colunas, escolher_coluna



def padronizar_lei_rouanet(df: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df)

    candidatos = {
        "cnpj": ["cgccpf", "cnpj", "cpf_cnpj", "documento"],
        "nome_convenente": ["nome", "proponente", "nome_proponente"],
        "tipo_pessoa": ["tipo_pessoa"],
        "responsavel": ["responsavel"],
        "uf": ["uf", "uf_proponente"],
        "municipio": ["municipio", "municipio_proponente"],
        "valor_captado": ["total_captado", "valor_captado", "captado"],
    }

    base = pd.DataFrame(index=df.index)
    for destino, opcoes in candidatos.items():
        col = escolher_coluna(df, opcoes)
        if col:
            base[destino] = df[col]

    if "cnpj" in base.columns:
        base["cnpj"] = (
            base["cnpj"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .str.zfill(14)
        )

    if "uf" in base.columns:
        base["uf"] = base["uf"].astype(str).str.upper().str.strip()

    if "municipio" in base.columns:
        base["municipio"] = base["municipio"].astype(str).str.strip()

    if "valor_captado" in base.columns:
        base["valor_captado"] = pd.to_numeric(base["valor_captado"], errors="coerce")

    return base



def gerar_indicadores_lei_rouanet(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    base = preparar_base_financiamento(df)
    saidas = {}

    if "valor_captado" not in base.columns:
        return saidas

    if "uf" in base.columns:
        saidas["lei_rouanet_captado_por_uf"] = (
            base.groupby("uf", dropna=False)["valor_captado"]
            .sum(min_count=1)
            .reset_index()
            .sort_values("valor_captado", ascending=False)
        )

    if {"uf", "municipio"}.issubset(base.columns):
        saidas["lei_rouanet_captado_por_municipio"] = (
            base.groupby(["uf", "municipio"], dropna=False)["valor_captado"]
            .sum(min_count=1)
            .reset_index()
            .sort_values("valor_captado", ascending=False)
        )

    if "cnpj" in base.columns:
        chaves = [c for c in ["cnpj", "nome_osc", "nome_convenente", "uf"] if c in base.columns]
        saidas["lei_rouanet_concentracao_por_osc"] = (
            base.groupby(chaves, dropna=False)["valor_captado"]
            .sum(min_count=1)
            .reset_index()
            .sort_values("valor_captado", ascending=False)
        )

    return saidas