# Projeto 01 — Operação Bisturi: Auditoria de Fraude Hospitalar

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo A — Investigativo (padrões ocultos para descobrir)

---

## Briefing da Operação

A Controladoria-Geral do Estado recebeu denúncias anônimas sobre possíveis fraudes em unidades hospitalares da rede pública do Nordeste. Há suspeitas de **superfaturamento de procedimentos**, **pacientes fantasma** e **internações fictícias**. Você foi convocado como analista de dados para auditar 15 unidades hospitalares nos últimos 3 anos e identificar quais unidades apresentam padrões incompatíveis com a operação legítima.

Os dados brutos estão nos sistemas — agora é preciso cruzá-los para encontrar as evidências.

---

## Datasets Fornecidos

### 1. `data/projeto_01_indicadores_hospitalares.csv`
Indicadores operacionais mensais de 15 unidades hospitalares (2022-2024).

| Coluna | Descrição |
|--------|-----------|
| `ano`, `mes` | Período de referência |
| `unidade` | Nome do hospital |
| `especialidade` | Especialidade médica |
| `leitos_disponiveis` | Quantidade de leitos disponíveis |
| `taxa_ocupacao` | Taxa de ocupação (0 a 1) |
| `internacoes` | Número de internações no período |
| `tempo_medio_internacao_dias` | Tempo médio de internação |
| `taxa_reinternacao_30d` | Taxa de reinternação em 30 dias |
| `obitos` | Número de óbitos |
| `custo_medio_internacao` | Custo médio por internação (R$) |
| `faixa_etaria_predominante` | Faixa etária predominante |
| `tipo_internacao` | Urgência ou Eletiva |

### 2. `data/projeto_01_registro_procedimentos.csv`
Registro individual de 12.000+ procedimentos realizados.

| Coluna | Descrição |
|--------|-----------|
| `procedimento_id` | Identificador único do procedimento |
| `unidade` | Hospital onde foi realizado |
| `paciente_id` | Identificador do paciente |
| `data_procedimento` | Data de realização |
| `tipo_procedimento` | Tipo (Consulta, Exame, Cirurgia, etc.) |
| `valor_cobrado` | Valor cobrado pelo procedimento (R$) |
| `convenio` | Convênio (SUS, Plano A, Plano B, Particular) |

### 3. `data/projeto_01_denuncias_anonimas.csv`
Relatos recebidos pela Ouvidoria.

| Coluna | Descrição |
|--------|-----------|
| `denuncia_id` | Identificador da denúncia |
| `data_denuncia` | Data do registro |
| `unidade_mencionada` | Hospital mencionado |
| `canal` | Canal de recebimento |
| `relato_resumido` | Resumo do relato |
| `classificacao` | Classificação (Fraude, Outros) |
| `status` | Status da denúncia |

---

## Missão

Investigue os dados e responda:

1. **Quais unidades apresentam relação incompatível entre número de leitos e volume de internações?** Compare a razão internações/leitos entre todos os hospitais. Quais fogem do padrão?
2. **Existem procedimentos duplicados** (mesmo paciente, mesma data, mesmo procedimento)? Em quais unidades isso se concentra?
3. **Os custos médios de internação e procedimentos são compatíveis** com a referência das demais unidades? Quais hospitais cobram significativamente mais?
4. **Existe sazonalidade suspeita no faturamento?** Há meses com picos de internações ou custos que coincidem com fechamento de metas ou final de exercício?
5. **O que as denúncias revelam?** Cruze os relatos da ouvidoria com os padrões encontrados nos dados operacionais. As denúncias são corroboradas pelos números?
6. **Monte o dossiê:** Identifique as unidades suspeitas e construa uma narrativa visual com as evidências encontradas.

---

## Pistas Iniciais

- Comece comparando a **razão internações por leito** entre todas as unidades — há hospitais com poucos leitos mas muitas internações?
- Procure **procedimentos com mesmo paciente_id + mesma data** no registro de procedimentos
- Compare os **custos médios** por tipo de procedimento: há hospitais onde o mesmo procedimento custa muito mais?
- Olhe os **meses de março e setembro** com atenção especial
- As denúncias mencionam nomes de hospitais — cruze com os dados quantitativos

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **DataSUS / TabNet** | https://datasus.saude.gov.br/transferencia-de-arquivos/ | Dados reais de internações SUS para comparar custos e taxas |
| **CNES** | https://cnes.datasus.gov.br/ | Cadastro de hospitais reais: leitos, especialidades, equipamentos |

**Perguntas de cruzamento:**
- Os custos médios do dataset estão compatíveis com os valores reais do SUS na região Nordeste?
- A taxa de ocupação das unidades é realista comparada aos dados do CNES?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Leitura de múltiplos CSVs, funções para cálculo de indicadores, tratamento de erros |
| **M2 — Pandas/NumPy** | `merge` entre datasets, `groupby` multi-nível, `pivot_table`, detecção de duplicatas com `duplicated`, cálculos de razões e proporções |
| **M3 — Visualização** | Heatmaps de correlação, boxplots comparativos por unidade, lineplots temporais (evolução mensal), barplots de custos, subplots integrados |

---

## Estrutura do Projeto

```
projeto_01/
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
   - Conclusões: quais unidades são suspeitas e por quê

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
