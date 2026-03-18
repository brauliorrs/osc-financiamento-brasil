from pathlib import Path
from zipfile import ZipFile

import pandas as pd

from src.config import RAW_DIR

BASE_DIR = RAW_DIR / "transferegov"
ZIP_CANDIDATOS = [
    BASE_DIR / "siconv.zip",
    RAW_DIR / "siconv.zip",
    Path(r"D:\siconv.zip"),
]


def caminho_pagamentos() -> Path:
    candidatos = [
        BASE_DIR / "siconv_pagamentos.csv",
        BASE_DIR / "siconv_pagamento.csv",
    ]

    for arq in candidatos:
        if arq.exists():
            return arq

    raise FileNotFoundError(
        f"Arquivo nao encontrado em {BASE_DIR}. "
        "Coloque o CSV extraido do zip nessa pasta."
    )


def caminho_zip_siconv() -> Path | None:
    for caminho in ZIP_CANDIDATOS:
        if caminho.exists():
            return caminho
    return None


def normalizar_nome_siconv(coluna: str) -> str:
    return str(coluna).replace("\ufeff", "").replace("ï»¿", "").strip().lower()


def _resolver_usecols(colunas_originais: list[str], usecols: list[str] | None) -> list[str] | None:
    if usecols is None:
        return None

    mapa = {normalizar_nome_siconv(col): col for col in colunas_originais}
    usecols_resolvidas = []
    for col in usecols:
        chave = normalizar_nome_siconv(col)
        if chave not in mapa:
            raise ValueError(f"Coluna esperada nao encontrada: {col}")
        usecols_resolvidas.append(mapa[chave])
    return usecols_resolvidas


def ler_csv_siconv(nome_arquivo: str, usecols: list[str] | None = None) -> pd.DataFrame:
    caminho_extraido = BASE_DIR / nome_arquivo
    if caminho_extraido.exists():
        header = pd.read_csv(caminho_extraido, sep=";", encoding="latin1", nrows=0, low_memory=False)
        usecols_resolvidas = _resolver_usecols(list(header.columns), usecols)
        return pd.read_csv(
            caminho_extraido,
            sep=";",
            encoding="latin1",
            usecols=usecols_resolvidas,
            low_memory=False,
        )

    caminho_zip = caminho_zip_siconv()
    if caminho_zip is None:
        raise FileNotFoundError(
            f"Arquivo {nome_arquivo} nao encontrado em {BASE_DIR} e nenhum siconv.zip foi localizado."
        )

    with ZipFile(caminho_zip) as zip_file:
        with zip_file.open(nome_arquivo) as arquivo_header:
            header = pd.read_csv(arquivo_header, sep=";", encoding="latin1", nrows=0, low_memory=False)
        usecols_resolvidas = _resolver_usecols(list(header.columns), usecols)
        with zip_file.open(nome_arquivo) as arquivo_zip:
            return pd.read_csv(
                arquivo_zip,
                sep=";",
                encoding="latin1",
                usecols=usecols_resolvidas,
                low_memory=False,
            )


def carregar_colunas_pagamentos(nrows: int = 5) -> pd.DataFrame:
    arq = caminho_pagamentos()
    return pd.read_csv(
        arq,
        sep=";",
        encoding="latin1",
        nrows=nrows,
        low_memory=False,
    )


