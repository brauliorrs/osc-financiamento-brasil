from pathlib import Path

import pandas as pd
import requests

from src.config import LEI_ROUANET_PROPONENTES_URL, RAW_DIR

BASE_DIR = RAW_DIR / "lei_rouanet"
BASE_DIR.mkdir(parents=True, exist_ok=True)



def baixar_arquivo(url: str, destino: Path) -> None:
    resp = requests.get(url, timeout=180)
    resp.raise_for_status()
    destino.write_bytes(resp.content)



def caminho_proponentes() -> Path:
    candidatos = [
        BASE_DIR / "proponentes.csv",
        RAW_DIR / "lei_rouanet_proponentes.csv",
    ]

    for caminho in candidatos:
        if caminho.exists():
            return caminho

    destino = BASE_DIR / "proponentes.csv"
    try:
        baixar_arquivo(LEI_ROUANET_PROPONENTES_URL, destino)
    except Exception as exc:
        raise FileNotFoundError(
            "Nao foi possivel localizar ou baixar a base de proponentes da Lei Rouanet. "
            "Salve o arquivo em data/raw/lei_rouanet/proponentes.csv ou verifique a URL oficial."
        ) from exc

    return destino



def carregar_lei_rouanet() -> pd.DataFrame:
    caminho = caminho_proponentes()

    try:
        return pd.read_csv(
            caminho,
            sep=",",
            encoding="utf-8",
            on_bad_lines="skip",
            low_memory=False,
        )
    except UnicodeDecodeError:
        return pd.read_csv(
            caminho,
            sep=",",
            encoding="latin1",
            on_bad_lines="skip",
            low_memory=False,
        )