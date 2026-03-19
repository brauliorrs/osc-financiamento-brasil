# Projeto de pesquisa para submissao
## Integracao de bases de dados sobre o financiamento das Organizacoes da Sociedade Civil no Brasil: infraestrutura analitica reprodutivel, pipeline em Python e visualizacao interativa

### 1. Introducao

As Organizacoes da Sociedade Civil (OSCs) desempenham papel relevante na provisao de servicos, na promocao de direitos e na implementacao de iniciativas de interesse publico em multiplas areas, atuando frequentemente como parceiras do Estado e da sociedade. No Brasil, esse universo e amplo e diverso, com forte presenca territorial e elevada relevancia social e institucional.

Apesar dessa centralidade, ainda nao existe um esforco suficientemente sistematico e integrado que permita mapear, de forma abrangente e comparavel, as distintas fontes de financiamento — publicas e privadas — que sustentam as OSCs brasileiras. A fragmentacao das bases de dados disponiveis dificulta a compreensao da estrutura de financiamento do setor e limita analises sobre sustentabilidade organizacional, padroes de concentracao de recursos e relacoes entre organizacoes, poder publico e financiadores privados.

O presente projeto busca contribuir para essa agenda por meio da construcao de uma infraestrutura integrada de dados sobre financiamento das OSCs no Brasil, apoiada em pipeline reprodutivel em Python, documentacao metodologica, indicadores analiticos e visualizacao interativa em ambiente web. A proposta parte de uma implementacao inicial ja operacional, que demonstra a viabilidade tecnica da integracao entre bases administrativas e a producao de paineis publicos de exploracao analitica.

Painel interativo preliminar:  
https://osc-financiamento-brasil-fwaqtyjfe9civ3ix83hd4a.streamlit.app/

Repositorio do projeto:  
https://github.com/brauliorrs/osc-financiamento-brasil

DOI:  
https://doi.org/10.5281/zenodo.19103098

### 2. Problema de pesquisa

As informacoes sobre financiamento das OSCs no Brasil encontram-se dispersas em multiplos sistemas administrativos e institucionais, com diferentes formatos, coberturas e logicas de registro. Essa fragmentacao limita a compreensao do volume, da composicao e da distribuicao territorial dos recursos destinados ao setor, dificultando a producao de diagnosticos comparaveis e a formulacao de analises baseadas em evidencias.

Nesse contexto, a questao central que orienta a pesquisa e:

**Como integrar, sistematizar e analisar as principais bases de dados sobre financiamento das OSCs no Brasil, produzindo uma infraestrutura analitica reprodutivel capaz de subsidiar pesquisas e politicas publicas?**

### 3. Objetivos

#### 3.1 Objetivo geral

Integrar e sistematizar diferentes bases de dados sobre financiamento das Organizacoes da Sociedade Civil no Brasil, desenvolvendo um pipeline reprodutivel em Python para analise, visualizacao interativa e disseminacao publica dos dados.

#### 3.2 Objetivos especificos

- identificar e catalogar bases de dados relevantes para o estudo do financiamento das OSCs;
- padronizar e harmonizar variaveis provenientes de diferentes sistemas administrativos e institucionais;
- integrar dados sobre transferencias publicas, incentivos fiscais e investimento social privado;
- produzir indicadores territoriais, tematicos e distributivos de financiamento;
- desenvolver dashboards interativos para exploracao analitica e difusao publica dos resultados;
- disponibilizar o pipeline computacional em repositorio aberto, com versionamento e possibilidade de arquivamento com DOI.

### 4. Justificativa e aderencia ao projeto da chamada

O projeto esta diretamente alinhado ao escopo da chamada publica “Quem financia as OSCs brasileiras?”, uma vez que busca identificar, sistematizar e integrar as principais bases de dados sobre financiamento do setor, organizando essas informacoes em infraestrutura analitica reutilizavel e em painel publico voltado a exploracao dos resultados.

Em sua implementacao atual, a infraestrutura ja opera com:

- base cadastral do Mapa das OSCs;
- integracao com pagamentos do TransfereGov/SICONV;
- geracao de indicadores de financiamento por UF, municipio, area tematica e concentracao;
- visualizacao interativa publica;
- incorporacao inicial da base de proponentes da Lei Rouanet, como primeira camada de financiamento incentivado.

