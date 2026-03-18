import unicodedata

import pandas as pd


def normalizar_nome_coluna(col: str) -> str:
    col = str(col).strip().lower()
    col = unicodedata.normalize("NFKD", col).encode("ascii", "ignore").decode("ascii")
    substituicoes = {
        " ": "_",
        "/": "_",
        "-": "_",
        ".": "",
        "(": "",
        ")": "",
        "[": "",
        "]": "",
        "{": "",
        "}": "",
        "%": "pct",
    }
    for k, v in substituicoes.items():
        col = col.replace(k, v)

    while "__" in col:
        col = col.replace("__", "_")

    return col.strip("_")


def normalizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [normalizar_nome_coluna(c) for c in df.columns]
    return df


def escolher_coluna(df: pd.DataFrame, opcoes: list[str]) -> str | None:
    for opcao in opcoes:
        if opcao in df.columns:
            return opcao
    return None


def padronizar_transferencias_publicas(df: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df)

    candidatos = {
        "cnpj": ["cnpj", "cnpj_osc", "nr_cnpj"],
        "nome_osc": ["nome_osc", "razao_social", "tx_razao_social_osc", "favorecido"],
        "codigo_municipio": ["cd_municipio", "codigo_municipio", "ibge"],
        "municipio": ["municipio", "municipio_nome", "nome_municipio"],
        "uf": ["uf", "uf_sigla", "sg_uf"],
        "ano": ["ano", "ano_referencia", "exercicio"],
        "valor_empenhado": ["valor_empenhado", "vl_empenhado", "empenhado"],
        "valor_pago": ["valor_pago", "vl_pago", "pago"],
        "funcao": ["funcao"],
        "subfuncao": ["subfuncao"],
        "orgao": ["orgao", "orgao_concedente"],
        "instrumento": ["instrumento", "tipo_instrumento"],
    }

    base = pd.DataFrame(index=df.index)

    for destino, opcoes in candidatos.items():
        col = escolher_coluna(df, opcoes)
        if col:
            base[destino] = df[col]

    if "cnpj" in base.columns:
        base["cnpj"] = (
            base["cnpj"].astype(str).str.replace(r"\D", "", regex=True).str.zfill(14)
        )

    if "codigo_municipio" in base.columns:
        base["codigo_municipio"] = (
            base["codigo_municipio"].astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
        )

    if "uf" in base.columns:
        base["uf"] = base["uf"].astype(str).str.upper().str.strip()

    if "municipio" in base.columns:
        base["municipio"] = base["municipio"].astype(str).str.strip()

    for col in ["valor_empenhado", "valor_pago"]:
        if col in base.columns:
            base[col] = (
                base[col]
                .astype(str)
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
            )
            base[col] = pd.to_numeric(base[col], errors="coerce")

    if "ano" in base.columns:
        base["ano"] = pd.to_numeric(base["ano"], errors="coerce")

    return base