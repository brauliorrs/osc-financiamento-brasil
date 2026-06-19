# OSC Financiamento Brasil

**Pipeline e dashboard para análise do financiamento das Organizações da Sociedade Civil no Brasil com dados públicos, Streamlit e DOI.**

O **OSC Financiamento Brasil** é uma infraestrutura analítica reprodutível para integrar, padronizar e visualizar bases públicas sobre financiamento das Organizações da Sociedade Civil (OSCs) no Brasil.

O projeto combina engenharia de dados, análise territorial, indicadores temáticos e visualização interativa para apoiar pesquisa, diagnóstico técnico, políticas públicas e inteligência institucional.

- **Painel público:** https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/
- **Repositório:** https://github.com/brauliorrs/osc-financiamento-brasil
- **DOI:** https://doi.org/10.5281/zenodo.19103098

---

## Resumo executivo

O projeto integra bases públicas relacionadas ao financiamento das OSCs brasileiras e gera indicadores por território, área temática e concentração de recursos.

**Entrega principal:** pipeline reprodutível + bases derivadas + dashboard público + preservação com DOI  
**Stack:** Python, pandas, Streamlit, Plotly, pyarrow, geopandas  
**Uso:** pesquisa aplicada, políticas públicas, diagnóstico institucional, transparência e análise do terceiro setor  
**Status:** versão operacional com painel público, release arquivada e estrutura preparada para expansão de fontes

---

## Problema

As informações sobre financiamento das Organizações da Sociedade Civil no Brasil estão distribuídas em diferentes sistemas administrativos, bases públicas e formatos institucionais.

Essa fragmentação dificulta:

- identificar padrões territoriais de financiamento;
- comparar recursos por UF, município e área temática;
- analisar concentração de valores por organização;
- cruzar bases de financiamento público e incentivado;
- produzir diagnósticos reprodutíveis;
- transformar dados administrativos em inteligência analítica.

O resultado é que existem muitos dados disponíveis, mas pouca integração sistemática para análise pública, científica e institucional.

---

## Solução

O projeto propõe uma infraestrutura analítica que:

1. coleta e organiza bases públicas sobre OSCs e financiamento;
2. padroniza variáveis, formatos e categorias;
3. harmoniza identificadores e dimensões territoriais;
4. integra bases administrativas distintas;
5. gera indicadores analíticos e agregados;
6. disponibiliza resultados em dashboard Streamlit;
7. preserva versões estáveis com DOI.

A proposta não é apenas criar um painel, mas construir uma base técnica reprodutível para pesquisas futuras sobre financiamento, território, desigualdades, concentração de recursos e políticas públicas voltadas ao terceiro setor.

---

## Estado atual do projeto

A versão atual já implementa:

- cadastro mestre das OSCs a partir do Mapa das OSCs;
- integração inicial com pagamentos do TransfereGov/SICONV;
- camada inicial de financiamento incentivado via Lei Rouanet;
- indicadores por UF, município, área temática e organização;
- métricas de concentração de recursos;
- dashboard público em Streamlit;
- estrutura modular de pipeline;
- documentação de execução local;
- licença MIT;
- arquivo `CITATION.cff`;
- release arquivada no Zenodo com DOI.

Essa infraestrutura deve ser lida como demonstração concreta de viabilidade técnica e como base para expansão metodológica.

---

## Fontes incorporadas

### Operacionais no pipeline

| Fonte | Uso no projeto |
|---|---|
| Mapa das OSCs | Cadastro mestre das organizações |
| TransfereGov / SICONV | Pagamentos e vínculos com convenentes |
| Lei Rouanet | Camada inicial de financiamento incentivado |

### Estrutura preparada para expansão

- transferências públicas complementares;
- incentivos fiscais e benefícios tributários;
- investimento social privado;
- bases estaduais e municipais;
- demais fontes previstas no escopo de pesquisa.

---

## Principais saídas analíticas

O pipeline gera bases derivadas e agregados como:

- `cadastro_mestre_oscs`;
- `pagamentos_transferegov_padronizados`;
- `base_financiamento_publico_oscs_transferegov`;
- `financiamento_publico_por_uf`;
- `financiamento_publico_por_municipio`;
- `financiamento_publico_por_area`;
- `concentracao_recursos_por_osc`;
- `lei_rouanet_padronizada`;
- `base_lei_rouanet_oscs`;
- `lei_rouanet_captado_por_uf`;
- `lei_rouanet_captado_por_municipio`;
- `lei_rouanet_concentracao_por_osc`.

Essas saídas permitem observar distribuição territorial, concentração, áreas de atuação, volume de recursos e vínculos entre bases de financiamento.

---

## Arquitetura do pipeline

