# Projeto Final — Datathon Investigativo

## MBA em Ciência de Dados | UNIFOR | Turma 13

**Professor:** Cássio Pinheiro
**Formato:** Datathon Investigativo — Operações com Dados
**Entrega:** Última aula da disciplina
**Trabalho:** Em duplas ou trios (formação livre)

---

## Visão Geral

O Projeto Final é um **Datathon Investigativo**: cada grupo recebe uma **operação** — um cenário realista onde dados escondem padrões, fraudes, anomalias ou crises que precisam ser descobertas. O objetivo é consolidar os três módulos da disciplina — Python, Pandas/NumPy e Visualização/EDA — em uma investigação analítica que demonstre capacidade de cruzar dados, levantar hipóteses e defender conclusões com evidências.

Diferente de uma análise exploratória convencional, aqui os dados **mentem, omitem ou escondem a verdade**. O aluno deve agir como um **investigador de dados**, cruzando múltiplas fontes para montar o quebra-cabeça.

### Formato Híbrido: Dados Gerados + Dados Reais

Cada projeto trabalha com **duas camadas de dados**:

1. **Dados fornecidos (3 CSVs por projeto)** — Datasets gerados com padrões ocultos plantados. Estes são a base da investigação.
2. **Dados reais complementares (obrigatório)** — Cada projeto indica 2-3 fontes públicas onde os alunos **devem** buscar dados reais para enriquecer, validar ou confrontar suas análises.

Essa abordagem espelha o trabalho real de um cientista de dados: raramente uma única fonte conta toda a história.

---

## Estrutura dos Projetos

Cada projeto contém:

1. **Nome da Operação** — Codinome e briefing investigativo
2. **3 Datasets fornecidos** — CSVs com descrição das colunas e padrões a investigar
3. **Missão** — 5-7 perguntas investigativas que guiam a descoberta
4. **Pistas iniciais** — Dicas sutis para direcionar sem entregar a resposta
5. **Desafio de dados reais** — Fontes públicas + perguntas de cruzamento
6. **Técnicas esperadas** — Alinhadas com os Módulos 1-3 da disciplina
7. **Entregáveis e avaliação** — Rubrica detalhada

---

## Os 10 Projetos

### Grupo A — Investigativos (padrões ocultos para descobrir)

| # | Operação | Tema | Perfil Ideal |
|---|----------|------|-------------|
| 01 | **Operação Bisturi** | Auditoria de Fraude Hospitalar | Saúde / Gestão Hospitalar |
| 02 | **Operação Marketplace** | Fraude em E-commerce | Administração / Gestão Comercial |
| 04 | **Operação Nota Inflada** | Fraude Educacional | Educação / Gestão Escolar |
| 05 | **Operação Frota Fantasma** | Desvio em Manutenção | Engenharia / Logística / Operações |
| 09 | **Operação Lava-Imóvel** | Lavagem de Dinheiro Imobiliário | Eng. Civil / Investidores / Finanças |

### Grupo B — Analíticos Realistas (investigação de negócio profunda)

| # | Operação | Tema | Perfil Ideal |
|---|----------|------|-------------|
| 03 | **Alerta Vermelho** | Crise Ambiental Misteriosa | Eng. Ambiental / Saúde Pública |
| 06 | **Operação Curto-Circuito** | Furto de Energia + Apagão | Eng. Elétrica / Sustentabilidade |
| 07 | **Dossiê Exodus** | Crise de Talentos e Discriminação | Gestão de Pessoas / Administração |
| 08 | **Alerta Epidemiológico** | Surto de Diabetes e Falha de Cobertura | Medicina / Saúde Pública |
| 10 | **Radiografia Municipal** | Desvio de Dinheiro Público | Gestão Pública / Economia / Pesquisa |

---

## Entregáveis (comum a todos os projetos)

Cada grupo deve entregar:

- **Notebook Python (.ipynb)** com toda a investigação, contendo:
  - Importação e inspeção inicial dos 3 datasets
  - Limpeza e transformação (tratamento de nulos, tipos, duplicatas, outliers)
  - **Cruzamento entre os 3 datasets** (merge/join) para construir a narrativa investigativa
  - Análise exploratória com estatísticas descritivas
  - Mínimo de **8 visualizações** (mix de Matplotlib e Seaborn)
  - Respostas às perguntas da missão com **evidências nos dados**
  - Integração com pelo menos **1 fonte de dados reais** (bônus)
  - Células Markdown explicando cada etapa (storytelling investigativo)
