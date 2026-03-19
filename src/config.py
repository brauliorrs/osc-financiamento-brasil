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
LEI_ROUANET_PROPONENTES_URL = "https://dados.cultura.gov.br/dataset/eab2b6a9-6afa-4b33-affa-96ee5b0981a4/resource/59fb244d-79b2-4c69-9bea-df8b3c7f5c30/download/proponentes.csv"