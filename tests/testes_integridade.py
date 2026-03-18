from src.ingestion.transferegov import caminho_pagamentos, carregar_pagamentos
from src.processing.padronizacao import normalizar_nome_coluna as normalizar_nome_coluna_mapa
from src.processing.padronizacao_transferencias import normalizar_nome_coluna as normalizar_nome_coluna_transferencias


def test_normalizacao_remove_acentos():
    assert normalizar_nome_coluna_mapa("Razão Social (OSC)") == "razao_social_osc"
    assert normalizar_nome_coluna_transferencias("Órgão Concedente") == "orgao_concedente"


def test_caminho_pagamentos_encontra_arquivo_existente():
    caminho = caminho_pagamentos()
    assert caminho.name in {"siconv_pagamento.csv", "siconv_pagamentos.csv"}


def test_carregar_pagamentos_padroniza_colunas_basicas():
    df = carregar_pagamentos().head(10)

    assert "valor_pago" in df.columns
    assert "ano" in df.columns
    if "numero_convenio" in df.columns:
        assert df["numero_convenio"].notna().any()