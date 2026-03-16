from pathlib import Path
import requests
import pandas as pd

from src.config import RAW_DIR, MAPA_OSC_BASE_URL, MAPA_OSC_DICIONARIO_URL


def baixar_arquivo(url: str, destino: Path) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.exists():
        return

    print(f"Baixando: {url}")
    with requests.get(url, timeout=300, stream=True) as resp:
        resp.raise_for_status()
        with open(destino, "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)


def garantir_downloads() -> tuple[Path, Path]:
    base_path = RAW_DIR / "mapa_osc_base.csv"
    dict_path = RAW_DIR / "mapa_osc_dicionario.xlsx"

    baixar_arquivo(MAPA_OSC_BASE_URL, base_path)
    baixar_arquivo(MAPA_OSC_DICIONARIO_URL, dict_path)

    return base_path, dict_path


def carregar_base_mapa_osc() -> pd.DataFrame:
    base_path, _ = garantir_downloads()

    print("Lendo base do Mapa das OSCs...")

    # leitura robusta para CSV grande do governo
    df = pd.read_csv(
        base_path,
        sep=";",
        encoding="latin1",
        engine="python",
        on_bad_lines="skip"
    )

    print("Leitura concluída.")
    return df