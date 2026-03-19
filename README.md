# Financiamento das Organizacoes da Sociedade Civil no Brasil
## Infraestrutura analitica reprodutivel para integracao de bases, producao de indicadores e visualizacao interativa

Este repositorio apresenta uma infraestrutura analitica reprodutivel voltada a integracao de bases de dados sobre o financiamento das Organizacoes da Sociedade Civil (OSCs) no Brasil. O projeto foi desenvolvido para apoiar diagnosticos tecnicos, pesquisas empiricas e visualizacoes publicas sobre transferencias publicas, financiamento incentivado e padroes de concentracao de recursos no setor.

A proposta esta alinhada ao esforco de construir uma base integrada sobre financiamento das OSCs brasileiras, reduzindo a fragmentacao informacional entre sistemas administrativos e ampliando a capacidade de analise territorial, tematica e distributiva.

Painel publico: https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/  
Repositorio: https://github.com/brauliorrs/osc-financiamento-brasil  
DOI: https://doi.org/10.5281/zenodo.19103098

## Links do projeto

- Dashboard Streamlit: https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/
- Reposit??rio GitHub: https://github.com/brauliorrs/osc-financiamento-brasil
- DOI no Zenodo: 10.5281/zenodo.19103098

---

## Estado atual do projeto

A versao atual do projeto ja implementa, em grau operacional, as seguintes entregas:

- padronizacao do cadastro mestre das OSCs a partir do Mapa das OSCs;
- integracao inicial com pagamentos do TransfereGov/SICONV;
- geracao de indicadores de financiamento por UF, municipio, area tematica e concentracao de recursos;
- painel interativo em Streamlit para exploracao dos resultados;
- incorporacao inicial de dados da Lei Rouanet na camada de financiamento incentivado;
- versionamento do codigo em repositorio aberto e arquivamento estavel com DOI.

Essa infraestrutura nao deve ser interpretada como etapa final do projeto de pesquisa, mas como demonstracao concreta de viabilidade tecnica para expansao a novas fontes e aprofundamento analitico.

---

## Objetivos

- integrar bases de dados sobre financiamento das OSCs no Brasil;
- padronizar e harmonizar variaveis provenientes de diferentes sistemas institucionais;
- produzir indicadores territoriais, tematicos e distributivos de financiamento;
- disponibilizar visualizacoes interativas para exploracao publica dos dados;
- garantir reprodutibilidade cientifica por meio de pipeline versionado e documentado.

---

## Arquitetura do pipeline

O pipeline segue uma estrutura modular composta por:

1. ingestao de dados de diferentes fontes institucionais;
2. padronizacao de variaveis e formatos;
3. harmonizacao semantica de categorias analiticas;
4. integracao das bases;
5. controle de qualidade e validacao;
6. geracao de indicadores e agregados;
7. visualizacao interativa e documentacao do processo.

---

## Fontes atualmente incorporadas

### Operacionais no pipeline

- Mapa das Organizacoes da Sociedade Civil (cadastro mestre)
- TransfereGov / SICONV (pagamentos e vinculo com convenentes)
- Lei Rouanet (camada inicial a partir da base de proponentes)

### Estrutura preparada para expansao

- transferencias publicas complementares
- incentivos fiscais e beneficios tributarios
- investimento social privado
- demais bases previstas no escopo da pesquisa

---

## Principais saidas analiticas

O pipeline gera, entre outras, as seguintes bases derivadas:

- `cadastro_mestre_oscs`
- `pagamentos_transferegov_padronizados`
- `base_financiamento_publico_oscs_transferegov`
- `financiamento_publico_por_uf`
- `financiamento_publico_por_municipio`
- `financiamento_publico_por_area`
- `concentracao_recursos_por_osc`
- `lei_rouanet_padronizada`
- `base_lei_rouanet_oscs`
- `lei_rouanet_captado_por_uf`
- `lei_rouanet_captado_por_municipio`
- `lei_rouanet_concentracao_por_osc`

---

## Estrutura do repositorio

```text
osc-financiamento-brasil/
|-- data/
|   |-- raw/
|   |-- interim/
|   `-- processed/
|-- src/
|   |-- ingestion/
|   |-- processing/
|   |-- integration/
|   |-- analytics/
|   `-- viz/
|-- dashboard/
|   |-- app.py
|   `-- data/
|-- docs/
|-- outputs/
|-- notebooks/
|-- tests/
|-- requirements.txt
|-- runtime.txt
|-- README.md
|-- LICENSE
`-- CITATION.cff
```

---

## Dados e reprodutibilidade

Por padrao, os diretorios `data/raw`, `data/interim` e `data/processed` nao sao versionados no GitHub. O repositorio publico distribui o codigo, a documentacao e os metadados do projeto, mas nao inclui automaticamente os arquivos de dados de grande porte utilizados nas analises completas.

Para reproducao local integral, e necessario disponibilizar os insumos em `data/raw/` e executar o pipeline.

Entradas hoje utilizadas no ambiente local:

- `data/raw/mapa_osc_base.csv`
- `data/raw/mapa_osc_dicionario.xlsx`
- `data/raw/transferegov/siconv_pagamento.csv`
- `data/raw/lei_rouanet/proponentes.csv` ou download automatico da fonte oficial

O painel publico utiliza um bundle leve em `dashboard/data/`, contendo agregados consolidados e uma amostra da base integrada, suficiente para demonstracao institucional e exploracao inicial.

---

## Execucao local

Instalacao de dependencias:

```bash
pip install -r requirements.txt
```

Execucao do pipeline:

```bash
python -m src.pipeline
```

Execucao do dashboard:

```bash
streamlit run dashboard/app.py
```

---

## Tecnologias utilizadas

Bibliotecas principais:

- pandas
- plotly
- streamlit
- requests
- pyarrow
- geopandas
- shapely

---

## DOI e preservacao digital

As versoes estaveis deste repositorio sao arquivadas no Zenodo.

DOI da release atual:

**10.5281/zenodo.19103098**

---

## Licenca

Este projeto e distribuido sob licenca MIT.

---

## Como citar este repositorio

Silva, B. R. R. (2026).  
Infraestrutura analitica para integracao de dados sobre financiamento das OSCs no Brasil.  
DOI: 10.5281/zenodo.19103098

Reposit??rio: https://github.com/brauliorrs/osc-financiamento-brasil

Dashboard: https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/

---

## Contato

Para duvidas, sugestoes ou colaboracoes, entre em contato com os autores do projeto.
