from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

for d in [RAW_DIR, INTERIM_DIR, PROCESSED_DIR]:
    d.mkdir(parents=True, exist_ok=True)

MAPA_OSC_BASE_URL = "https://mapaosc.ipea.gov.br/download/20260310_MOSC_baseresumida.csv"
MAPA_OSC_DICIONARIO_URL = "https://mapaosc.ipea.gov.br/arquivos/subitems/4038-dicionario-de-dados-mapa-oscs.xlsx"