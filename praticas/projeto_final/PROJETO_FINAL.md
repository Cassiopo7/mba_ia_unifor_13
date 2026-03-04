# Projeto Final — Programação para Ciência de Dados

## MBA em Ciência de Dados | UNIFOR | Turma 13

**Professor:** Cássio Pinheiro
**Formato:** Datathon Aplicado
**Entrega:** Última aula da disciplina
**Trabalho:** Em duplas ou trios (formação livre)

---

## Visão Geral

O Projeto Final é um **Datathon aplicado**: cada grupo recebe um case de negócio real, com dataset(s) reais e um conjunto de perguntas que simulam demandas analíticas do mundo corporativo. O objetivo é consolidar os três módulos da disciplina — Python, Pandas/NumPy e Visualização/EDA — em uma entrega que demonstre capacidade analítica, storytelling com dados e domínio técnico.

Inspirado no formato de Datathons profissionais, cada projeto coloca o aluno no papel de **analista de dados** contratado para investigar um problema real e entregar insights acionáveis.

---

## Estrutura dos Projetos

Cada projeto contém:

1. **Contexto de negócio** — Descrição do cenário e da organização
2. **Dataset(s)** — Bases de dados reais (CSV) para análise
3. **Perguntas de negócio** — 5 a 7 perguntas que guiam a investigação
4. **Entregáveis obrigatórios** — O que deve ser entregue

---

## Entregáveis (comum a todos os projetos)

Cada grupo deve entregar:

- **Notebook Python (.ipynb)** com toda a análise, contendo:
  - Importação e inspeção inicial dos dados
  - Limpeza e transformação (tratamento de nulos, tipos, duplicatas)
  - Análise exploratória com estatísticas descritivas
  - Mínimo de **8 visualizações** (mix de Matplotlib e Seaborn)
  - Respostas às perguntas de negócio com evidências nos dados
  - Células Markdown explicando cada etapa (storytelling)
- **Apresentação oral** (5-7 minutos) contando a história dos dados
- **Conclusões e recomendações** escritas no notebook

### Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Qualidade da limpeza e transformação dos dados | 20% |
| Profundidade da análise exploratória | 25% |
| Qualidade e variedade das visualizações | 20% |
| Storytelling e clareza nas conclusões | 20% |
| Organização do código e boas práticas | 15% |

---

## Os 10 Projetos

---

### Projeto 1 — Análise de Indicadores Hospitalares

**Perfil:** Saúde / Gestão Hospitalar
**Dataset:** `projeto_01_indicadores_hospitalares.csv`
**Fonte inspiradora:** Dados do DataSUS / CNES (adaptados)

**Contexto:** Você foi contratado como analista de dados por uma rede hospitalar do Nordeste que deseja entender o desempenho operacional de suas 15 unidades nos últimos 3 anos. A diretoria precisa de evidências para decidir onde investir, quais unidades precisam de intervenção e como otimizar a taxa de ocupação de leitos.

**Perguntas de Negócio:**

1. Qual é a taxa média de ocupação de leitos por unidade e como ela evoluiu trimestralmente? Há unidades consistentemente acima ou abaixo da média?
2. Existe correlação entre o tempo médio de internação e a taxa de reinternação em 30 dias? O que isso sugere sobre a qualidade da alta?
3. Quais especialidades médicas apresentam maior variação sazonal na demanda? Como isso pode orientar o planejamento de escala?
4. A taxa de mortalidade hospitalar varia significativamente entre unidades de mesmo porte? Quais fatores operacionais parecem associados?
5. Qual é o perfil dos pacientes (faixa etária, tipo de internação) que mais contribuem para a superlotação?
6. Construa um dashboard analítico (visualizações integradas) que a diretoria possa usar para monitoramento mensal.

**Técnicas esperadas:** groupby multi-nível, pivot_table, visualizações temporais (lineplot), heatmaps de correlação, boxplots comparativos, tratamento de outliers em tempos de internação.

---

### Projeto 2 — Performance de Vendas no E-commerce

