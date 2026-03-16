from pathlib import Path
import pandas as pd
import requests

from src.config import RAW_DIR, LEI_ROUANET_URL


def baixar_arquivo(url: str, destino: Path) -> None:
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    destino.write_bytes(resp.content)


def carregar_lei_rouanet() -> pd.DataFrame:
    destino = RAW_DIR / "lei_rouanet.csv"

    if not destino.exists():
        if "COLE_AQUI" in LEI_ROUANET_URL:
            raise ValueError("Defina LEI_ROUANET_URL em src/config.py")
        baixar_arquivo(LEI_ROUANET_URL, destino)

    try:
        df = pd.read_csv(destino, sep=None, engine="python", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(destino, sep=None, engine="python", encoding="latin1")

    return df