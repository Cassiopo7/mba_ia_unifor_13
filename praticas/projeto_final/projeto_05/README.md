# Projeto 05 — Operação Frota Fantasma: Desvio em Manutenção

> **Disciplina:** Programação para Ciência de Dados
> **Curso:** MBA em Ciência de Dados — UNIFOR
> **Professor:** Cássio Pinheiro
> **Formato:** Datathon Investigativo
> **Trabalho:** Em duplas ou trios (formação livre)
> **Classificação:** Grupo A — Investigativo (padrões ocultos para descobrir)

---

## Briefing da Operação

Uma empresa de logística com frota de 200 veículos viu os custos de manutenção **subirem 35% em 18 meses** sem explicação operacional. A auditoria interna suspeita que **oficinas credenciadas estão superfaturando serviços**, registrando **manutenções repetidas desnecessárias** e atendendo veículos em **cidades incompatíveis** com suas rotas. Há indícios de que os responsáveis pelo desvio estão ligados entre si.

Você recebeu os registros de manutenção, o cadastro de oficinas e a tabela de preços de referência do mercado. Monte o dossiê.

---

## Datasets Fornecidos

### 1. `data/projeto_05_frota_manutencao.csv`
4.500+ registros de manutenções realizadas (18 meses).

| Coluna | Descrição |
|--------|-----------|
| `manutencao_id` | Identificador da manutenção |
| `veiculo_id` | Identificador do veículo |
| `tipo_veiculo` | Tipo (Caminhão, Van, Utilitário) |
| `ano_fabricacao` | Ano de fabricação |
| `data_manutencao` | Data da manutenção |
| `oficina` | Nome da oficina |
| `tipo_manutencao` | Preventiva ou Corretiva |
| `componente` | Componente (Motor, Freios, Suspensão, etc.) |
| `custo_reais` | Custo do serviço (R$) |
| `tempo_parado_horas` | Tempo de parada do veículo |
| `km_odometro` | Quilometragem no momento |
| `cidade_servico` | Cidade onde o serviço foi realizado |

### 2. `data/projeto_05_oficinas_credenciadas.csv`
Cadastro das oficinas credenciadas.

| Coluna | Descrição |
|--------|-----------|
| `oficina_id` | Identificador |
| `nome_oficina` | Nome da oficina |
| `cnpj` | CNPJ |
| `socio_principal` | Nome do sócio principal |
| `endereco` | Endereço |
| `cidade` | Cidade |
| `data_credenciamento` | Data de credenciamento |
| `avaliacao_media` | Avaliação média |
| `total_servicos_realizados` | Total de serviços realizados |

### 3. `data/projeto_05_tabela_precos_referencia.csv`
Tabela de preços de referência do mercado (SINDIREPA).

| Coluna | Descrição |
|--------|-----------|
| `componente` | Componente |
| `tipo_manutencao` | Preventiva ou Corretiva |
| `preco_referencia_min` | Preço mínimo de referência (R$) |
| `preco_referencia_medio` | Preço médio de referência (R$) |
| `preco_referencia_max` | Preço máximo de referência (R$) |
| `fonte` | Fonte da tabela |
| `data_atualizacao` | Data de atualização |

---

## Missão

Investigue os dados e responda:

1. **Quais oficinas cobram acima da tabela de referência?** Cruze os custos de manutenção com a tabela SINDIREPA. Quais oficinas estão consistentemente 40-80% acima?
2. **Existem serviços repetidos no mesmo veículo em intervalo curto?** Identifique manutenções do mesmo componente no mesmo veículo em menos de 30 dias. Em quais oficinas isso se concentra?
3. **Há veículos sendo atendidos em cidades incompatíveis com sua base operacional?** Cruze a cidade de serviço com o padrão de localização do veículo. Há manutenções em cidades como Recife, Salvador, Teresina?
4. **As oficinas suspeitas têm vínculos entre si?** Analise o cadastro: mesmo sócio, mesmo endereço, datas de credenciamento próximas.
5. **Qual o impacto financeiro do desvio?** Calcule quanto a empresa pagou a mais vs. o preço de referência nas oficinas suspeitas.
6. **Proponha um sistema de alertas** baseado nos padrões descobertos para prevenir futuros desvios.

---

## Pistas Iniciais

- Compare o **custo médio por componente** de cada oficina com o **preço_referencia_medio** da tabela SINDIREPA
- Procure **mesmo veiculo_id + mesmo componente** com diferença de **< 30 dias** entre manutenções
- Filtre manutenções feitas em cidades fora do Ceará — veículos dessa frota operam localmente
- No cadastro de oficinas, procure **sócios com mesmo sobrenome** e **mesmo endereço**
- Três oficinas se destacam — comece por elas

---

## Desafio de Dados Reais

Enriqueça sua investigação com dados públicos reais:

| Fonte | URL | O que buscar |
|-------|-----|-------------|
| **SINDIREPA** | https://www.sindirepa.org.br/ | Tabela de referência de preços de manutenção |
| **DETRAN-CE** | https://www.detran.ce.gov.br/ | Dados de frota registrada no Ceará |

**Perguntas de cruzamento:**
- Os preços cobrados pelas oficinas legítimas estão compatíveis com a referência real do mercado?
- O perfil da frota (idade, tipo) é compatível com a realidade de empresas de logística?

---

## Técnicas Esperadas

| Módulo | Técnicas |
|--------|----------|
| **M1 — Python** | Funções para cálculo de sobrepreço, loops para detecção de padrões temporais, tratamento de erros |
| **M2 — Pandas/NumPy** | `merge` entre 3 datasets, `groupby` por oficina/componente, detecção de duplicatas por múltiplas colunas, cálculos de razões e desvios, `diff()` para intervalos temporais |
| **M3 — Visualização** | Gráficos de Pareto (custos por oficina), scatter com anotações, boxplots de custo por componente, barplots comparativos (real vs. referência), cumsum para custos acumulados |

---

## Estrutura do Projeto

```
projeto_05/
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
   - Conclusões: quais oficinas estão desviando e quanto custou

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
