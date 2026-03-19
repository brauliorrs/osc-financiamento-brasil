import pandas as pd

from src.analytics.indicadores import gerar_indicadores_basicos, gerar_indicadores_financiamento
from src.config import PROCESSED_DIR
from src.ingestion.lei_rouanet import carregar_lei_rouanet
from src.ingestion.mapa_osc import carregar_base_mapa_osc
from src.ingestion.transferegov import carregar_pagamentos
from src.ingestion.transferencias_publicas import carregar_transferencias_publicas
from src.integration.integrar_transferencias import integrar_cadastro_com_transferencias
from src.processing.padronizacao import padronizar_mapa_osc
from src.processing.padronizacao_lei_rouanet import padronizar_lei_rouanet, gerar_indicadores_lei_rouanet
from src.processing.padronizacao_transferencias import padronizar_transferencias_publicas


def salvar_csv_parquet(df: pd.DataFrame, nome: str) -> None:
    csv_path = PROCESSED_DIR / f"{nome}.csv"
    parquet_path = PROCESSED_DIR / f"{nome}.parquet"

    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    df.to_parquet(parquet_path, index=False)


def selecionar_colunas_cadastro_para_merge(cadastro: pd.DataFrame) -> pd.DataFrame:
    colunas_prioritarias = [
        "cnpj",
        "nome_osc",
        "uf",
        "municipio",
        "codigo_municipio",
        "natureza_juridica",
        "situacao_cadastral",
        "matriz_filial",
    ]
    colunas_area = [c for c in cadastro.columns if c.startswith("area_")]
    colunas = [c for c in colunas_prioritarias if c in cadastro.columns]
    colunas.extend(colunas_area)

    cadastro_merge = cadastro[colunas].copy()
    if "cnpj" in cadastro_merge.columns:
        cadastro_merge = cadastro_merge.drop_duplicates(subset=["cnpj"])
    return cadastro_merge


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

    print("4. Gerando indicadores basicos do cadastro...")
    indicadores = gerar_indicadores_basicos(cadastro)
    for nome, df in indicadores.items():
        salvar_csv_parquet(df, nome)

    transf = None
    print("5. Carregando transferencias publicas...")
    try:
        transf_raw = carregar_transferencias_publicas()
    except FileNotFoundError as exc:
        print(f"5. Fonte opcional ausente: {exc}")
    else:
        print(f"Registros de transferencias: {len(transf_raw):,}")
        print(f"Colunas de transferencias: {len(transf_raw.columns)}")

        print("6. Padronizando transferencias...")
        transf = padronizar_transferencias_publicas(transf_raw)
        salvar_csv_parquet(transf, "transferencias_publicas_padronizadas")

        print("7. Integrando cadastro mestre + transferencias...")
        base_fin = integrar_cadastro_com_transferencias(cadastro, transf)
        salvar_csv_parquet(base_fin, "base_financiamento_publico_oscs")

    print("8. Carregando pagamentos TransfereGov...")
    pag = carregar_pagamentos()
    print(f"Pagamentos: {len(pag):,}")
    salvar_csv_parquet(pag, "pagamentos_transferegov_padronizados")

    base_fin_transferegov = None
    if 'cnpj' in pag.columns:
        print("9. Integrando TransfereGov com cadastro OSC por CNPJ...")
        cadastro_merge = selecionar_colunas_cadastro_para_merge(cadastro)
        base_fin_transferegov = pag.merge(cadastro_merge, on='cnpj', how='left')
        salvar_csv_parquet(base_fin_transferegov, 'base_financiamento_publico_oscs_transferegov')
    else:
        print(
            "9. Integracao com cadastro OSC nao executada: "
            "o arquivo de pagamentos nao contem CNPJ do convenente."
        )

    print("10. Gerando indicadores de financiamento...")
    base_resumo = base_fin_transferegov
    if base_resumo is None and transf is not None:
        base_resumo = integrar_cadastro_com_transferencias(cadastro, transf)
    if base_resumo is None:
        base_resumo = pag
    indicadores_fin = gerar_indicadores_financiamento(base_resumo)
    for nome, df in indicadores_fin.items():
        salvar_csv_parquet(df, nome)

    print("11. Carregando Lei Rouanet...")
    try:
        rouanet_raw = carregar_lei_rouanet()
    except FileNotFoundError as exc:
        print(f"11. Fonte opcional ausente: {exc}")
    else:
        print(f"Registros Lei Rouanet: {len(rouanet_raw):,}")
        print(f"Colunas Lei Rouanet: {len(rouanet_raw.columns)}")

        print("12. Padronizando Lei Rouanet...")
        rouanet = padronizar_lei_rouanet(rouanet_raw)
        salvar_csv_parquet(rouanet, "lei_rouanet_padronizada")

        if "cnpj" in rouanet.columns:
            print("13. Integrando Lei Rouanet com cadastro OSC por CNPJ...")
            base_rouanet = rouanet.merge(cadastro, on="cnpj", how="left")
            salvar_csv_parquet(base_rouanet, "base_lei_rouanet_oscs")

            print("14. Gerando indicadores Lei Rouanet...")
            indicadores_rouanet = gerar_indicadores_lei_rouanet(base_rouanet)
            for nome, df in indicadores_rouanet.items():
                salvar_csv_parquet(df, nome)

    print("Pipeline V2 concluido com sucesso.")
    print(f"Saidas em: {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