- **Apresentação oral** (5-7 minutos) contando a história da investigação
- **Relatório final** com conclusões, evidências e recomendações

---

## Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Qualidade da limpeza e transformação dos dados | 20% |
| Profundidade da investigação e cruzamento entre datasets | 25% |
| Qualidade e variedade das visualizações | 20% |
| Storytelling investigativo e clareza nas conclusões | 20% |
| Organização do código e boas práticas | 15% |

### Bonificações

| Bonificação | Valor |
|-------------|-------|
| **Enriquecimento com dados reais** — Integração de pelo menos 1 fonte pública real que agregue valor à análise | **+1.0 ponto** |
| Uso criativo de feature engineering (variáveis derivadas relevantes) | +0.5 ponto |
| Visualização avançada além do esperado (dashboard integrado, gráficos interativos) | +0.5 ponto |
| Análise adicional não solicitada que gere insights valiosos | +0.5 ponto |

*Máximo de bonificação: +2.5 pontos*

### Penalizações

- Notebook sem células Markdown explicativas: **-1.0 ponto**
- Gráficos sem título, rótulos ou legendas: **-0.5 ponto por gráfico**
- Código copiado sem adaptação (entre grupos): **nota zero para ambos**
- Entrega após o prazo: **-2.0 pontos por dia**

### Escala de Notas

| Nota | Descrição |
|------|-----------|
| **10** | Excepcional — investigação completa, padrões ocultos descobertos, dados reais integrados, storytelling envolvente |
| **8-9** | Muito bom — todos os critérios atendidos com qualidade, boa investigação, pequenas melhorias possíveis |
| **6-7** | Satisfatório — atende aos requisitos mínimos, investigação superficial em alguns pontos |
| **4-5** | Insuficiente — falhas significativas na investigação, limpeza ou visualizações |
| **0-3** | Inadequado — entrega incompleta ou sem evidência de esforço investigativo |

---

## Orientações Finais

### Sobre os Datasets
Cada projeto possui **3 datasets** na pasta `data/` do projeto. Todos os CSVs possuem cabeçalho e estão codificados em UTF-8. Os datasets possuem **problemas intencionais** (valores nulos, tipos incorretos, duplicatas, outliers, valores impossíveis) para que os alunos pratiquem limpeza de dados. **A verdade está no cruzamento** — nenhum dataset isolado conta a história completa.

### Sobre os Dados Reais
Cada README indica fontes de dados públicos onde os alunos devem buscar dados complementares. O objetivo é **enriquecer a análise** com contexto real: comparar valores com referências de mercado, validar padrões encontrados, ou cruzar com indicadores oficiais. Não é esperado que os dados reais sejam perfeitos ou completos — o processo de busca e integração já é parte do aprendizado.

### Sobre a Apresentação
Cada grupo terá **5 a 7 minutos** para apresentar. A apresentação deve contar a **história da investigação** — não é uma mera sequência de gráficos. Estrutura sugerida: (1) O que sabíamos no início, (2) O que os dados revelaram, (3) As evidências encontradas, (4) Conclusões e recomendações.

### Sobre o Código
O notebook deve ser **autoexplicativo** — alguém que não assistiu à apresentação deve conseguir entender a investigação lendo o notebook. Use células Markdown para narrar cada etapa da descoberta.

### Dicas

1. Comecem pela **inspeção** dos 3 datasets (`shape`, `dtypes`, `describe`, `info`, `head`)
2. Façam a **limpeza** antes de qualquer análise
3. **Cruzem os datasets** — a resposta quase nunca está em um único CSV
4. Sigam as **pistas iniciais** do README — elas apontam a direção certa
5. Usem pelo menos **3 tipos diferentes** de gráfico
6. Não ignorem **outliers** — nesta investigação, eles podem ser a evidência
7. A **conclusão** é tão importante quanto a análise — defendam suas descobertas

---

*Boas investigações e boas descobertas nos dados!*

**Prof. Cássio Pinheiro**
MBA em Ciência de Dados — UNIFOR — 2026
