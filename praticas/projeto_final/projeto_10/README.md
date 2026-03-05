# Projeto 10 — Radiografia Municipal: Onde Foi o Dinheiro Público?

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo B — Analítico Realista (análise pura + investigação de desvio)

---

## Briefing da Operação

O Tribunal de Contas do Estado detectou **inconsistências** em municípios do Ceará: alguns recebem **repasses federais muito acima da média** há anos, mas seus **indicadores sociais permanecem estagnados** — IDH baixo, analfabetismo alto, saneamento precário. Ao mesmo tempo, o volume de licitações nesses municípios é anormalmente alto, com empresas vencedoras que parecem ter **vínculos entre si** (mesmo endereço, mesmos sócios).

Você recebeu indicadores socioeconômicos dos 184 municípios cearenses, dados de repasses federais e registros de licitações. Descubra onde o dinheiro público não está chegando à população.

---

## Datasets Fornecidos

### 1. `data/projeto_10_indicadores_municipais.csv`
Indicadores socioeconômicos dos 184 municípios do Ceará (2020-2023).

| Coluna | Descrição |
|--------|-----------|
| `municipio` | Nome do município |
| `ano` | Ano |
| `populacao` | População |
| `pib_per_capita` | PIB per capita (R$) |
| `idh` | Índice de Desenvolvimento Humano — **atenção: pode conter valores impossíveis** |
| `taxa_analfabetismo_pct` | Taxa de analfabetismo (%) |
| `anos_estudo_medio` | Anos de estudo (média) |
| `mortalidade_infantil_por_mil` | Mortalidade infantil (por 1.000 nascidos vivos) |
| `expectativa_vida_anos` | Expectativa de vida (anos) |
| `indice_gini` | Índice de Gini (desigualdade) |
| `cobertura_esgoto_pct` | Cobertura de esgoto (%) |
| `cobertura_agua_pct` | Cobertura de água tratada (%) |

### 2. `data/projeto_10_repasses_federais.csv`
Repasses federais por município e programa.

| Coluna | Descrição |
|--------|-----------|
| `municipio` | Nome do município |
| `ano` | Ano |
| `programa` | Programa (Saúde, Educação, Saneamento, etc.) |
| `valor_repassado` | Valor repassado (R$) |
| `valor_executado_declarado` | Valor declarado como executado (R$) |
| `fonte` | Fonte do repasse (FPM, FUNDEB, SUS, PAC, Emenda) |

### 3. `data/projeto_10_licitacoes_municipais.csv`
Licitações realizadas pelos municípios.

| Coluna | Descrição |
|--------|-----------|
| `licitacao_id` | Identificador |
| `municipio` | Município |
| `ano` | Ano |
| `objeto` | Objeto da licitação |
| `valor_contrato` | Valor do contrato (R$) |
| `modalidade` | Modalidade (Pregão, Dispensa, Tomada de Preços, etc.) |
| `empresa_vencedora` | Nome da empresa vencedora |
| `cnpj_vencedora` | CNPJ da vencedora |
| `socio_principal` | Sócio principal |
| `endereco_empresa` | Endereço da empresa |
| `numero_participantes` | Número de participantes na licitação |
| `status` | Status (Concluído, Em execução, Atrasado) |

---

## Missão

Investigue os dados e responda:

1. **Quais municípios recebem repasses muito acima da média mas têm indicadores sociais estagnados?** Compare valor total de repasses vs. evolução do IDH, analfabetismo e saneamento.
2. **Os indicadores sociais desses municípios melhoraram ao longo dos anos?** Compare a evolução 2020-2023 dos municípios suspeitos vs. a média estadual.
3. **Existem empresas de fachada nas licitações?** Procure empresas com mesmo endereço, mesmos sócios ou CNPJs muito próximos vencendo licitações nos mesmos municípios.
4. **Há contratos fracionados para evitar licitação?** Identifique municípios com muitos contratos logo abaixo de R$ 80.000 (limite de dispensa de licitação).
5. **A modalidade "Dispensa" é usada excessivamente?** Compare a proporção de dispensas nos municípios suspeitos vs. demais.
6. **Monte o ranking de risco:** Quais municípios combinam alto repasse + indicadores estagnados + licitações suspeitas?
7. **Quais municípios são "outliers positivos"?** IDH acima do esperado dado seu PIB per capita — o que os diferencia?

