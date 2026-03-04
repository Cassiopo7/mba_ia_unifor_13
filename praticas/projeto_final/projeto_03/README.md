# Projeto 03 — Qualidade do Ar e Saúde Pública

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

A Secretaria de Meio Ambiente de uma capital nordestina instalou 8 estações de monitoramento de qualidade do ar. Após 2 anos de coleta, precisa de uma análise que demonstre padrões de poluição, identifique zonas críticas e embase a criação de políticas públicas para redução de emissões.

## Dataset

- **Arquivo:** `data/projeto_03_qualidade_ar.csv`
- **Fonte inspiradora:** Dados de estações de monitoramento (CETESB / OpenAQ adaptados)
- **Registros:** ~23.000

## Perguntas de Negócio

1. Quais estações apresentam concentrações médias de MP2.5 e MP10 acima dos limites recomendados pela OMS? Com que frequência isso ocorre?
2. Existe padrão sazonal na qualidade do ar? Meses de seca vs. chuva apresentam diferenças significativas?
3. Qual é o horário do dia com maior concentração de poluentes? Isso coincide com horários de pico de trânsito?
4. Há correlação entre os diferentes poluentes (MP2.5, MP10, O3, NO2, SO2)? O que isso sugere sobre as fontes de emissão?
5. As estações próximas a zonas industriais apresentam padrões distintos das estações em áreas residenciais?
6. Construa um índice composto de qualidade do ar (baseado nos poluentes disponíveis) e classifique cada estação/período.

## Técnicas Esperadas

O projeto deve utilizar conceitos dos três módulos do curso: **merge** de datasets quando houver múltiplas fontes, **análise temporal** por hora, dia e mês, **heatmaps calendário** para visualização sazonal, **violinplots** para distribuições por estação, **cálculo de percentis** para limites e categorização, **criação de features derivadas** (índice composto, classificação), e **FacetGrid** do Seaborn para comparações multi-painel.

---

## Estrutura do Projeto

```
projeto_03/
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