**Perfil:** Administração / Gestão Comercial
**Dataset:** `projeto_02_ecommerce_vendas.csv`
**Fonte inspiradora:** Brazilian E-Commerce (Olist) / dados simulados

**Contexto:** Uma empresa de e-commerce cearense que vende produtos de moda, eletrônicos e casa & decoração precisa entender seu desempenho de vendas dos últimos 2 anos. O CEO quer identificar padrões de compra, sazonalidade e oportunidades de crescimento antes de uma rodada de investimento.

**Perguntas de Negócio:**

1. Qual é a evolução mensal do faturamento e do ticket médio? Há tendência de crescimento ou estagnação?
2. Quais categorias de produto concentram maior receita vs. maior volume de pedidos? Existe um "Pareto" (80/20)?
3. Como se distribui a base de clientes por região (estado)? Há concentração geográfica que represente risco?
4. Qual é a taxa de cancelamento de pedidos por categoria e por faixa de valor? O que pode estar causando cancelamentos em faixas específicas?
5. Existe diferença significativa no comportamento de compra entre dias da semana e finais de semana? E entre turnos do dia?
6. Quais são os 10 produtos com maior taxa de avaliação negativa (nota ≤ 2)? Há padrões em comum?
7. Projete um painel de indicadores-chave (KPIs) que o CEO possa acompanhar semanalmente.

**Técnicas esperadas:** análise temporal com resample, crosstab, value_counts normalizado, análise de Pareto, gráficos de barras empilhados, scatter com regressão, subplots organizados.

---

### Projeto 3 — Qualidade do Ar e Saúde Pública

**Perfil:** Engenharia Ambiental / Saúde Pública
**Dataset:** `projeto_03_qualidade_ar.csv`
**Fonte inspiradora:** Dados de estações de monitoramento (CETESB / OpenAQ adaptados)

**Contexto:** A Secretaria de Meio Ambiente de uma capital nordestina instalou 8 estações de monitoramento de qualidade do ar. Após 2 anos de coleta, precisa de uma análise que demonstre padrões de poluição, identifique zonas críticas e embase a criação de políticas públicas para redução de emissões.

**Perguntas de Negócio:**

1. Quais estações apresentam concentrações médias de MP2.5 e MP10 acima dos limites recomendados pela OMS? Com que frequência isso ocorre?
2. Existe padrão sazonal na qualidade do ar? Meses de seca vs. chuva apresentam diferenças significativas?
3. Qual é o horário do dia com maior concentração de poluentes? Isso coincide com horários de pico de trânsito?
4. Há correlação entre os diferentes poluentes (MP2.5, MP10, O3, NO2, SO2)? O que isso sugere sobre as fontes de emissão?
5. As estações próximas a zonas industriais apresentam padrões distintos das estações em áreas residenciais?
6. Construa um índice composto de qualidade do ar (baseado nos poluentes disponíveis) e classifique cada estação/período.

**Técnicas esperadas:** merge de datasets, análise temporal por hora/dia/mês, heatmaps calendário, violinplots, cálculo de percentis, criação de features derivadas, FacetGrid do Seaborn.

---

### Projeto 4 — Análise de Desempenho Educacional

**Perfil:** Educação / Gestão Escolar
**Dataset:** `projeto_04_desempenho_educacional.csv`
**Fonte inspiradora:** Microdados INEP / SAEB (adaptados)

**Contexto:** Uma rede de escolas com 12 unidades (fundamental e médio) precisa entender os fatores que influenciam o desempenho dos alunos nas avaliações padronizadas. A coordenação pedagógica quer evidências para direcionar intervenções e reduzir a evasão escolar.

**Perguntas de Negócio:**

1. Qual é a distribuição de notas por escola e por série? Há escolas que se destacam positiva ou negativamente?
2. Existe diferença significativa de desempenho entre turnos (manhã vs. tarde) e entre níveis (fundamental vs. médio)?
3. A frequência escolar (% de presença) tem relação mensurável com o desempenho nas avaliações? Qual é o limiar crítico?
4. Quais fatores socioeconômicos (renda familiar, escolaridade dos pais, acesso à internet) apresentam maior correlação com o desempenho?
5. Qual é o perfil dos alunos em risco de evasão (frequência < 75%)? Existem padrões demográficos ou acadêmicos que os identifiquem?
6. Compare o desempenho em Matemática vs. Língua Portuguesa: as deficiências são correlacionadas ou independentes?

