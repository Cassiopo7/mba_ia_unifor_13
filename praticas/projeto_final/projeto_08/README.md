# Projeto 08 — Alerta Epidemiológico: Surto de Diabetes e Falha de Cobertura

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo B — Analítico Realista (análise de saúde pública)

---

## Briefing da Operação

A Secretaria Municipal de Saúde detectou um **aumento preocupante de emergências por complicações de diabetes** em uma região específica da cidade. Ao mesmo tempo, dados clínicos sugerem que existe uma **faixa etária subdiagnosticada** — pessoas com indicadores de risco que ainda não receberam diagnóstico. A investigação inicial aponta para uma **falha de cobertura** em uma das UBS (Unidades Básicas de Saúde).

Três datasets. Um surto. Uma falha sistêmica. Descubra o que está acontecendo.

---

## Datasets Fornecidos

### 1. `data/projeto_08_diabetes_clinico.csv`
Dados clínicos de 2.000 pacientes.

| Coluna | Descrição |
|--------|-----------|
| `paciente_id` | Identificador |
| `idade` | Idade |
| `sexo` | Sexo (M/F) |
| `regiao` | Região da cidade |
| `imc` | Índice de Massa Corporal — **atenção: pode conter valores impossíveis** |
| `atividade_fisica` | Nível de atividade física |
| `historico_familiar_diabetes` | Histórico familiar (0/1) |
| `tabagismo` | Tabagismo (Nunca, Ex-fumante, Fumante) |
| `glicemia_jejum_mgdl` | Glicemia de jejum (mg/dL) |
| `hba1c_pct` | Hemoglobina glicada (%) |
| `pressao_sistolica` | Pressão arterial sistólica |
| `pressao_diastolica` | Pressão arterial diastólica |
| `colesterol_total_mgdl` | Colesterol total (mg/dL) |
| `hdl_mgdl` | HDL (mg/dL) |
| `ldl_mgdl` | LDL (mg/dL) |
| `triglicerideos_mgdl` | Triglicerídeos (mg/dL) |
| `diagnostico_diabetes` | Diagnóstico de diabetes (0/1) |
| `acompanhamento_regular` | Se tem acompanhamento regular (0/1) |
| `dias_desde_ultima_consulta` | Dias desde a última consulta |

### 2. `data/projeto_08_atendimentos_emergencia.csv`
3.500 atendimentos de emergência por complicações de diabetes.

| Coluna | Descrição |
|--------|-----------|
| `atendimento_id` | Identificador |
| `paciente_id` | Identificador do paciente |
| `data_atendimento` | Data do atendimento |
| `regiao` | Região |
| `complicacao` | Complicação (Cetoacidose, Hipoglicemia, Pé Diabético, etc.) |
| `gravidade` | Gravidade (Leve, Moderada, Grave, Crítica) |
| `dias_internacao` | Dias de internação |
| `uti` | Se precisou de UTI (0/1) |
| `desfecho` | Desfecho (Alta, Óbito) |
| `tinha_acompanhamento_previo` | Se tinha acompanhamento prévio (0/1) |

### 3. `data/projeto_08_unidades_saude_cobertura.csv`
Cadastro das UBS e sua capacidade.

| Coluna | Descrição |
|--------|-----------|
| `ubs_id` | Identificador |
| `nome_unidade` | Nome da UBS |
| `regiao` | Região |
| `status` | Status (Ativa, Fechada temporariamente) |
| `data_fechamento` | Data de fechamento (se aplicável) |
| `medicos_disponiveis` | Número de médicos |
| `enfermeiros` | Número de enfermeiros |
| `pacientes_cadastrados` | Pacientes cadastrados |
| `pacientes_diabetes_acompanhados` | Pacientes com diabetes em acompanhamento |
| `consultas_mes_medio` | Consultas por mês (média) |
| `capacidade_maxima_dia` | Capacidade máxima diária |

---

## Missão

Investigue os dados e responda:

1. **Qual região concentra mais emergências graves?** Compare o número e a gravidade de atendimentos de emergência por região. Alguma se destaca?
2. **Pacientes sem acompanhamento regular têm emergências mais graves?** Compare gravidade, dias de internação, UTI e desfecho entre pacientes com e sem acompanhamento.
3. **Existe uma faixa etária subdiagnosticada?** Identifique pacientes **sem diagnóstico** mas com **glicemia de jejum > 126 mg/dL** ou **HbA1c > 6.5%**. Qual a faixa etária predominante?
4. **Alguma UBS tem problema de cobertura?** Cruze a região com mais emergências com o cadastro de UBS. Há alguma fechada ou com capacidade insuficiente?
5. **O fechamento de uma UBS causou o surto?** Analise a evolução temporal das emergências na região afetada — houve aumento após uma data específica?
6. **Quais indicadores clínicos melhor discriminam pacientes diabéticos de não-diabéticos?** Compare distribuições e construa faixas de risco.
7. **Atividade física protege mesmo com IMC elevado?** Compare indicadores clínicos de pacientes ativos vs. sedentários com IMC > 30.

---

## Pistas Iniciais

- A **Zona Oeste** merece atenção especial — compare com as demais regiões
- Procure uma UBS com **status "Fechada temporariamente"** — quando fechou? O que aconteceu depois?
- Pacientes da faixa **40-55 anos** podem ter **glicemia alta sem diagnóstico** — isso é subdiagnóstico
- Compare emergências **com e sem acompanhamento prévio** — a diferença de gravidade é dramática
- Atenção com IMC: há valores impossíveis (0, -1, 999) que precisam de tratamento

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **VIGITEL / Ministério da Saúde** | https://www.gov.br/saude/pt-br/assuntos/vigitel | Prevalência real de diabetes no Brasil por região |
| **DataSUS** | https://datasus.saude.gov.br/ | Morbidade hospitalar por diabetes |

**Perguntas de cruzamento:**
- A prevalência de diabetes no dataset é compatível com a prevalência real no Nordeste?
- Os tipos de complicação mais frequentes estão alinhados com as estatísticas nacionais?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Tratamento de valores impossíveis (IMC), funções para classificação de risco, leitura de múltiplos CSVs |
| **M2 — Pandas/NumPy** | `merge` entre datasets, distribuições comparativas, `groupby` com múltiplas agregações, percentis para faixas de risco, análise temporal |
| **M3 — Visualização** | Histogramas com hue (diabéticos vs. não), violinplot, pairplot colorido por diagnóstico, lineplot temporal, barplots de gravidade, subplots integrados |

---

## Estrutura do Projeto

```
projeto_08/
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
   - Conclusões: causa do surto, subdiagnóstico e recomendações

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
