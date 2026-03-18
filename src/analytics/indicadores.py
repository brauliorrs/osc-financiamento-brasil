import pandas as pd



def _coalescer_colunas(df: pd.DataFrame, destino: str, candidatos: list[str]) -> pd.DataFrame:
    if destino in df.columns:
        return df

    existentes = [col for col in candidatos if col in df.columns]
    if not existentes:
        return df

    serie = df[existentes[0]]
    for col in existentes[1:]:
        serie = serie.combine_first(df[col])

    df = df.copy()
    df[destino] = serie
    return df



def preparar_base_financiamento(df: pd.DataFrame) -> pd.DataFrame:
    base = df.copy()
    base = _coalescer_colunas(base, 'uf', ['uf', 'uf_x', 'uf_y'])
    base = _coalescer_colunas(base, 'municipio', ['municipio', 'municipio_x', 'municipio_y'])
    return base



def gerar_indicadores_basicos(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    saidas = {}

    if 'uf' in df.columns:
        saidas['oscs_por_uf'] = (
            df.groupby('uf', dropna=False)
            .size()
            .reset_index(name='total_oscs')
            .sort_values('total_oscs', ascending=False)
        )

    if {'uf', 'municipio'}.issubset(df.columns):
        saidas['oscs_por_municipio'] = (
            df.groupby(['uf', 'municipio'], dropna=False)
            .size()
            .reset_index(name='total_oscs')
            .sort_values('total_oscs', ascending=False)
        )

    if 'situacao_cadastral' in df.columns:
        saidas['oscs_por_situacao'] = (
            df.groupby('situacao_cadastral', dropna=False)
            .size()
            .reset_index(name='total_oscs')
            .sort_values('total_oscs', ascending=False)
        )

    if 'natureza_juridica' in df.columns:
        saidas['oscs_por_natureza_juridica'] = (
            df.groupby('natureza_juridica', dropna=False)
            .size()
            .reset_index(name='total_oscs')
            .sort_values('total_oscs', ascending=False)
        )

    if 'matriz_filial' in df.columns:
        saidas['oscs_por_matriz_filial'] = (
            df.groupby('matriz_filial', dropna=False)
            .size()
            .reset_index(name='total_oscs')
            .sort_values('total_oscs', ascending=False)
        )

    area_cols = [c for c in df.columns if c.startswith('area_')]
    if area_cols:
        totais_area = df[area_cols].fillna(0).sum().reset_index()
        totais_area.columns = ['area', 'total_oscs']
        totais_area = totais_area.sort_values('total_oscs', ascending=False)
        saidas['oscs_por_area'] = totais_area

    subarea_cols = [c for c in df.columns if c.startswith('subarea_')]
    if subarea_cols:
        totais_subarea = df[subarea_cols].fillna(0).sum().reset_index()
        totais_subarea.columns = ['subarea', 'total_oscs']
        totais_subarea = totais_subarea.sort_values('total_oscs', ascending=False)
        saidas['oscs_por_subarea'] = totais_subarea

    return saidas



def gerar_indicadores_financiamento(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    base = preparar_base_financiamento(df)
    saidas = {}

    if 'valor_pago' not in base.columns:
        return saidas

    if 'uf' in base.columns:
        saidas['financiamento_publico_por_uf'] = (
            base.groupby('uf', dropna=False)['valor_pago']
            .sum(min_count=1)
            .reset_index()
            .sort_values('valor_pago', ascending=False)
        )

    if {'uf', 'municipio'}.issubset(base.columns):
        saidas['financiamento_publico_por_municipio'] = (
            base.groupby(['uf', 'municipio'], dropna=False)['valor_pago']
            .sum(min_count=1)
            .reset_index()
            .sort_values('valor_pago', ascending=False)
        )

    area_cols = [c for c in base.columns if c.startswith('area_')]
    if area_cols:
        registros_area = []
        for col in area_cols:
            serie = pd.to_numeric(base[col], errors='coerce').fillna(0)
            valor = base.loc[serie > 0, 'valor_pago'].sum(min_count=1)
            registros_area.append({'area': col, 'valor_pago': valor})
        saidas['financiamento_publico_por_area'] = (
            pd.DataFrame(registros_area)
            .sort_values('valor_pago', ascending=False)
            .reset_index(drop=True)
        )

    chaves_concentracao = [c for c in ['cnpj', 'nome_osc', 'nome_convenente', 'uf'] if c in base.columns]
    if 'cnpj' in chaves_concentracao:
        concentracao = (
            base.groupby(chaves_concentracao, dropna=False)['valor_pago']
            .agg(['sum', 'size'])
            .reset_index()
            .rename(columns={'sum': 'valor_pago', 'size': 'quantidade_pagamentos'})
            .sort_values('valor_pago', ascending=False)
            .reset_index(drop=True)
        )
        total = concentracao['valor_pago'].sum()
        if pd.notna(total) and total != 0:
            concentracao['participacao_pct'] = concentracao['valor_pago'] / total * 100
            concentracao['participacao_acumulada_pct'] = concentracao['participacao_pct'].cumsum()
        else:
            concentracao['participacao_pct'] = 0.0
            concentracao['participacao_acumulada_pct'] = 0.0
        concentracao['ranking'] = concentracao.index + 1
        saidas['concentracao_recursos_por_osc'] = concentracao

    return saidas