**Técnicas esperadas:** distribuições com histogramas e KDE, pairplot, correlações com heatmap, segmentação por múltiplas variáveis, boxenplot, análise de frequência relativa, tratamento de dados categóricos.

---

### Projeto 5 — Gestão de Frota e Manutenção Veicular

**Perfil:** Engenharia / Logística / Gestão de Operações
**Dataset:** `projeto_05_frota_manutencao.csv`
**Fonte inspiradora:** Dados operacionais de frotas (simulados com base em padrões reais)

**Contexto:** Uma empresa de logística com frota de 200 veículos (caminhões e vans) precisa otimizar seus custos de manutenção. Nos últimos 18 meses, os gastos com manutenção corretiva subiram 35%. A gerência de operações precisa entender o que está acontecendo e propor um plano de manutenção preventiva baseado em dados.

**Perguntas de Negócio:**

1. Qual é a distribuição dos custos de manutenção por tipo (preventiva vs. corretiva) e por categoria de veículo? A proporção mudou ao longo do tempo?
2. Quais componentes/sistemas (motor, freios, suspensão, elétrica) concentram maior custo e maior frequência de falhas?
3. Existe relação entre a quilometragem acumulada e a frequência de manutenções corretivas? Qual é o ponto crítico de km?
4. A idade do veículo é um preditor melhor que a quilometragem para antecipar falhas? Construa uma análise comparativa.
5. Quais veículos específicos são "outliers" em custo de manutenção? Seria mais econômico substituí-los?
6. Proponha faixas de km/tempo para manutenção preventiva por componente, baseado nos padrões encontrados nos dados.

**Técnicas esperadas:** análise de custos com groupby, scatter com anotações, detecção de outliers (IQR e Z-score), análise de sobrevivência simplificada, gráficos de Pareto, cumsum para custos acumulados.

---

### Projeto 6 — Análise de Consumo de Energia Elétrica

**Perfil:** Engenharia Elétrica / Sustentabilidade / Gestão Empresarial
**Dataset:** `projeto_06_consumo_energia.csv`
**Fonte inspiradora:** Dados EPE / ANEEL (adaptados)

**Contexto:** Uma concessionária de energia elétrica do Ceará precisa analisar o padrão de consumo de 5.000 unidades consumidoras (residenciais, comerciais e industriais) ao longo de 24 meses. O objetivo é identificar perfis de consumo, detectar anomalias que possam indicar fraude ou erro de medição, e projetar a demanda futura.

**Perguntas de Negócio:**

1. Qual é o perfil médio de consumo por classe (residencial, comercial, industrial) e como ele varia ao longo dos meses?
2. Existe sazonalidade clara no consumo? Quais meses são pico e quais são vale para cada classe?
3. Quais unidades consumidoras apresentam variações abruptas de consumo (possíveis anomalias)? Defina critérios estatísticos para flagging.
4. Há correlação entre o consumo de energia e variáveis climáticas (temperatura média) disponíveis no dataset?
5. Qual é a concentração de consumo? Os 10% maiores consumidores representam que percentual do consumo total?
6. Segmente os consumidores residenciais em 3-4 perfis com base no padrão de consumo mensal. Descreva cada perfil.

**Técnicas esperadas:** segmentação manual com cut/qcut, detecção de anomalias (Z-score, IQR), análise de concentração (curva de Lorenz simplificada), heatmaps temporais, boxplots mensais, merge com dados climáticos.

---

### Projeto 7 — Análise de Dados de RH — People Analytics

**Perfil:** Gestão de Pessoas / Administração / Gestores
**Dataset:** `projeto_07_people_analytics.csv`
**Fonte inspiradora:** IBM HR Analytics / dados corporativos simulados