Essa etapa ja demonstra capacidade de:

- integrar e organizar bancos de dados e seus codigos;
- produzir indicadores a partir de registros administrativos;
- estruturar paineis analiticos publicos;
- reduzir fragmentacao informacional sobre financiamento das OSCs.

A pesquisa proposta para a bolsa corresponde, portanto, ao aprofundamento e expansao dessa infraestrutura, com incorporacao de novas fontes, refinamento metodologico e producao de diagnosticos aplicados e notas tecnicas.

### 5. Referencial teorico

A literatura sobre sociedade civil e terceiro setor reconhece a importancia das associacoes e organizacoes sem fins lucrativos para a vida democratica, a provisao de bens publicos e a mediacao entre Estado e sociedade. Em Tocqueville (1835), as associacoes civis aparecem como elementos fundamentais para a cooperacao social e o aprendizado democratico. Em Salamon e Anheier (1998), o terceiro setor e tratado como esfera institucional relevante para compreender arranjos contemporaneos de governanca, provisao de servicos e inovacao social.

No que se refere ao financiamento das OSCs, a literatura mostra que o setor opera por meio de arranjos hibridos, combinando recursos publicos, privados, incentivos fiscais e receitas proprias. Essa diversidade de fontes torna particularmente relevante a construcao de bases integradas capazes de captar composicao, volume, distribuicao e concentracao dos recursos (Salamon, 2010).

A literatura sobre transparencia publica e dados abertos tambem fornece suporte importante ao projeto. A abertura de dados administrativos amplia possibilidades de escrutinio, reuso e inovacao civica, mas nao elimina o problema da fragmentacao entre sistemas. Nesse contexto, infraestruturas analiticas reprodutiveis sao essenciais para converter dados dispersos em evidencia utilizavel por pesquisadores, gestores publicos e organizacoes da sociedade civil (Noveck, 2015).

### 6. Metodologia

A pesquisa possui natureza aplicada e exploratoria, combinando:

- revisao bibliografica e documental;
- integracao de bases administrativas;
- analise quantitativa;
- visualizacao interativa de dados.

O projeto sera desenvolvido integralmente em Python, com arquitetura modular e reprodutivel. O pipeline encontra-se organizado em camadas de ingestao, padronizacao, harmonizacao semantica, integracao, controle de qualidade e producao de indicadores.

A estrategia metodologica parte de uma implementacao inicial ja em desenvolvimento, o que permite articular formulacao analitica e validacao empirica progressiva. Em vez de iniciar do zero, a bolsa permitira consolidar uma infraestrutura ja funcional, ampliando seu escopo, robustez e utilidade publica.

As etapas principais serao:

**Ingestao**  
Leitura e organizacao de bases em diferentes formatos, com priorizacao de fontes administrativas governamentais e bases publicas estruturadas.

**Padronizacao**  
Normalizacao de nomes de variaveis, formatos de datas, identificadores institucionais, codigos territoriais e valores monetarios.

**Harmonizacao semantica**  
Criacao de equivalencias entre categorias analiticas e variaveis provenientes de diferentes sistemas.

**Integracao**  
Vinculacao de registros por CNPJ, territorialidade, tempo e atributos analiticos, de forma rastreavel e documentada.

**Controle de qualidade**  
Testes de consistencia, avaliacao de completude, verificacao de duplicidades e documentacao dos procedimentos adotados.

**Producao analitica**  
Geracao de indicadores, tabelas, visualizacoes interativas e produtos tecnicos voltados a analise do financiamento das OSCs.

### 7. Pipeline computacional

O pipeline do projeto estrutura-se da seguinte forma:

Fontes de dados  
↓  
Ingestao em Python  
↓  
Padronizacao  
↓  
Harmonizacao semantica  
↓  
Integracao das bases  
↓  
Controle de qualidade  
↓  
Base analitica consolidada  
↓  
Indicadores e dashboards  
↓  
GitHub → Zenodo → DOI

Entre as fontes prioritarias, destacam-se:

- Mapa das OSCs;
- TransfereGov/SICONV;
- Lei Rouanet/SALIC;
- bases de transferencias publicas complementares;
- bases futuras sobre incentivos fiscais, financas municipais e investimento social privado.

### 8. Estado atual de desenvolvimento

