import pandas as pd


def integrar_rouanet_com_osc(rouanet: pd.DataFrame, osc: pd.DataFrame) -> pd.DataFrame:
    rouanet = rouanet.copy()
    osc = osc.copy()

    for col in ["uf", "municipio"]:
        if col in rouanet.columns:
            rouanet[col] = rouanet[col].astype(str).str.strip().str.upper()
        if col in osc.columns:
            osc[col] = osc[col].astype(str).str.strip().str.upper()

    chaves = [c for c in ["uf", "municipio"] if c in rouanet.columns and c in osc.columns]

    if not chaves:
        return rouanet

    osc_ref = osc[chaves + [c for c in ["id_osc", "nome_osc", "area_tematica"] if c in osc.columns]].drop_duplicates()

    integrado = rouanet.merge(
        osc_ref,
        on=chaves,
        how="left",
        suffixes=("", "_osc")
    )
    return integrado