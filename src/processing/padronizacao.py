import pandas as pd


def normalizar_nome_coluna(col: str) -> str:
    col = str(col).strip().lower()
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
        "ã": "a",
        "á": "a",
        "à": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "ç": "c",
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


def padronizar_mapa_osc(df: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df)

    candidatos = {
        "cnpj": ["cnpj"],
        "nome_osc": ["tx_razao_social_osc", "razao_social", "nome_osc"],
        "nome_fantasia": ["tx_nome_fantasia_osc", "nome_fantasia"],
        "natureza_juridica": ["natureza_juridica"],
        "matriz_filial": ["matriz_filial"],
        "situacao_cadastral": ["situacao_cadastral"],
        "data_abertura": ["dt_fundacao_osc", "data_abertura"],
        "removida_do_mosc": ["removida_do_mosc"],
        "data_fechamento": ["data_fechamento"],
        "ano_fechamento": ["ano_fechamento"],
        "endereco_completo": ["tx_endereco_completo"],
        "codigo_municipio": ["cd_municipio"],
        "municipio": ["municipio_nome", "municipio"],
        "uf": ["uf_sigla", "uf"],
        "longitude": ["longitude"],
        "latitude": ["latitude"],
        "cnae_principal": ["cnae"],
        "cnae_secundaria": ["cnae_secundaria"],
    }

    base = pd.DataFrame(index=df.index)

    for destino, opcoes in candidatos.items():
        col = escolher_coluna(df, opcoes)
        if col:
            base[destino] = df[col]

    # Áreas temáticas
    area_cols = [c for c in df.columns if c.startswith("area_")]
    subarea_cols = [c for c in df.columns if c.startswith("subarea_")]

    for c in area_cols:
        base[c] = df[c]

    for c in subarea_cols:
        base[c] = df[c]

    if "uf" in base.columns:
        base["uf"] = base["uf"].astype(str).str.upper().str.strip()

    if "municipio" in base.columns:
        base["municipio"] = base["municipio"].astype(str).str.strip()

    if "cnpj" in base.columns:
        base["cnpj"] = (
            base["cnpj"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .str.zfill(14)
        )

    if "codigo_municipio" in base.columns:
        base["codigo_municipio"] = (
            base["codigo_municipio"]
            .astype(str)
            .str.replace(r"\.0$", "", regex=True)
            .str.strip()
        )

    return base