O projeto ja dispoe de uma versao inicial operacional da infraestrutura analitica, com os seguintes resultados alcancados:

- construcao e padronizacao do cadastro mestre das OSCs;
- leitura e integracao inicial de pagamentos do TransfereGov/SICONV;
- producao de indicadores por UF, municipio, area tematica e concentracao de recursos;
- construcao de painel interativo publico em Streamlit;
- disponibilizacao do codigo em repositorio aberto com DOI;
- incorporacao inicial da base de proponentes da Lei Rouanet, ampliando o escopo para financiamento incentivado.

Esse estagio inicial demonstra a viabilidade tecnica da proposta e oferece base concreta para aprofundamento analitico ao longo da bolsa.

### 9. Atividades a serem desenvolvidas durante a bolsa

Em consonancia com a chamada, as atividades previstas sao:

- redigir relatorios e notas tecnicas;
- integrar e organizar bancos de dados, suas fontes e os codigos utilizados na integracao;
- ampliar a cobertura de fontes de financiamento, com prospeccao e incorporacao gradual de novas bases;
- apoiar a sistematizacao de dados de maior qualidade sobre o setor, inclusive em interlocucao institucional quando necessario;
- participar de reunioes periodicas para apresentacao de resultados e acompanhamento das atividades;
- estruturar dados e produtos analiticos que possam subsidiar novas analises conduzidas no ambito do Ipea.

### 10. Produtos e resultados esperados

#### Produtos imediatos

- base integrada sobre financiamento direto e incentivado de OSCs;
- relatorios analiticos e notas tecnicas sobre estrutura e distribuicao do financiamento;
- indicadores territoriais e distributivos de financiamento;
- painel interativo para exploracao publica dos dados;
- documentacao metodologica do pipeline e das fontes utilizadas.

#### Resultados esperados

- ampliacao da capacidade analitica sobre financiamento das OSCs no Brasil;
- consolidacao de infraestrutura publica de dados passivel de incorporacao ao ambiente do Mapa das OSCs;
- maior transparencia sobre transferencias, incentivos e padroes de concentracao dos recursos;
- subsidios para diagnosticos aplicados e formulacao de politicas publicas;
- reducao de custos de acesso e tratamento de dados para a comunidade academica e institucional;
- fortalecimento da agenda de dados publicos, reprodutibilidade e governo aberto.

### 11. Inovacao cientifica

O projeto apresenta quatro contribuicoes principais:

- integracao de bases dispersas sobre financiamento das OSCs;
- desenvolvimento de pipeline reprodutivel em Python para tratamento e integracao de dados administrativos;
- producao de visualizacao interativa publica como ferramenta analitica e de transparencia;
- construcao de infraestrutura aberta com versionamento e DOI.

### 12. Cronograma

| Meses | Atividades |
|---|---|
| 1–2 | revisao bibliografica e documental; refinamento do inventario de bases |
| 2–3 | catalogacao e documentacao das fontes |
| 3–5 | ingestao e padronizacao de novas bases |
| 4–6 | harmonizacao semantica e integracao |
| 6–8 | controle de qualidade e refinamento metodologico |
| 7–9 | producao de indicadores e analises aplicadas |
| 8–10 | aperfeicoamento do painel e produtos de visualizacao |
| 10–12 | notas tecnicas, relatorio final e consolidacao dos produtos |

### 13. Plano de gestao de dados

Os dados serao organizados em tres camadas principais:

- `raw`: dados originais;
- `interim`: dados padronizados e preparados para integracao;
- `processed`: bases consolidadas e prontas para analise.

Scripts, documentacao metodologica e versoes estaveis do pipeline serao disponibilizados em repositorio versionado, com arquivamento das versoes estaveis no Zenodo.

### Referencias

ANHEIER, H.; SALAMON, L. *The Emerging Sector Revisited*. Johns Hopkins University, 1998.

IPEA. *Mapa das Organizacoes da Sociedade Civil*. Disponivel em: https://mapaosc.ipea.gov.br.

NOVECK, B. *Smart Citizens, Smarter State: The Technologies of Expertise and the Future of Governing*. Harvard University Press, 2015.

SALAMON, L. *The State of Nonprofit America*. Brookings Institution Press, 2010.

TOCQUEVILLE, A. *Democracy in America*. 1835.