from pathlib import Path
import pandas as pd

from src.config import RAW_DIR


def localizar_arquivo_transferencias() -> Path:
    candidatos = [
        RAW_DIR / "transferencias_federais_oscs.csv",
        RAW_DIR / "transferencias_federais_oscs.xlsx",
        RAW_DIR / "transferencias_publicas_oscs.csv",
        RAW_DIR / "transferencias_publicas_oscs.xlsx",
    ]

    for caminho in candidatos:
        if caminho.exists():
            return caminho

    raise FileNotFoundError(
        "Arquivo de transferências não encontrado em data/raw/. "
        "Salve ali um CSV/XLSX exportado do Mapa das OSCs, por exemplo: "
        "'transferencias_federais_oscs.xlsx'"
    )


def carregar_transferencias_publicas() -> pd.DataFrame:
    caminho = localizar_arquivo_transferencias()

    if caminho.suffix.lower() == ".csv":
        try:
            return pd.read_csv(caminho, sep=";", encoding="latin1", engine="python", on_bad_lines="skip")
        except Exception:
            return pd.read_csv(caminho, sep=",", encoding="latin1", engine="python", on_bad_lines="skip")

    if caminho.suffix.lower() == ".xlsx":
        return pd.read_excel(caminho)

    raise ValueError(f"Formato não suportado: {caminho.suffix}")