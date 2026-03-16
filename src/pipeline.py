import pandas as pd

from src.config import PROCESSED_DIR
from src.ingestion.mapa_osc import carregar_base_mapa_osc
from src.processing.padronizacao import padronizar_mapa_osc
from src.analytics.indicadores import gerar_indicadores_basicos


def salvar_csv_parquet(df: pd.DataFrame, nome: str) -> None:
    csv_path = PROCESSED_DIR / f"{nome}.csv"
    parquet_path = PROCESSED_DIR / f"{nome}.parquet"

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    df.to_parquet(parquet_path, index=False)


def main() -> None:
    print("1. Carregando Base Principal do Mapa das OSCs...")
    bruto = carregar_base_mapa_osc()

    print(f"Registros brutos: {len(bruto):,}")
    print(f"Colunas brutas: {len(bruto.columns)}")

    print("2. Padronizando cadastro mestre...")
    cadastro = padronizar_mapa_osc(bruto)

    print(f"Registros padronizados: {len(cadastro):,}")
    print(f"Colunas padronizadas: {len(cadastro.columns)}")

    print("3. Salvando cadastro mestre...")
    salvar_csv_parquet(cadastro, "cadastro_mestre_oscs")

    print("4. Gerando indicadores básicos...")
    indicadores = gerar_indicadores_basicos(cadastro)

    for nome, df in indicadores.items():
        salvar_csv_parquet(df, nome)

    print("Pipeline concluído com sucesso.")
    print(f"Saídas em: {PROCESSED_DIR}")


if __name__ == "__main__":
    main()