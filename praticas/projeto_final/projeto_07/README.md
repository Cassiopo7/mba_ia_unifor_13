# Projeto 07 — Dossiê Exodus: Crise de Talentos e Discriminação

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo B — Analítico Realista (análise + padrões ocultos)

---

## Briefing da Operação

Uma empresa de tecnologia com 1.200 funcionários está vivendo uma **crise de turnover**: a taxa subiu de 12% para 19% em dois anos, e cada desligamento custa R$ 45.000. A VP de Pessoas pediu uma investigação profunda nos dados de RH. Mas há algo mais grave escondido: **denúncias anônimas na pesquisa de clima** sugerem um gestor tóxico em um departamento específico, e a análise de promoções e salários pode revelar um **padrão de discriminação de gênero** sistemática.

Três datasets. Uma crise. Descubra o que está acontecendo.

---

## Datasets Fornecidos

### 1. `data/projeto_07_people_analytics.csv`
Dados de 1.200 funcionários (ativos e desligados).

| Coluna | Descrição |
|--------|-----------|
| `funcionario_id` | Identificador |
| `departamento` | Departamento (Engenharia, Produto, Marketing, Vendas, etc.) |
| `cargo` | Cargo (Júnior, Pleno, Sênior, Coordenador, Gerente) |
| `idade` | Idade |
| `sexo` | Sexo (M/F) |
| `tempo_empresa_meses` | Tempo na empresa (meses) |
| `salario_mensal` | Salário mensal (R$) |
| `satisfacao_trabalho` | Satisfação com o trabalho (1-5) |
| `satisfacao_ambiente` | Satisfação com o ambiente (1-5) |
| `equilibrio_vida_trabalho` | Equilíbrio vida-trabalho (1-5) |
| `promovido_ultimos_2anos` | Se foi promovido nos últimos 2 anos (0/1) |
| `horas_extras_mes` | Horas extras mensais |
| `num_projetos` | Número de projetos |
| `avaliacao_desempenho` | Avaliação de desempenho (1-5) |
| `saiu_da_empresa` | Se saiu da empresa (0/1) |
| `data_admissao` | Data de admissão |
| `data_saida` | Data de saída (se aplicável) |

### 2. `data/projeto_07_pesquisa_clima_anonima.csv`
400 respostas de pesquisa de clima organizacional.

| Coluna | Descrição |
|--------|-----------|
| `resposta_id` | Identificador |
| `data_pesquisa` | Data da pesquisa |
| `departamento` | Departamento |
| `tempo_empresa_faixa` | Faixa de tempo na empresa |
| `sexo` | Sexo |
| `nota_satisfacao_geral` | Nota de satisfação geral (1-5) |
| `nota_lideranca` | Nota da liderança (1-5) |
| `nota_remuneracao` | Nota da remuneração (1-5) |
| `nota_crescimento` | Nota de oportunidades de crescimento (1-5) |
| `recomendaria_empresa` | Se recomendaria a empresa (0/1) |
| `comentario_aberto` | Comentário anônimo (texto livre) |

### 3. `data/projeto_07_historico_promocoes.csv`
600 promoções realizadas nos últimos anos.

| Coluna | Descrição |
|--------|-----------|
| `funcionario_id` | Identificador |
| `sexo` | Sexo |
| `departamento` | Departamento |
| `cargo_anterior` | Cargo antes da promoção |
| `cargo_novo` | Cargo após promoção |
| `data_promocao` | Data da promoção |
| `meses_no_cargo_anterior` | Meses no cargo anterior até a promoção |
| `salario_anterior` | Salário antes da promoção |
| `salario_novo` | Salário após promoção |
| `aumento_percentual` | Aumento percentual |
| `avaliacao_no_momento` | Avaliação de desempenho no momento da promoção |

---

## Missão

Investigue os dados e responda:

1. **Qual departamento tem o turnover mais alto?** Compare a taxa de saída por departamento. Há algum dramaticamente acima da média?
2. **Existe gap salarial de gênero?** Compare salários de homens e mulheres no **mesmo cargo e departamento**. Quantifique a diferença.
3. **Mulheres demoram mais para ser promovidas?** Compare o `meses_no_cargo_anterior` entre homens e mulheres no histórico de promoções.
4. **A pesquisa de clima confirma um gestor tóxico?** Qual departamento tem as piores notas de liderança? Os comentários abertos revelam padrões de assédio ou pressão?
5. **Quais fatores mais influenciam a decisão de sair?** Satisfação, salário, promoção, horas extras — construa uma análise multivariada.
6. **Estime o custo total do turnover** por departamento nos últimos 12 meses (R$ 45.000 por saída).
7. **Proponha um "scorecard de risco de saída"** baseado nos indicadores mais relevantes.

---

## Pistas Iniciais

- O departamento de **Vendas** tem métricas muito piores que os demais — investigue satisfação, clima e turnover
- Compare o **salário médio por cargo** entre homens e mulheres — há uma diferença consistente de ~15%?
- No histórico de promoções, compare **meses_no_cargo_anterior** por sexo — mulheres esperam ~40% mais?
- Os **comentários abertos** da pesquisa de clima do departamento tóxico contêm palavras-chave reveladoras
- Funcionários com **satisfação ≤ 2** e **sem promoção** são os mais propensos a sair

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **CAGED / RAIS** | https://bi.mte.gov.br/bgcaged/ | Dados reais de movimentação de emprego no Brasil |
| **Glassdoor** | https://www.glassdoor.com.br/ | Referência salarial por cargo e setor |

**Perguntas de cruzamento:**
- O gap salarial encontrado é compatível com as estatísticas nacionais de desigualdade de gênero?
- A taxa de turnover do dataset é realista para empresas de tecnologia no Brasil?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Funções para cálculo de taxas e scores, manipulação de strings (comentários), tratamento de nulos |
| **M2 — Pandas/NumPy** | `merge` entre datasets, análise bivariada intensiva, `groupby` com múltiplas agregações, cálculo de proporções e taxas, análise de coorte simplificada |
| **M3 — Visualização** | Countplot com hue, catplot, stacked bars normalizados, boxplots comparativos (M vs. F), heatmaps de correlação, violinplot |

---

## Estrutura do Projeto

```
projeto_07/
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
   - Conclusões: evidências de discriminação, gestor tóxico e plano de retenção

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
