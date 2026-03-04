# Projeto 08 — Análise de Dados Clínicos — Diabetes

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

Uma clínica especializada em endocrinologia atende 2.000 pacientes em acompanhamento para prevenção e tratamento de diabetes tipo 2. A equipe médica precisa entender quais fatores clínicos e de estilo de vida estão mais associados ao desenvolvimento da doença, para criar protocolos de triagem mais eficientes e programas de prevenção direcionados.

## Dataset

- **Arquivo:** `data/projeto_08_diabetes_clinico.csv`
- **Fonte inspiradora:** Pima Indians Diabetes Database / dados clínicos simulados
- **Registros:** ~2.000

## Perguntas de Negócio

1. Qual é a prevalência de diabetes na base e como ela se distribui por faixa etária, sexo e IMC?
2. Quais indicadores clínicos (glicemia de jejum, HbA1c, pressão arterial, colesterol, triglicerídeos) apresentam maior diferença entre pacientes diabéticos e não-diabéticos?
3. O IMC é o melhor preditor isolado de diabetes ou existem indicadores mais discriminantes? Construa uma análise comparativa.
4. Existem pacientes com indicadores clínicos de risco que ainda não foram diagnosticados? (possíveis subdiagnosticados)
5. Há diferença no perfil de risco entre homens e mulheres? A idade de onset é similar?
6. Pacientes que praticam atividade física regular apresentam indicadores clínicos significativamente melhores, mesmo com IMC elevado?
7. Proponha faixas de risco (baixo/médio/alto) baseadas nos indicadores que mais discriminam, com evidência visual.

## Técnicas Esperadas

Distribuições comparativas (histograma com hue), análise ROC simplificada (sem sklearn, usando percentis), pairplot colorido por diagnóstico, violinplot, swarmplot para amostras menores e cálculo de sensibilidade/especificidade manual, conforme conteúdo dos três módulos do curso.

---

## Estrutura do Projeto

```
projeto_08/
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
