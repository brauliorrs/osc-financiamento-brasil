# Financiamento das Organizações da Sociedade Civil no Brasil
## Infraestrutura analítica reprodutível para integração de bases, produção de indicadores e visualização interativa

Este repositório apresenta uma infraestrutura analítica reprodutível voltada à integração de bases de dados sobre o financiamento das Organizações da Sociedade Civil (OSCs) no Brasil. O projeto foi desenvolvido para apoiar diagnósticos técnicos, pesquisas empíricas e visualizações públicas sobre transferências públicas, financiamento incentivado e padrões de concentração de recursos no setor.

A proposta está alinhada ao esforço de construir uma base integrada sobre financiamento das OSCs brasileiras, reduzindo a fragmentação informacional entre sistemas administrativos e ampliando a capacidade de análise territorial, temática e distributiva.

Painel público: https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/  
Repositório: https://github.com/brauliorrs/osc-financiamento-brasil  
DOI: https://doi.org/10.5281/zenodo.19103098

---

## Estado atual do projeto

A versão atual do projeto já implementa, em grau operacional, as seguintes entregas:

- padronização do cadastro mestre das OSCs a partir do Mapa das OSCs;
- integração inicial com pagamentos do TransfereGov/SICONV;
- geração de indicadores de financiamento por UF, município, área temática e concentração de recursos;
- painel interativo em Streamlit para exploração dos resultados;
- incorporação inicial de dados da Lei Rouanet na camada de financiamento incentivado;
- versionamento do código em repositório aberto e arquivamento estável com DOI.

Essa infraestrutura não deve ser interpretada como etapa final do projeto de pesquisa, mas como demonstração concreta de viabilidade técnica para expansão a novas fontes e aprofundamento analítico.

---

## Objetivos

- integrar bases de dados sobre financiamento das OSCs no Brasil;
- padronizar e harmonizar variáveis provenientes de diferentes sistemas institucionais;
- produzir indicadores territoriais, temáticos e distributivos de financiamento;
- disponibilizar visualizações interativas para exploração pública dos dados;
- garantir reprodutibilidade científica por meio de pipeline versionado e documentado.

---

## Arquitetura do pipeline

O pipeline segue uma estrutura modular composta por:

1. ingestão de dados de diferentes fontes institucionais;
2. padronização de variáveis e formatos;
3. harmonização semântica de categorias analíticas;
4. integração das bases;
5. controle de qualidade e validação;
6. geração de indicadores e agregados;
7. visualização interativa e documentação do processo.

---

## Fontes atualmente incorporadas

### Operacionais no pipeline

- Mapa das Organizações da Sociedade Civil (cadastro mestre)
- TransfereGov / SICONV (pagamentos e vínculo com convenentes)
- Lei Rouanet (camada inicial a partir da base de proponentes)

### Estrutura preparada para expansão

- transferências públicas complementares
- incentivos fiscais e benefícios tributários
- investimento social privado
- demais bases previstas no escopo da pesquisa

---

## Principais saídas analíticas

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

## Estrutura do repositório

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

Por padrão, os diretórios `data/raw`, `data/interim` e `data/processed` não são versionados no GitHub. O repositório público distribui o código, a documentação e os metadados do projeto, mas não inclui automaticamente os arquivos de dados de grande porte utilizados nas análises completas.

Para reprodução local integral, é necessário disponibilizar os insumos em `data/raw/` e executar o pipeline.

Entradas hoje utilizadas no ambiente local:

- `data/raw/mapa_osc_base.csv`
- `data/raw/mapa_osc_dicionario.xlsx`
- `data/raw/transferegov/siconv_pagamento.csv`
- `data/raw/lei_rouanet/proponentes.csv` ou download automático da fonte oficial

O painel público utiliza um bundle leve em `dashboard/data/`, contendo agregados consolidados e uma amostra da base integrada, suficiente para demonstração institucional e exploração inicial.

---

## Execução local

Instalação de dependências:

```bash
pip install -r requirements.txt
```

Execução do pipeline:

```bash
python -m src.pipeline
```

Execução do dashboard:

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

## DOI e preservação digital

As versões estáveis deste repositório são arquivadas no Zenodo.

DOI da release atual:

**10.5281/zenodo.19103098**

---

## Licença

Este projeto é distribuído sob licença MIT.

---

## Como citar este repositório

Silva, B. R. R. (2026).  
Infraestrutura analítica para integração de dados sobre financiamento das OSCs no Brasil.  
DOI: 10.5281/zenodo.19103098

---

## Contato

Para dúvidas, sugestões ou colaborações, entre em contato com os autores do projeto.
