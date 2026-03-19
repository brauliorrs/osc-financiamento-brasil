# Financiamento das Organizacoes da Sociedade Civil no Brasil
## Integracao de bases de dados e infraestrutura analitica reprodutivel

Este repositorio contem o pipeline computacional desenvolvido para integrar bases de dados sobre o financiamento das Organizacoes da Sociedade Civil (OSCs) no Brasil.

O projeto integra informacoes provenientes de diferentes fontes institucionais, incluindo dados sobre transferencias publicas, incentivos fiscais e investimento social privado.

O objetivo e construir uma base analitica consolidada capaz de subsidiar analises academicas, relatorios tecnicos e visualizacoes interativas sobre o financiamento do terceiro setor no pais.

---

# Objetivos do projeto

- integrar bases de dados sobre financiamento das OSCs
- padronizar e harmonizar variaveis provenientes de diferentes sistemas
- produzir indicadores territoriais e tematicos de financiamento
- disponibilizar dashboards interativos para exploracao dos dados
- garantir reprodutibilidade cientifica do pipeline

---

# Estrutura do repositorio

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
|   |-- metodologia.md
|   |-- catalogo_de_bases.md
|   `-- arquitetura_pipeline.md
|-- outputs/
|   |-- tables/
|   |-- figures/
|   `-- maps/
|-- notebooks/
|   `-- exploracao_dados.ipynb
|-- tests/
|   `-- testes_integridade.py
|-- requirements.txt
|-- runtime.txt
|-- README.md
|-- LICENSE
`-- CITATION.cff
```

---

# Arquitetura do pipeline

O pipeline segue as seguintes etapas:

1. ingestao de dados de diferentes fontes institucionais
2. padronizacao de variaveis e formatos
3. harmonizacao semantica das categorias analiticas
4. integracao das bases de dados
5. controle de qualidade e validacao
6. geracao de indicadores e analises territoriais
7. visualizacao interativa e dashboards

---

# Tecnologias utilizadas

Bibliotecas principais:

- pandas
- geopandas
- plotly
- streamlit
- requests
- pyarrow

---

# Dados e reprodutibilidade

Por padrao, os diretorios `data/raw`, `data/interim` e `data/processed` nao sao versionados no GitHub. Isso significa que o repositorio publico contem o codigo, a documentacao e os metadados do projeto, mas nao inclui automaticamente os arquivos de dados de grande porte utilizados nas analises.

Para reproduzir os resultados localmente, e necessario disponibilizar os insumos em `data/raw/` e executar o pipeline.

Entradas atualmente utilizadas no projeto:

- `data/raw/mapa_osc_base.csv`
- `data/raw/mapa_osc_dicionario.xlsx`
- `data/raw/transferegov/siconv_pagamento.csv`
- opcionalmente, outras bases complementares de transferencias publicas

Saidas geradas pelo pipeline incluem, entre outras:

- `cadastro_mestre_oscs`
- `pagamentos_transferegov_padronizados`
- `base_financiamento_publico_oscs_transferegov`
- `financiamento_publico_por_uf`
- `financiamento_publico_por_municipio`
- `financiamento_publico_por_area`
- `concentracao_recursos_por_osc`

---

# Executando o pipeline

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Executar pipeline:

```bash
python -m src.pipeline
```

Executar dashboard:

```bash
streamlit run dashboard/app.py
```

---

# Dashboard

O dashboard Streamlit utiliza prioritariamente os arquivos gerados em `data/processed/`. Para a demonstracao publica do painel, o repositorio tambem inclui um bundle leve em `dashboard/data/`, contendo agregados consolidados e uma amostra da base integrada.

---

# DOI e preservacao digital

As versoes estaveis deste repositorio sao arquivadas automaticamente no Zenodo.

DOI da release atual:

**10.5281/zenodo.19103098**

---

# Licenca

Este projeto e distribuido sob licenca MIT.

---

# Como citar este repositorio

Silva, B. R. R. (2026).  
Infraestrutura analitica para integracao de dados sobre financiamento das OSCs no Brasil.  
DOI: 10.5281/zenodo.19103098

---

# Contato

Para duvidas ou sugestoes, entre em contato com os autores do projeto.