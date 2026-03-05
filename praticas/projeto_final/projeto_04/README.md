# Projeto 04 — Operação Nota Inflada: Fraude Educacional

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo A — Investigativo (padrões ocultos para descobrir)

---

## Briefing da Operação

A Secretaria de Educação recebeu alertas sobre **possíveis irregularidades nas notas internas** de algumas escolas da rede. O sistema de bonificação premia escolas que atingem metas de desempenho — e há suspeitas de que **certas escolas estejam inflando notas internas** para garantir bônus financeiros, enquanto os resultados nas avaliações externas (SAEB) contam outra história.

Você recebeu três datasets: desempenho individual dos alunos, resultados de avaliações externas e o histórico de metas e bonificações. Descubra quem está fraudando.

---

## Datasets Fornecidos

### 1. `data/projeto_04_desempenho_educacional.csv`
Registros individuais de alunos de 12 escolas (2021-2024).

| Coluna | Descrição |
|--------|-----------|
| `aluno_id` | Identificador do aluno |
| `ano_letivo` | Ano letivo |
| `escola` | Nome da escola |
| `serie` | Série (6º Ano a 3º Médio) |
| `turno` | Manhã ou Tarde |
| `idade` | Idade do aluno |
| `sexo` | Sexo (M/F) |
| `renda_familiar` | Faixa de renda familiar |
| `escolaridade_pais` | Escolaridade dos pais |
| `acesso_internet` | Se tem acesso à internet (0/1) |
| `frequencia_pct` | Frequência escolar (%) |
| `nota_matematica` | Nota em Matemática (0-100) |
| `nota_portugues` | Nota em Português (0-100) |
| `nota_media_geral` | Nota média geral |

### 2. `data/projeto_04_historico_avaliacoes_externas.csv`
Resultados das avaliações externas (SAEB) por escola e série.

| Coluna | Descrição |
|--------|-----------|
| `ano` | Ano da avaliação |
| `escola` | Nome da escola |
| `serie_avaliada` | Série avaliada (5º Ano, 9º Ano, 3º Médio) |
| `nota_saeb_matematica` | Nota SAEB em Matemática |
| `nota_saeb_portugues` | Nota SAEB em Português |
| `nota_interna_media_matematica` | Nota interna média em Matemática |
| `nota_interna_media_portugues` | Nota interna média em Português |
| `numero_alunos_avaliados` | Número de alunos avaliados |
| `taxa_participacao_pct` | Taxa de participação (%) |

### 3. `data/projeto_04_metas_bonificacao.csv`
Histórico de metas e bonificações por escola.

| Coluna | Descrição |
|--------|-----------|
| `ano` | Ano |
| `escola` | Nome da escola |
| `meta_nota_media` | Meta de nota média estabelecida |
| `nota_media_alcancada` | Nota média efetivamente alcançada |
| `meta_atingida` | Se a meta foi atingida (True/False) |
| `valor_bonificacao_reais` | Valor da bonificação recebida (R$) |
| `ranking_rede` | Posição no ranking da rede |

---

## Missão

Investigue os dados e responda:

1. **Existe um gap entre notas internas e notas externas (SAEB)?** Compare a nota média interna com a nota SAEB por escola. Quais escolas têm a maior discrepância?
2. **A distribuição de notas internas é "perfeita demais" em alguma escola?** Compare a variância/desvio-padrão das notas entre escolas. Há escolas com variância suspeitamente baixa?
3. **Houve salto repentino de notas em algum ano específico?** Analise a evolução temporal das notas internas — há escolas com melhora súbita incompatível com as externas?
4. **As escolas suspeitas são consistentemente as que atingem metas e recebem bonificação?** Cruze com o dataset de metas. Sempre atingem a meta, apesar do SAEB baixo?
5. **Os fatores socioeconômicos explicam o desempenho?** Escolas com alunos de renda mais alta têm notas melhores? As escolas suspeitas têm perfil socioeconômico que justifique notas tão altas?
6. **Construa a evidência visual:** Compare, lado a lado, notas internas vs. SAEB das escolas suspeitas vs. demais.

---

## Pistas Iniciais

- Compare escolas onde a **nota interna média é 15-25 pontos acima da nota SAEB** — isso é normal ou irregular?
- Olhe o **desvio-padrão das notas** por escola: escolas legítimas têm variação natural; escolas com fraude podem ter notas "agrupadas demais"
- O ano de **2023** merece atenção especial — houve um pico de notas em algumas escolas
- Cruze as escolas que **sempre atingem a meta** com as que têm **piores notas no SAEB** — a contradição é a evidência
- Procure escolas cujo nome começa com letras gregas específicas

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **INEP / Microdados SAEB** | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados | Notas reais do SAEB para referência |
| **QEdu** | https://qedu.org.br/ | Indicadores educacionais por escola e município |

**Perguntas de cruzamento:**
- As notas SAEB do dataset estão na faixa realista para escolas do Nordeste?
- Qual é o gap médio real entre notas internas e externas em escolas públicas brasileiras?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Funções para cálculo de gaps e scores, manipulação de dados categóricos, tratamento de nulos |
| **M2 — Pandas/NumPy** | `merge` entre datasets, `groupby` com `agg` (média, std, count), `pivot_table`, detecção de duplicatas, cálculo de variância e desvio-padrão |
| **M3 — Visualização** | Distribuições com histogramas e KDE, pairplot, boxenplot, heatmaps de correlação, barplots comparativos (interno vs. externo), lineplot de evolução temporal |

---

## Estrutura do Projeto

```
projeto_04/
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
   - Conclusões: quais escolas estão fraudando e como provar

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
