import pandas as pd


def integrar_cadastro_com_transferencias(
    cadastro: pd.DataFrame,
    transferencias: pd.DataFrame
) -> pd.DataFrame:
    cadastro = cadastro.copy()
    transferencias = transferencias.copy()

    # 1º critério: CNPJ
    if "cnpj" in cadastro.columns and "cnpj" in transferencias.columns:
        integrado = transferencias.merge(
            cadastro,
            on="cnpj",
            how="left",
            suffixes=("_transf", "")
        )
        return integrado

    # 2º critério: município + UF + nome
    chaves = [c for c in ["municipio", "uf", "nome_osc"] if c in cadastro.columns and c in transferencias.columns]
    if chaves:
        cadastro_ref = cadastro.drop_duplicates(subset=chaves)
        integrado = transferencias.merge(
            cadastro_ref,
            on=chaves,
            how="left",
            suffixes=("_transf", "")
        )
        return integrado

    return transferencias