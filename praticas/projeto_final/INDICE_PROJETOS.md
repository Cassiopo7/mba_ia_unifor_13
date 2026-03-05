# Índice de Projetos — Datathon Investigativo

## Mapeamento por Perfil Profissional

### Grupo A — Investigativos (padrões ocultos para descobrir)

| # | Operação | Perfil Ideal | Datasets | Fontes Reais |
|---|----------|-------------|----------|-------------|
| 01 | **Operação Bisturi** — Fraude Hospitalar | Saúde / Gestão Hospitalar | `indicadores_hospitalares`, `registro_procedimentos`, `denuncias_anonimas` | DataSUS, CNES |
| 02 | **Operação Marketplace** — Fraude E-commerce | Administração / Gestão Comercial | `ecommerce_vendas`, `vendedores_perfil`, `avaliacoes_suspeitas` | Olist (Kaggle), Reclame Aqui |
| 04 | **Operação Nota Inflada** — Fraude Educacional | Educação / Gestão Escolar | `desempenho_educacional`, `historico_avaliacoes_externas`, `metas_bonificacao` | INEP/SAEB, QEdu |
| 05 | **Operação Frota Fantasma** — Desvio Manutenção | Engenharia / Logística / Operações | `frota_manutencao`, `oficinas_credenciadas`, `tabela_precos_referencia` | SINDIREPA, DETRAN-CE |
| 09 | **Operação Lava-Imóvel** — Lavagem Dinheiro | Eng. Civil / Investidores / Finanças | `mercado_imobiliario`, `compradores_perfil`, `historico_precos_bairro` | FipeZap, VivaReal |

### Grupo B — Analíticos Realistas (investigação de negócio profunda)

| # | Operação | Perfil Ideal | Datasets | Fontes Reais |
|---|----------|-------------|----------|-------------|
| 03 | **Alerta Vermelho** — Crise Ambiental | Eng. Ambiental / Saúde Pública | `qualidade_ar`, `internacoes_respiratorias`, `cadastro_industrias` | OpenAQ, CETESB, DataSUS |
| 06 | **Operação Curto-Circuito** — Furto Energia | Eng. Elétrica / Sustentabilidade | `consumo_energia`, `ocorrencias_rede`, `cadastro_transformadores` | ANEEL, ONS |
| 07 | **Dossiê Exodus** — Discriminação + Turnover | Gestão de Pessoas / Administração | `people_analytics`, `pesquisa_clima_anonima`, `historico_promocoes` | CAGED/RAIS, Glassdoor |
| 08 | **Alerta Epidemiológico** — Surto Diabetes | Medicina / Saúde Pública | `diabetes_clinico`, `atendimentos_emergencia`, `unidades_saude_cobertura` | VIGITEL, DataSUS |
| 10 | **Radiografia Municipal** — Dinheiro Público | Gestão Pública / Economia / Pesquisa | `indicadores_municipais`, `repasses_federais`, `licitacoes_municipais` | IBGE, Atlas Brasil, IPEA |

---

## Cobertura de Conteúdo por Projeto

Cada projeto exercita os 3 módulos da disciplina. A tabela abaixo detalha quais técnicas são mais exploradas:

| Técnica (Módulo) | P01 | P02 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 |
|-------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **M1** Tipos e conversões | ● | ●● | ● | ● | ● | ● | ● | ●● | ● | ●● |
| **M1** Funções e lógica | ●● | ●● | ●● | ● | ●● | ●● | ●● | ● | ●● | ●● |
| **M1** Tratamento de erros | ● | ●● | ● | ● | ● | ● | ● | ●● | ● | ● |
| **M1** Leitura de arquivos | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M2** NumPy | ● | ● | ●● | ● | ●● | ●● | ● | ●● | ● | ●● |
| **M2** Pandas (filter/sort) | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M2** Limpeza de dados | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M2** groupby/pivot_table | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ● | ●● | ●● |
| **M2** merge/concat (3 datasets) | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M2** Detecção de duplicatas | ●● | ●● | ● | ●● | ●● | ● | ● | ● | ●● | ●● |
| **M3** Matplotlib básico | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M3** Seaborn avançado | ●● | ● | ●● | ●● | ● | ● | ●● | ●● | ●● | ●● |
| **M3** Detecção outliers/anomalias | ●● | ●● | ●● | ● | ●● | ●● | ● | ●● | ●● | ●● |

● = utiliza | ●● = fortemente utiliza

---

## Problemas Intencionais nos Datasets

Todos os datasets possuem problemas para exercitar a limpeza:

| Problema | Projetos |
|----------|----------|
| Valores nulos (NaN) | Todos |
| Duplicatas intencionais | P01, P04 |
| Tipos incorretos (str no lugar de float) | P02 |
| Outliers extremos | P01, P05, P06, P08, P09, P10 |
| Valores negativos impossíveis | P03, P10 |
| Valores fora de faixa (IMC=999, IDH=1.5) | P08, P10 |

---

## Padrões Ocultos por Projeto

Cada projeto investigativo tem padrões plantados nos dados que os alunos devem descobrir:

| Projeto | Tipo de Padrão | Complexidade |
|---------|---------------|-------------|
| P01 | Superfaturamento + pacientes fantasma + picos em meses de meta | Alta |
| P02 | Avaliações falsas + vendas em horário atípico + cluster de vendedores | Alta |
| P03 | Emissões noturnas ilegais + correlação com internações | Média |
| P04 | Inflação de notas internas + gap com SAEB + bonificação indevida | Alta |
| P05 | Superfaturamento + serviços repetidos + oficinas com vínculos | Alta |
| P06 | Queda abrupta de consumo (gato) + sobrecarga de transformador | Média |
| P07 | Gap salarial de gênero + gestor tóxico + tempo de promoção desigual | Média |
| P08 | Subdiagnóstico por faixa etária + falha de cobertura (UBS fechada) | Média |
| P09 | Renda incompatível + sobrepreço + revenda rápida (flip) + CNPJs ligados | Alta |
| P10 | Alto repasse + indicadores estagnados + empresas de fachada + fracionamento | Alta |

---

## Estrutura de Pastas

```
projeto_final/
├── PROJETO_FINAL.md              ← Documento geral do datathon
├── INDICE_PROJETOS.md            ← Este arquivo
├── datasets/
│   ├── gerar_datasets.py         ← Script gerador (30 CSVs)
│   ├── projeto_01_*.csv          ← 3 CSVs por projeto
│   ├── projeto_02_*.csv
│   ├── ...
│   └── projeto_10_*.csv
├── projeto_01/
│   ├── README.md                 ← Briefing da operação
│   ├── data/                     ← 3 CSVs do projeto
│   ├── notebooks/                ← Análise do aluno
│   ├── scripts/                  ← Scripts auxiliares
│   └── docs/                     ← Apresentação
├── projeto_02/
│   └── (mesma estrutura)
├── ...
└── projeto_10/
    └── (mesma estrutura)
```