```text
Fontes públicas
      ↓
Ingestão de dados
      ↓
Padronização de variáveis
      ↓
Harmonização territorial e temática
      ↓
Integração das bases
      ↓
Controle de qualidade
      ↓
Geração de indicadores
      ↓
Bases derivadas e agregados
      ↓
Dashboard Streamlit
      ↓
Release e preservação com DOI
```

---

## Estrutura do repositório

```text
osc-financiamento-brasil/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── integration/
│   ├── analytics/
│   └── viz/
├── dashboard/
│   ├── app.py
│   └── data/
├── docs/
├── outputs/
├── notebooks/
├── tests/
├── requirements.txt
├── runtime.txt
├── README.md
├── LICENSE
└── CITATION.cff
```

---

## Dashboard

O painel público em Streamlit apresenta uma camada leve de exploração dos dados consolidados.

Ele permite visualizar, em formato interativo:

- distribuição territorial dos recursos;
- indicadores por UF e município;
- recortes por área temática;
- concentração de financiamento por OSC;
- camada inicial de análise da Lei Rouanet;
- amostras consolidadas da base integrada.

Acesse:

https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/

---

## Dados e reprodutibilidade

Por padrão, os diretórios `data/raw`, `data/interim` e `data/processed` não são versionados no GitHub.

O repositório público distribui:

- código-fonte;
- documentação;
- metadados;
- dashboard;
- agregados leves para demonstração;
- estrutura de reprodutibilidade.

Para reprodução local integral, é necessário disponibilizar os insumos em `data/raw/` e executar o pipeline.

### Entradas esperadas no ambiente local

```text
data/raw/mapa_osc_base.csv
data/raw/mapa_osc_dicionario.xlsx
data/raw/transferegov/siconv_pagamento.csv
data/raw/lei_rouanet/proponentes.csv
```

A base da Lei Rouanet também pode ser obtida por download automático quando configurada a partir da fonte oficial.

O painel público utiliza um bundle leve em `dashboard/data/`, contendo agregados consolidados e uma amostra da base integrada, suficiente para demonstração institucional e exploração inicial.

---

## Como executar localmente

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o pipeline

```bash
python -m src.pipeline
```

### 3. Executar o dashboard

```bash
streamlit run dashboard/app.py
```

---

## Tecnologias utilizadas

Bibliotecas e ferramentas principais:

- Python;
- pandas;
- plotly;
- streamlit;
- requests;
- pyarrow;
- geopandas;
- shapely.

---

## O que este projeto demonstra

Este repositório evidencia competências em:

- engenharia de dados aplicada a bases públicas;
- integração de fontes administrativas heterogêneas;
- padronização e harmonização de dados;
- análise territorial e temática;
- construção de indicadores de concentração;
- dashboards analíticos com Streamlit;
- documentação técnica e científica;
- reprodutibilidade de pesquisa;
- preservação digital com DOI;
- transformação de dados públicos em inteligência institucional.

---

## Roadmap

### Concluído ou em funcionamento

- Cadastro mestre das OSCs
- Integração inicial com TransfereGov/SICONV
- Camada inicial da Lei Rouanet
- Indicadores territoriais e temáticos
- Dashboard público em Streamlit
- Estrutura modular de pipeline
- Release arquivada no Zenodo
- DOI público

### Próximas etapas

- Ampliar integração com novas bases de financiamento público
- Melhorar validações automáticas de consistência
- Expandir indicadores por área temática e território
- Incluir novas camadas de financiamento incentivado
- Documentar metodologia em arquivos específicos em `docs/`
- Criar relatórios analíticos exportáveis
- Ampliar testes automatizados do pipeline

---

## Limitações

O projeto trabalha com bases públicas que podem apresentar limitações de completude, atualização, padronização e disponibilidade.

Entre as limitações esperadas estão:

- diferenças de formato entre fontes;
- ausência de identificadores uniformes;
- dados administrativos incompletos;
- alterações em bases públicas de origem;
- necessidade de tratamento manual em casos específicos;
- distinção entre dados disponíveis e universo total de financiamento das OSCs.

Essas limitações são tratadas como parte do desafio metodológico do projeto.

---

## DOI e preservação digital

As versões estáveis deste repositório são arquivadas no Zenodo.

DOI da release atual:

**10.5281/zenodo.19103098**

Link:

https://doi.org/10.5281/zenodo.19103098

---

## Como citar

Silva, B. R. R. (2026).  
**Infraestrutura analítica para integração de dados sobre financiamento das OSCs no Brasil.**  
DOI: 10.5281/zenodo.19103098

---

## Licença

Este projeto é distribuído sob licença MIT. Consulte o arquivo `LICENSE`.

---

## Autor

**Bráulio Roberto Rangel da Silva**

Pesquisador e desenvolvedor com atuação em dados públicos, automação, observatórios digitais, pesquisa aplicada e produtos digitais.

GitHub: [@brauliorrs](https://github.com/brauliorrs)
