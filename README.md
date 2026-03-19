# Financiamento das Organizações da Sociedade Civil no Brasil
## Integração de bases de dados e infraestrutura analítica reprodutível

Este repositório contém o pipeline computacional desenvolvido para integrar bases de dados sobre o financiamento das Organizações da Sociedade Civil (OSCs) no Brasil.

O projeto integra informações provenientes de diferentes fontes institucionais, incluindo dados sobre transferências públicas, incentivos fiscais e investimento social privado.

O objetivo é construir uma base analítica consolidada capaz de subsidiar análises acadêmicas, relatórios técnicos e visualizações interativas sobre o financiamento do terceiro setor no país.

---

# Objetivos do projeto

- integrar bases de dados sobre financiamento das OSCs
- padronizar e harmonizar variáveis provenientes de diferentes sistemas
- produzir indicadores territoriais e temáticos de financiamento
- disponibilizar dashboards interativos para exploração dos dados
- garantir reprodutibilidade científica do pipeline

---

# Estrutura do repositório
osc-financiamento-brasil/
│
├ data/
│ ├ raw/
│ ├ interim/
│ └ processed/
│
├ src/
│ ├ ingestion/
│ ├ processing/
│ ├ integration/
│ ├ analytics/
│ └ viz/
│
├ dashboard/
│ └ app.py
│
├ docs/
│ ├ metodologia.md
│ ├ catalogo_de_bases.md
│ └ arquitetura_pipeline.md
│
├ outputs/
│ ├ tables/
│ ├ figures/
│ └ maps/
│
├ notebooks/
│ └ exploracao_dados.ipynb
│
├ tests/
│ └ testes_integridade.py
│
├ requirements.txt
├ README.md
├ LICENSE
└ CITATION.cff

---

# Arquitetura do pipeline

O pipeline segue as seguintes etapas:

1. ingestão de dados de diferentes fontes institucionais  
2. padronização de variáveis e formatos  
3. harmonização semântica das categorias analíticas  
4. integração das bases de dados  
5. controle de qualidade e validação  
6. geração de indicadores e análises territoriais  
7. visualização interativa e dashboards  

---

# Tecnologias utilizadas

Python

Bibliotecas principais:

- pandas
- geopandas
- plotly
- streamlit
- requests
- pyarrow

---

# Executando o pipeline

Instalar dependências:
pip install -r requirements.txt

Executar pipeline:
python src/pipeline.py

Executar dashboard:

streamlit run dashboard/app.py


---

# Reprodutibilidade científica

Todos os scripts de coleta, tratamento e integração de dados estão documentados neste repositório.

O pipeline foi desenvolvido para permitir a reprodução completa das análises realizadas no projeto.

---

# DOI e preservação digital

As verssões estáveis deste repositório são arquivadas automaticamente no Zenodo.

DOI da release atual:

10.5281/zenodo.19103098

---

# Licença

Este projeto é distribuído sob licença MIT.

---

# Como citar este repositório

SILVA, B, R, R, (2026).  
Infraestrutura analítica para integração de dados sobre financiamento das OSCs no Brasil.  
DOI: 10.5281/zenodo.19103098

---

# Contato

Para dúvidas ou sugestões, entre em contato com oS autores do projeto.