**Contexto:** O departamento de RH de uma empresa de tecnologia com 1.200 funcionários precisa entender os fatores que influenciam a rotatividade (turnover). Nos últimos 2 anos, a taxa de turnover subiu de 12% para 19%, e o custo estimado de cada desligamento é de R$ 45.000. A VP de Pessoas precisa de evidências para fundamentar uma nova política de retenção.

**Perguntas de Negócio:**

1. Qual é o perfil dos funcionários que pedem demissão vs. os que permanecem? (idade, tempo de empresa, cargo, departamento, salário)
2. Existe um "período crítico" de tempo de empresa em que a probabilidade de saída é maior?
3. O nível de satisfação com o trabalho, ambiente e equilíbrio vida-trabalho tem correlação mensurável com o turnover?
4. Funcionários que receberam promoção nos últimos 2 anos apresentam taxa de turnover significativamente menor?
5. Quais departamentos concentram maior rotatividade? O salário médio do departamento explica essa diferença?
6. Estime o custo total do turnover por departamento nos últimos 12 meses e identifique onde a intervenção teria maior ROI.
7. Construa um "scorecard de risco de saída" baseado nos indicadores mais relevantes encontrados na análise.

**Técnicas esperadas:** análise bivariada intensiva, countplot com hue, catplot, cálculo de taxas e proporções, análise de coorte simplificada, stacked bars normalizados, correlação ponto-bisserial (variável binária vs. contínua).

---

### Projeto 8 — Análise de Dados Clínicos — Diabetes

**Perfil:** Saúde / Medicina / Gestão Hospitalar
**Dataset:** `projeto_08_diabetes_clinico.csv`
**Fonte inspiradora:** Pima Indians Diabetes Database / dados clínicos simulados

**Contexto:** Uma clínica especializada em endocrinologia atende 2.000 pacientes em acompanhamento para prevenção e tratamento de diabetes tipo 2. A equipe médica precisa entender quais fatores clínicos e de estilo de vida estão mais associados ao desenvolvimento da doença, para criar protocolos de triagem mais eficientes e programas de prevenção direcionados.

**Perguntas de Negócio:**

1. Qual é a prevalência de diabetes na base e como ela se distribui por faixa etária, sexo e IMC?
2. Quais indicadores clínicos (glicemia de jejum, HbA1c, pressão arterial, colesterol, triglicerídeos) apresentam maior diferença entre pacientes diabéticos e não-diabéticos?
3. O IMC é o melhor preditor isolado de diabetes ou existem indicadores mais discriminantes? Construa uma análise comparativa.
4. Existem pacientes com indicadores clínicos de risco que ainda não foram diagnosticados? (possíveis subdiagnosticados)
5. Há diferença no perfil de risco entre homens e mulheres? A idade de onset é similar?
6. Pacientes que praticam atividade física regular apresentam indicadores clínicos significativamente melhores, mesmo com IMC elevado?
7. Proponha faixas de risco (baixo/médio/alto) baseadas nos indicadores que mais discriminam, com evidência visual.

**Técnicas esperadas:** distribuições comparativas (histograma com hue), análise ROC simplificada (sem sklearn, usando percentis), pairplot colorido por diagnóstico, violinplot, swarmplot para amostras menores, cálculo de sensibilidade/especificidade manual.

---

### Projeto 9 — Análise do Mercado Imobiliário

**Perfil:** Engenharia Civil / Investidores / Gestão Financeira
**Dataset:** `projeto_09_mercado_imobiliario.csv`
**Fonte inspiradora:** Dados FipeZap / registros imobiliários simulados

**Contexto:** Uma incorporadora que atua em Fortaleza e região metropolitana quer entender o comportamento do mercado imobiliário nos últimos 3 anos para orientar seus próximos lançamentos. A diretoria comercial precisa saber onde investir, qual perfil de imóvel tem maior demanda e como precificar novos empreendimentos.

**Perguntas de Negócio:**