---

## Pistas Iniciais

- Procure municípios com nome **"Município 101" a "Município 105"** — eles recebem repasses muito altos
- Compare o **total de repasses per capita** dos suspeitos vs. a média — é 2x a 2.5x maior
- Nas licitações, procure empresas com **mesmo endereço ("Rua Fictícia, 100")** e **sócios com mesmo sobrenome ("Almeida")**
- Filtre contratos na faixa **R$ 50.000-79.000** — são suspeitamente frequentes nos municípios com desvio
- Atenção com IDH: há valores impossíveis (1.5, -0.2, 999) que precisam de tratamento

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **IBGE Cidades** | https://cidades.ibge.gov.br/ | Indicadores reais dos municípios cearenses |
| **Atlas Brasil** | http://www.atlasbrasil.org.br/ | IDH e IDHM reais por município |
| **IPEA Data** | http://www.ipeadata.gov.br/ | Indicadores socioeconômicos e repasses |

**Perguntas de cruzamento:**
- Os valores de IDH do dataset estão na faixa realista para municípios do Ceará?
- O volume de repasses per capita dos municípios suspeitos é compatível com dados reais do Portal da Transparência?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Funções para cálculo de scores compostos, tratamento de valores impossíveis, manipulação de strings |
| **M2 — Pandas/NumPy** | `merge` de múltiplas fontes, clusterização manual (quintis, categorização com `cut`/`qcut`), `groupby` com múltiplas agregações, detecção de duplicatas por endereço/sócio, cálculos per capita |
| **M3 — Visualização** | Scatter com tamanho e cor representando variáveis, mapa de correlações, ranking com `barh`, swarmplot, heatmap de indicadores, subplots comparativos |

---

## Estrutura do Projeto

```
projeto_10/
├── README.md          ← Este arquivo
├── data/              ← 3 datasets do projeto
├── notebooks/         ← Notebook(s) Jupyter com a investigação
├── scripts/           ← Scripts Python auxiliares (se necessário)
└── docs/              ← Documentação adicional, apresentação
```

## Entregáveis

1. **Notebook Python (.ipynb)** em `notebooks/` contendo:
   - Importação e inspeção dos 3 datasets
   - Limpeza e transformação (nulos, tipos, valores impossíveis, outliers)
   - Cruzamento entre datasets (merge/join)
   - Análise investigativa com estatísticas descritivas
   - Mínimo de **8 visualizações** (mix de Matplotlib e Seaborn)
   - Respostas à missão com **evidências nos dados**
   - Células Markdown narrando a investigação (storytelling)
   - Conclusões: quais municípios são suspeitos e quais as evidências

2. **Apresentação oral** (5-7 minutos) — arquivo em `docs/`

## Critérios de Avaliação

| Critério | Peso | O que será observado |
|----------|------|----------------------|
| **Limpeza e transformação dos dados** | 20% | Tratamento de nulos, duplicatas, tipos incorretos, outliers. Justificativa das decisões. |
| **Profundidade da investigação** | 25% | Cruzamento entre os 3 datasets. Respostas fundamentadas à missão. Descoberta de padrões ocultos. |
| **Qualidade e variedade das visualizações** | 20% | Mínimo 8 gráficos. Pelo menos 3 tipos diferentes. Títulos, rótulos, legendas. |
| **Storytelling investigativo** | 20% | Narrativa coerente. Evidências visuais. Conclusões defendidas com dados. Apresentação oral. |
| **Organização do código e boas práticas** | 15% | Código limpo. Funções quando apropriado. Notebook autoexplicativo. |

### Bonificações
- **Enriquecimento com dados reais** (integração de fonte pública): **+1.0 ponto**
- Uso criativo de feature engineering: **+0.5 ponto**
- Visualização avançada além do esperado: **+0.5 ponto**
- Análise adicional não solicitada com insights valiosos: **+0.5 ponto**

### Penalizações
- Notebook sem células Markdown explicativas: **-1.0 ponto**
- Gráficos sem título, rótulos ou legendas: **-0.5 ponto por gráfico**
- Código copiado sem adaptação (entre grupos): **nota zero para ambos**
- Entrega após o prazo: **-2.0 pontos por dia**

---

*Prof. Cássio Pinheiro — MBA Ciência de Dados — UNIFOR — 2026*