def carregar_mapa_convenente() -> pd.DataFrame:
    convenio = ler_csv_siconv("siconv_convenio.csv", usecols=["NR_CONVENIO", "ID_PROPOSTA"])
    proposta = ler_csv_siconv(
        "siconv_proposta.csv",
        usecols=["ID_PROPOSTA", "IDENTIF_PROPONENTE", "NM_PROPONENTE", "UF_PROPONENTE", "MUNIC_PROPONENTE"],
    )

    convenio.columns = [normalizar_nome_siconv(col) for col in convenio.columns]
    proposta.columns = [normalizar_nome_siconv(col) for col in proposta.columns]

    mapa = convenio.merge(proposta, on="id_proposta", how="left")
    mapa = mapa.rename(
        columns={
            "nr_convenio": "numero_convenio",
            "identif_proponente": "cnpj",
            "nm_proponente": "nome_convenente",
            "uf_proponente": "uf",
            "munic_proponente": "municipio",
        }
    )

    mapa["numero_convenio"] = mapa["numero_convenio"].astype(str).str.strip()
    mapa["cnpj"] = mapa["cnpj"].astype(str).str.replace(r"\D", "", regex=True).str.zfill(14)
    mapa["uf"] = mapa["uf"].astype(str).str.upper().str.strip()
    mapa["municipio"] = mapa["municipio"].astype(str).str.strip()

    return mapa[["numero_convenio", "cnpj", "nome_convenente", "uf", "municipio"]].drop_duplicates()


def carregar_pagamentos() -> pd.DataFrame:
    arq = caminho_pagamentos()
    header = pd.read_csv(arq, sep=";", encoding="latin1", nrows=0, low_memory=False)
    colunas_originais = list(header.columns)
    mapa_colunas = {normalizar_nome_siconv(col): col for col in colunas_originais}

    candidatos = [
        ["nr_cnpj_convenente", "vl_pago", "dt_pagamento", "id_convenio"],
        ["cnpj_convenente", "vl_pago", "dt_pagamento", "id_convenio"],
        ["nr_cnpj_convenente", "vl_pagamento", "dt_pagamento", "id_convenio"],
        ["cnpj_convenente", "vl_pagamento", "dt_pagamento", "id_convenio"],
        ["nr_convenio", "identif_fornecedor", "nome_fornecedor", "data_pag", "vl_pago"],
        ["nr_convenio", "identif_fornecedor", "nome_fornecedor", "data_pag", "vl_pagamento"],
    ]

    usecols = None
    for grupo in candidatos:
        if all(c in mapa_colunas for c in grupo):
            usecols = [mapa_colunas[c] for c in grupo]
            break

    if usecols is None:
        df = pd.read_csv(arq, sep=";", encoding="latin1", low_memory=False)
    else:
        df = pd.read_csv(
            arq,
            sep=";",
            encoding="latin1",
            usecols=usecols,
            low_memory=False,
        )

    df.columns = [normalizar_nome_siconv(col) for col in df.columns]
    rename_map = {
        "nr_cnpj_convenente": "cnpj",
        "cnpj_convenente": "cnpj",
        "vl_pago": "valor_pago",
        "vl_pagamento": "valor_pago",
        "dt_pagamento": "data_pagamento",
        "data_pag": "data_pagamento",
        "nr_convenio": "numero_convenio",
        "id_convenio": "numero_convenio",
        "identif_fornecedor": "identificador_favorecido",
        "nome_fornecedor": "nome_favorecido",
    }
    df = df.rename(columns=rename_map)

    if "numero_convenio" in df.columns:
        df["numero_convenio"] = df["numero_convenio"].astype(str).str.strip()

    if "cnpj" not in df.columns and "numero_convenio" in df.columns:
        mapa_convenente = carregar_mapa_convenente()
        df = df.merge(mapa_convenente, on="numero_convenio", how="left")

    if "cnpj" in df.columns:
        df["cnpj"] = (
            df["cnpj"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .str.zfill(14)
        )

    if "identificador_favorecido" in df.columns:
        df["identificador_favorecido"] = (
            df["identificador_favorecido"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .str.strip()
        )

    if "valor_pago" in df.columns:
        df["valor_pago"] = (
            df["valor_pago"]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        df["valor_pago"] = pd.to_numeric(df["valor_pago"], errors="coerce")

    if "data_pagamento" in df.columns:
        df["data_pagamento"] = pd.to_datetime(df["data_pagamento"], dayfirst=True, errors="coerce")
        df["ano"] = df["data_pagamento"].dt.year

    return df


