# Projeto 06 — Operação Curto-Circuito: Furto de Energia + Apagão

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo B — Analítico Realista (semi-investigativo)

---

## Briefing da Operação

Uma concessionária de energia elétrica do Ceará está enfrentando **perdas não-técnicas crescentes** (furto de energia) e um **aumento de ocorrências de queda de energia** concentrado em um bairro específico. A engenharia suspeita que os dois problemas estão conectados: o furto estaria sobrecarregando a infraestrutura local, causando os apagões.

Você recebeu dados de consumo de 5.000 unidades consumidoras, registro de ocorrências na rede e o cadastro de transformadores. Descubra onde está o problema.

---

## Datasets Fornecidos

### 1. `data/projeto_06_consumo_energia.csv`
Consumo mensal de 5.000 unidades consumidoras (2023-2024).

| Coluna | Descrição |
|--------|-----------|
| `uc_id` | Identificador da unidade consumidora |
| `classe` | Classe (Residencial, Comercial, Industrial) |
| `bairro` | Bairro |
| `ano` | Ano |
| `mes` | Mês |
| `consumo_kwh` | Consumo mensal (kWh) |
| `temperatura_media_c` | Temperatura média do mês (°C) |

### 2. `data/projeto_06_ocorrencias_rede.csv`
Registro de ocorrências na rede elétrica.

| Coluna | Descrição |
|--------|-----------|
| `ocorrencia_id` | Identificador da ocorrência |
| `data_ocorrencia` | Data da ocorrência |
| `bairro` | Bairro afetado |
| `tipo_ocorrencia` | Tipo (Queda de energia, Flutuação, Curto-circuito, Furto, etc.) |
| `transformador_id` | Transformador associado |
| `duracao_horas` | Duração da interrupção (horas) |
| `ucs_afetadas` | Número de UCs afetadas |
| `causa_provavel` | Causa provável (Sobrecarga, Falha, Clima, etc.) |

### 3. `data/projeto_06_cadastro_transformadores.csv`
Cadastro dos 50 transformadores da concessionária.

| Coluna | Descrição |
|--------|-----------|
| `transformador_id` | Identificador |
| `bairro` | Bairro |
| `capacidade_kva` | Capacidade (kVA) |
| `ucs_conectadas` | Número de UCs conectadas |
| `ano_instalacao` | Ano de instalação |
| `ultima_manutencao` | Data da última manutenção |
| `status` | Status operacional |

---

## Missão

Investigue os dados e responda:

1. **Quais unidades consumidoras apresentam queda abrupta de consumo?** Identifique UCs cujo consumo caiu 80-90% de um mês para o outro. Quando isso aconteceu e em qual bairro?
2. **As UCs com queda abrupta estão concentradas geograficamente?** Há um bairro que concentra essas anomalias?
3. **Existe correlação entre as anomalias de consumo e o aumento de ocorrências na rede?** Cruze os dois datasets por bairro e período.
4. **Qual transformador está sobrecarregado?** Identifique transformadores com número de UCs conectadas muito acima de sua capacidade.
5. **O surto de ocorrências está ligado à sobrecarga?** O transformador sobrecarregado é o mesmo associado às ocorrências frequentes?
6. **Estime o prejuízo** da concessionária com o furto: quanto de energia está sendo "desviada" por mês?

---

## Pistas Iniciais

- Filtre UCs com **consumo < 30 kWh** a partir de **julho/2024** que antes consumiam > 150 kWh
- O bairro **Barra do Ceará** concentra anomalias — investigue
- O transformador **T-023** aparece com frequência nas ocorrências — cruze com o cadastro
- Compare a **capacidade (kVA)** do transformador com o **número de UCs conectadas** — há sobrecarga?
- As ocorrências do tipo **"Sobrecarga"** aumentaram no 2º semestre de 2024

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **ANEEL Dados Abertos** | https://dadosabertos.aneel.gov.br/ | Dados de consumo, perdas e indicadores de qualidade |
| **ONS** | https://www.ons.org.br/paginas/sobre-o-ons/procedimentos-de-rede/dados-abertos | Carga de energia por subsistema |

**Perguntas de cruzamento:**
- O consumo médio residencial do dataset é compatível com a média real do Ceará?
- A taxa de perdas não-técnicas estimada está dentro da faixa reportada pela ANEEL para o Nordeste?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Funções para detecção de anomalias, cálculos de variação percentual, tratamento de nulos |
| **M2 — Pandas/NumPy** | `merge` entre datasets, segmentação com `cut`/`qcut`, detecção de anomalias (Z-score, variação %), `groupby` por bairro/mês, cálculos de razão capacidade/carga |
| **M3 — Visualização** | Heatmaps temporais (consumo por mês), boxplots mensais, lineplot de séries temporais (antes/depois), barplots de ocorrências, scatter de capacidade vs. carga |

---

## Estrutura do Projeto

```
projeto_06/
├── README.md          ← Este arquivo
├── data/              ← 3 datasets do projeto
├── notebooks/         ← Notebook(s) Jupyter com a investigação
├── scripts/           ← Scripts Python auxiliares (se necessário)
└── docs/              ← Documentação adicional, apresentação
```

## Entregáveis

1. **Notebook Python (.ipynb)** em `notebooks/` contendo:
   - Importação e inspeção dos 3 datasets
   - Limpeza e transformação (nulos, tipos, duplicatas, outliers)
   - Cruzamento entre datasets (merge/join)
   - Análise investigativa com estatísticas descritivas
   - Mínimo de **8 visualizações** (mix de Matplotlib e Seaborn)
   - Respostas à missão com **evidências nos dados**
   - Células Markdown narrando a investigação (storytelling)
   - Conclusões: onde está o furto, qual o impacto e como resolver

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
