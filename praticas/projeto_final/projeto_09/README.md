# Projeto 09 — Análise do Mercado Imobiliário

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

Uma incorporadora que atua em Fortaleza e região metropolitana quer entender o comportamento do mercado imobiliário nos últimos 3 anos para orientar seus próximos lançamentos. A diretoria comercial precisa saber onde investir, qual perfil de imóvel tem maior demanda e como precificar novos empreendimentos.

## Dataset

- **Arquivo:** `data/projeto_09_mercado_imobiliario.csv`
- **Fonte inspiradora:** Dados FipeZap / registros imobiliários simulados
- **Registros:** ~3.500

## Perguntas de Negócio

1. Qual é a distribuição de preços por metro quadrado nos diferentes bairros? Quais são os mais valorizados e os mais acessíveis?
2. Como o preço médio por m² evoluiu trimestralmente? Há bairros com valorização acima da média?
3. Quais características do imóvel (área, quartos, vagas, andar, vista) mais influenciam o preço? Construa uma análise de importância relativa.
4. O tempo médio de venda (dias no mercado) varia por faixa de preço e por bairro? Imóveis mais caros demoram mais?
5. Existe um "sweet spot" de área e preço que concentra maior volume de transações? (análise de demanda)
6. Compare imóveis novos vs. usados: a diferença de preço por m² justifica a preferência do mercado?
7. Gere um mapa de calor (heatmap) de preço por m² e volume de transações por bairro para apoiar a decisão de lançamento.

## Técnicas Esperadas

Regplot com análise de resíduos, jointplot, análise multivariada com pairplot, histogramas com KDE, cálculo de percentis para faixas, pivot_table complexo e subplots com grid para comparação por bairro, conforme conteúdo dos três módulos do curso.

---

## Estrutura do Projeto

```
projeto_09/
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