1. Qual é a distribuição de preços por metro quadrado nos diferentes bairros? Quais são os mais valorizados e os mais acessíveis?
2. Como o preço médio por m² evoluiu trimestralmente? Há bairros com valorização acima da média?
3. Quais características do imóvel (área, quartos, vagas, andar, vista) mais influenciam o preço? Construa uma análise de importância relativa.
4. O tempo médio de venda (dias no mercado) varia por faixa de preço e por bairro? Imóveis mais caros demoram mais?
5. Existe um "sweet spot" de área e preço que concentra maior volume de transações? (análise de demanda)
6. Compare imóveis novos vs. usados: a diferença de preço por m² justifica a preferência do mercado?
7. Gere um mapa de calor (heatmap) de preço por m² e volume de transações por bairro para apoiar a decisão de lançamento.

**Técnicas esperadas:** regplot com análise de resíduos, jointplot, análise multivariada com pairplot, histogramas com KDE, cálculo de percentis para faixas, pivot_table complexo, subplots com grid para comparação por bairro.

---

### Projeto 10 — Análise de Indicadores Socioeconômicos Municipais

**Perfil:** Gestão Pública / Economia / Professores / Pesquisadores
**Dataset:** `projeto_10_indicadores_municipais.csv`
**Fonte inspiradora:** IBGE / Atlas do Desenvolvimento Humano / IPEA (adaptados)

**Contexto:** Uma consultoria foi contratada pelo governo do estado do Ceará para analisar indicadores socioeconômicos dos 184 municípios cearenses. O objetivo é identificar clusters de desenvolvimento, municípios que se destacam (positiva e negativamente) e propor uma priorização de investimentos públicos baseada em evidências.

**Perguntas de Negócio:**

1. Qual é a distribuição dos municípios por faixa de IDH? Quantos estão abaixo do limiar de "baixo desenvolvimento humano"?
2. Existe correlação entre PIB per capita e indicadores de educação (taxa de analfabetismo, anos de estudo) e saúde (mortalidade infantil, expectativa de vida)?
3. Quais municípios são "outliers positivos" — IDH acima do esperado dado seu PIB per capita? O que os diferencia?
4. A desigualdade de renda (índice de Gini) é maior em municípios mais ricos ou mais pobres? Há um padrão?
5. Agrupe os municípios em 4-5 clusters baseados em múltiplos indicadores. Descreva o perfil de cada cluster.
6. Quais indicadores apresentaram maior melhora na última década? Quais estagnaram?
7. Proponha um ranking priorizado de municípios para receber investimentos, justificando os critérios com dados.

**Técnicas esperadas:** clusterização manual (quintis, categorização), scatter com tamanho e cor representando variáveis, mapa de correlações, ranking com barh, análise de distribuição com swarmplot, cálculo de scores compostos, merge de múltiplas fontes.

---

## Orientações Finais

### Sobre os Datasets
Todos os datasets estão na pasta `datasets/` dentro de `projeto_final/`. Cada CSV já contém cabeçalho e está codificado em UTF-8. Alguns datasets possuem **problemas intencionais** (valores nulos, tipos incorretos, duplicatas, outliers) para que os alunos pratiquem limpeza de dados.

### Sobre a Apresentação
Cada grupo terá **5 a 7 minutos** para apresentar. A apresentação deve contar uma **história com os dados** — não é uma mera sequência de gráficos. Estrutura sugerida: (1) Contexto do problema, (2) O que os dados revelaram, (3) Insights principais, (4) Recomendações.

### Sobre o Código
O notebook deve ser **autoexplicativo** — alguém que não assistiu à apresentação deve conseguir entender a análise lendo o notebook. Use células Markdown para narrar cada etapa.

### Dicas
- Comecem pela **inspeção** dos dados (shape, dtypes, describe, info, head)
- Façam a **limpeza** antes de qualquer análise
- Usem **pelo menos 3 tipos diferentes** de gráfico
- Não ignorem **outliers** — investiguem e decidam o que fazer com eles
- A **conclusão** é tão importante quanto a análise — não terminem sem ela

---

*Bom trabalho e boas descobertas nos dados!*

**Prof. Cássio Pinheiro**
MBA em Ciência de Dados — UNIFOR — 2026
