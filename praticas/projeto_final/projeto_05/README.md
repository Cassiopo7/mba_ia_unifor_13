# Projeto 05 — Gestão de Frota e Manutenção Veicular

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

Uma empresa de logística com frota de 200 veículos (caminhões e vans) precisa otimizar seus custos de manutenção. Nos últimos 18 meses, os gastos com manutenção corretiva subiram 35%. A gerência de operações precisa entender o que está acontecendo e propor um plano de manutenção preventiva baseado em dados.

## Dataset

- **Arquivo:** `data/projeto_05_frota_manutencao.csv`
- **Fonte inspiradora:** Dados operacionais de frotas (simulados com base em padrões reais)
- **Registros:** ~4.500

## Perguntas de Negócio

1. Qual é a distribuição dos custos de manutenção por tipo (preventiva vs. corretiva) e por categoria de veículo? A proporção mudou ao longo do tempo?
2. Quais componentes/sistemas (motor, freios, suspensão, elétrica) concentram maior custo e maior frequência de falhas?
3. Existe relação entre a quilometragem acumulada e a frequência de manutenções corretivas? Qual é o ponto crítico de km?
4. A idade do veículo é um preditor melhor que a quilometragem para antecipar falhas? Construa uma análise comparativa.
5. Quais veículos específicos são "outliers" em custo de manutenção? Seria mais econômico substituí-los?
6. Proponha faixas de km/tempo para manutenção preventiva por componente, baseado nos padrões encontrados nos dados.

## Técnicas Esperadas

O projeto deve utilizar conceitos dos três módulos do curso: **análise de custos** com groupby e agregações, **scatter com anotações** para destacar veículos ou pontos críticos, **detecção de outliers** (IQR e Z-score) com justificativa de tratamento, **análise de sobrevivência simplificada** para km até primeira falha por componente, **gráficos de Pareto** para concentração de custos/falhas, e **cumsum** para custos acumulados e evolução temporal.

---

## Estrutura do Projeto

```
projeto_05/
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
