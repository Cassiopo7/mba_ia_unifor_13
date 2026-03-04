# Índice de Projetos — Mapeamento por Perfil

## Atribuição Sugerida por Perfil Profissional

| # | Projeto | Perfil Ideal | Dataset | Registros |
|---|---------|-------------|---------|-----------|
| 01 | Indicadores Hospitalares | Saúde / Gestão Hospitalar | `projeto_01_indicadores_hospitalares.csv` | ~2.400 |
| 02 | E-commerce — Vendas | Administração / Gestão Comercial | `projeto_02_ecommerce_vendas.csv` | 8.000 |
| 03 | Qualidade do Ar | Engenharia Ambiental / Saúde Pública | `projeto_03_qualidade_ar.csv` | ~23.000 |
| 04 | Desempenho Educacional | Educação / Gestão Escolar | `projeto_04_desempenho_educacional.csv` | ~5.400 |
| 05 | Frota e Manutenção | Engenharia / Logística / Operações | `projeto_05_frota_manutencao.csv` | 4.500 |
| 06 | Consumo de Energia | Engenharia Elétrica / Sustentabilidade | `projeto_06_consumo_energia.csv` | 120.000 |
| 07 | People Analytics (RH) | Gestão de Pessoas / Administração | `projeto_07_people_analytics.csv` | 1.200 |
| 08 | Diabetes — Dados Clínicos | Medicina / Saúde | `projeto_08_diabetes_clinico.csv` | 2.000 |
| 09 | Mercado Imobiliário | Engenharia Civil / Investidores | `projeto_09_mercado_imobiliario.csv` | 3.500 |
| 10 | Indicadores Municipais (CE) | Gestão Pública / Economia / Pesquisa | `projeto_10_indicadores_municipais.csv` | 184 |

---

## Cobertura de Conteúdo por Projeto

Cada projeto exercita os 3 módulos da disciplina. A tabela abaixo detalha quais técnicas são mais exploradas:

| Técnica (Módulo) | P01 | P02 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 |
|-------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **M1** Tipos e conversões | ● | ●● | ● | ● | ● | ● | ● | ● | ● | ● |
| **M1** Listas/dicts/funções | ● | ● | ● | ● | ● | ● | ● | ● | ● | ●● |
| **M1** Tratamento de erros | ● | ●● | ● | ● | ● | ● | ● | ●● | ● | ● |
| **M1** Leitura de arquivos | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| **M2** NumPy | ● | ● | ●● | ● | ●● | ●● | ● | ●● | ● | ●● |
| **M2** Pandas (filter/sort) | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M2** Limpeza de dados | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M2** groupby/pivot_table | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ● | ●● | ●● |
| **M2** merge/concat | ● | ● | ●● | ● | ● | ●● | ● | ● | ● | ●● |
| **M3** Matplotlib básico | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● | ●● |
| **M3** Seaborn avançado | ●● | ● | ●● | ●● | ● | ● | ●● | ●● | ●● | ●● |
| **M3** Detecção outliers | ● | ● | ● | ● | ●● | ●● | ● | ●● | ●● | ●● |

● = utiliza | ●● = fortemente utiliza

---

## Problemas Intencionais nos Datasets

Todos os datasets possuem problemas para exercitar a limpeza:

| Problema | Projetos |
|----------|----------|
| Valores nulos (NaN) | Todos |
| Duplicatas | P01, P04 |
| Tipos incorretos (str no lugar de float) | P02 |
| Outliers extremos | P01, P05, P06, P08, P09, P10 |
| Valores negativos impossíveis | P03, P10 |
| Valores fora de faixa (IMC=999, IDH=1.5) | P08, P10 |

---

## Estrutura de Pastas

```
projeto_final/
├── PROJETO_FINAL.md          ← Documento completo com os 10 projetos
├── INDICE_PROJETOS.md        ← Este arquivo
└── datasets/
    ├── gerar_datasets.py     ← Script gerador (reprodutibilidade)
    ├── projeto_01_indicadores_hospitalares.csv
    ├── projeto_02_ecommerce_vendas.csv
    ├── projeto_03_qualidade_ar.csv
    ├── projeto_04_desempenho_educacional.csv
    ├── projeto_05_frota_manutencao.csv
    ├── projeto_06_consumo_energia.csv
    ├── projeto_07_people_analytics.csv
    ├── projeto_08_diabetes_clinico.csv
    ├── projeto_09_mercado_imobiliario.csv
    └── projeto_10_indicadores_municipais.csv
```
