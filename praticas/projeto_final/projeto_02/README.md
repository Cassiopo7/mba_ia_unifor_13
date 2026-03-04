# Projeto 02 — Performance de Vendas no E-commerce

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

Uma empresa de e-commerce cearense que vende produtos de moda, eletrônicos e casa & decoração precisa entender seu desempenho de vendas dos últimos 2 anos. O CEO quer identificar padrões de compra, sazonalidade e oportunidades de crescimento antes de uma rodada de investimento.

## Dataset

- **Arquivo:** `data/projeto_02_ecommerce_vendas.csv`
- **Fonte inspiradora:** Brazilian E-Commerce (Olist) / dados simulados
- **Registros:** ~8.000

## Perguntas de Negócio

1. Qual é a evolução mensal do faturamento e do ticket médio? Há tendência de crescimento ou estagnação?
2. Quais categorias de produto concentram maior receita vs. maior volume de pedidos? Existe um "Pareto" (80/20)?
3. Como se distribui a base de clientes por região (estado)? Há concentração geográfica que represente risco?
4. Qual é a taxa de cancelamento de pedidos por categoria e por faixa de valor? O que pode estar causando cancelamentos em faixas específicas?
5. Existe diferença significativa no comportamento de compra entre dias da semana e finais de semana? E entre turnos do dia?
6. Quais são os 10 produtos com maior taxa de avaliação negativa (nota ≤ 2)? Há padrões em comum?
7. Projete um painel de indicadores-chave (KPIs) que o CEO possa acompanhar semanalmente.

## Técnicas Esperadas

O projeto deve utilizar conceitos dos três módulos do curso: **análise temporal** com resample para tendências mensais, **crosstab** para cruzamento de categorias e variáveis, **value_counts** normalizado para distribuições relativas, **análise de Pareto** para identificar concentração de receita, **gráficos de barras empilhados** para composição, **scatter com regressão** para tendências, e **subplots organizados** para painéis integrados de indicadores.

---

## Estrutura do Projeto

```
projeto_02/
├── README.md          ← Este arquivo
├── data/              ← Dataset(s) do projeto
├── notebooks/         ← Notebook(s) Jupyter com a análise
├── scripts/           ← Scripts Python auxiliares (se necessário)
└── docs/              ← Documentação adicional, apresentação
```

## Entregáveis

1. **Notebook Python (.ipynb)** em `notebooks/` contendo:
   - Importação e inspeção inicial dos dados
   - Limpeza e transformação (nulos, tipos, duplicatas, outliers)
   - Análise exploratória com estatísticas descritivas
   - Mínimo de **8 visualizações** (mix de Matplotlib e Seaborn)
   - Respostas às perguntas de negócio com evidências nos dados
   - Células Markdown narrando cada etapa (storytelling)
   - Conclusões e recomendações

2. **Apresentação oral** (5-7 minutos) — arquivo em `docs/`

3. **Conclusões e recomendações** escritas no notebook

## Critérios de Avaliação

| Critério | Peso | O que será observado |
|----------|------|----------------------|
| **Limpeza e transformação dos dados** | 20% | Tratamento de nulos, duplicatas, tipos incorretos, outliers. Justificativa das decisões tomadas. |
| **Profundidade da análise exploratória** | 25% | Estatísticas descritivas, segmentações, cruzamentos entre variáveis. Respostas fundamentadas às perguntas de negócio. |
| **Qualidade e variedade das visualizações** | 20% | Mínimo 8 gráficos. Pelo menos 3 tipos diferentes. Títulos, rótulos, legendas. Gráficos adequados ao tipo de dado. |
| **Storytelling e clareza nas conclusões** | 20% | Narrativa coerente em Markdown. Insights acionáveis. Recomendações baseadas em evidências. Apresentação oral. |
| **Organização do código e boas práticas** | 15% | Código limpo e legível. Uso de funções quando apropriado. Notebook autoexplicativo. Estrutura de pastas respeitada. |

### Escala de Notas

| Nota | Descrição |
|------|-----------|
| **10** | Excepcional — análise completa, insights originais, código exemplar, storytelling envolvente |
| **8-9** | Muito bom — todos os critérios atendidos com qualidade, pequenas melhorias possíveis |
| **6-7** | Satisfatório — atende aos requisitos mínimos, análise superficial em alguns pontos |
| **4-5** | Insuficiente — falhas significativas em limpeza, análise ou visualizações |
| **0-3** | Inadequado — entrega incompleta ou sem evidência de esforço analítico |

### Bonificações (+0.5 cada, máx +1.5)
- Uso criativo de feature engineering (criar variáveis derivadas relevantes)
- Visualização avançada além do esperado (dashboard integrado, gráficos interativos)
- Análise adicional não solicitada que gere insights valiosos

### Penalizações
- Notebook sem células Markdown explicativas: **-1.0 ponto**
- Gráficos sem título, rótulos ou legendas: **-0.5 ponto por gráfico**
- Código copiado sem adaptação (entre grupos): **nota zero para ambos**
- Entrega após o prazo: **-2.0 pontos por dia**

## Dicas Importantes

1. Comecem pela **inspeção** dos dados (`shape`, `dtypes`, `describe`, `info`, `head`)
2. Façam a **limpeza** antes de qualquer análise
3. Usem pelo menos **3 tipos diferentes** de gráfico
4. Não ignorem **outliers** — investiguem e decidam o que fazer
5. A **conclusão** é tão importante quanto a análise
6. O notebook deve ser **autoexplicativo** — alguém que não assistiu à apresentação deve entender

---

*Prof. Cássio Pinheiro — MBA Ciência de Dados — UNIFOR — 2026*
