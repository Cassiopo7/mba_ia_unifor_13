# Projeto 01 — Análise de Indicadores Hospitalares

> **Disciplina:** Programação para Ciência de Dados  
> **Curso:** MBA em Ciência de Dados — UNIFOR  
> **Professor:** Cássio Pinheiro  
> **Formato:** Datathon Aplicado  
> **Trabalho:** Em duplas ou trios (formação livre)

---

## Contexto de Negócio

Você foi contratado como analista de dados por uma rede hospitalar do Nordeste que deseja entender o desempenho operacional de suas 15 unidades nos últimos 3 anos. A diretoria precisa de evidências para decidir onde investir, quais unidades precisam de intervenção e como otimizar a taxa de ocupação de leitos.

## Dataset

- **Arquivo:** `data/projeto_01_indicadores_hospitalares.csv`
- **Fonte inspiradora:** Dados do DataSUS / CNES (adaptados)
- **Registros:** ~2.400

## Perguntas de Negócio

1. Qual é a taxa média de ocupação de leitos por unidade e como ela evoluiu trimestralmente? Há unidades consistentemente acima ou abaixo da média?
2. Existe correlação entre o tempo médio de internação e a taxa de reinternação em 30 dias? O que isso sugere sobre a qualidade da alta?
3. Quais especialidades médicas apresentam maior variação sazonal na demanda? Como isso pode orientar o planejamento de escala?
4. A taxa de mortalidade hospitalar varia significativamente entre unidades de mesmo porte? Quais fatores operacionais parecem associados?
5. Qual é o perfil dos pacientes (faixa etária, tipo de internação) que mais contribuem para a superlotação?
6. Construa um dashboard analítico (visualizações integradas) que a diretoria possa usar para monitoramento mensal.

## Técnicas Esperadas

O projeto deve utilizar conceitos dos três módulos do curso: **groupby** multi-nível para agregações por unidade e especialidade, **pivot_table** para reorganizar indicadores temporais, **visualizações temporais** (lineplot) para evolução trimestral, **heatmaps de correlação** entre variáveis de desempenho, **boxplots comparativos** entre unidades e especialidades, e **tratamento de outliers** em tempos de internação, com justificativa das decisões tomadas.

---

## Estrutura do Projeto

```
projeto_01/
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
