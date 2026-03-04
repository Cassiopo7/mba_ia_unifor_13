# Projeto 10 — Análise de Indicadores Socioeconômicos Municipais

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

Uma consultoria foi contratada pelo governo do estado do Ceará para analisar indicadores socioeconômicos dos 184 municípios cearenses. O objetivo é identificar clusters de desenvolvimento, municípios que se destacam (positiva e negativamente) e propor uma priorização de investimentos públicos baseada em evidências.

## Dataset

- **Arquivo:** `data/projeto_10_indicadores_municipais.csv`
- **Fonte inspiradora:** IBGE / Atlas do Desenvolvimento Humano / IPEA (adaptados)
- **Registros:** ~184

## Perguntas de Negócio

1. Qual é a distribuição dos municípios por faixa de IDH? Quantos estão abaixo do limiar de "baixo desenvolvimento humano"?
2. Existe correlação entre PIB per capita e indicadores de educação (taxa de analfabetismo, anos de estudo) e saúde (mortalidade infantil, expectativa de vida)?
3. Quais municípios são "outliers positivos" — IDH acima do esperado dado seu PIB per capita? O que os diferencia?
4. A desigualdade de renda (índice de Gini) é maior em municípios mais ricos ou mais pobres? Há um padrão?
5. Agrupe os municípios em 4-5 clusters baseados em múltiplos indicadores. Descreva o perfil de cada cluster.
6. Quais indicadores apresentaram maior melhora na última década? Quais estagnaram?
7. Proponha um ranking priorizado de municípios para receber investimentos, justificando os critérios com dados.

## Técnicas Esperadas

Clusterização manual (quintis, categorização), scatter com tamanho e cor representando variáveis, mapa de correlações, ranking com barh, análise de distribuição com swarmplot, cálculo de scores compostos e merge de múltiplas fontes, conforme conteúdo dos três módulos do curso.

---

## Estrutura do Projeto

```
projeto_10/
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
