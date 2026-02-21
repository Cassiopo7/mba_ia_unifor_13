# Módulo 1 – Práticas de Fundamentos de Programação com Python

## Visão Geral

Este módulo contém **10 práticas** com datasets temáticos variados, cobrindo todos os conceitos do Módulo 1 do curso. Cada prática possui **12 tarefas** organizadas em 3 níveis de dificuldade (Básico, Intermediário e Avançado).

**Total de tarefas disponíveis:** 120

---

## Mapa de Práticas por Tema

| # | Prática | Dataset | Foco Principal |
|---|---------|---------|----------------|
| 01 | [Análise de Notas de Alunos](pratica_01_alunos_notas.md) | `alunos_notas.csv` | Listas, dicionários, funções |
| 02 | [Gestão de Produtos de Loja](pratica_02_produtos_loja.md) | `produtos_loja.csv` | Compreensões, lambda, filter |
| 03 | [Análise de Temperaturas](pratica_03_temperaturas.md) | `temperaturas_cidades.csv` | Controle de fluxo, tuplas, sets |
| 04 | [Dados de Funcionários](pratica_04_funcionarios.md) | `funcionarios_empresa.csv` | Dicionários avançados, sets, **kwargs |
| 05 | [Catálogo de Filmes](pratica_05_filmes.md) | `filmes_streaming.csv` | Compreensões avançadas, reduce, tuplas |
| 06 | [Vendas de Cafeteria](pratica_06_vendas_cafeteria.md) | `vendas_cafeteria.csv` | map, filter, reduce, lambda |
| 07 | [Sistema de Biblioteca](pratica_07_biblioteca.md) | `biblioteca_livros.csv` | Strings, listas, dicionários |
| 08 | [Desempenho de Atletas](pratica_08_atletas.md) | `atletas_corrida.csv` | Funções avançadas, sorted, tuplas |
| 09 | [Controle de Gastos Pessoais](pratica_09_gastos.md) | `gastos_pessoais.csv` | **Integradora** – todos os conceitos |
| 10 | [Análise de Dados Clínicos](pratica_10_pacientes.md) | `pacientes_clinica.csv` | Funções, classificação condicional |

---

## Mapa de Conceitos por Prática

| Conceito (Seção do Notebook) | P01 | P02 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 |
|------------------------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1.1 Tipos de Dados e Operações | ✓ | | | | | ✓ | | | ✓ | ✓ |
| 1.2 Listas | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 1.2 Dicionários | ✓ | ✓ | | ✓ | ✓ | | ✓ | | ✓ | |
| 1.2 Tuplas | | | ✓ | | ✓ | | | ✓ | ✓ | |
| 1.2 Sets | | | ✓ | ✓ | ✓ | | | | ✓ | |
| 1.3 Estruturas de Controle | | | ✓ | | | | | | ✓ | ✓ |
| 1.4 List Comprehension | | ✓ | | | ✓ | | ✓ | | ✓ | |
| 1.4 Dict Comprehension | | ✓ | | | ✓ | | | | ✓ | |
| 1.4 Lambda/Map/Filter | ✓ | ✓ | | | ✓ | ✓ | | | ✓ | ✓ |
| 1.4 Reduce | | ✓ | | | ✓ | ✓ | | | ✓ | |
| 1.5 Funções Avançadas | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
| 1.6 Manipulação de Arquivos | ✓ | | ✓ | ✓ | | ✓ | ✓ | | ✓ | ✓ |

---

## Sugestões de Distribuição para 25 Alunos

### Opção A – Prática Individual (cada aluno faz 1 prática)
- Atribuir práticas 01-10, repetindo as práticas para preencher 25 vagas
- Priorizar variedade: cada prática para 2-3 alunos

### Opção B – Prática em Dupla/Trio + Individual
- **Duplas/Trios:** Uma prática intermediária (P02-P08) por grupo
- **Individual:** Prática integradora (P09 ou P10) para todos

### Opção C – Progressão de Dificuldade
- **Semana 1:** Todos fazem P01 (Básico) como aquecimento
- **Semana 2:** Escolher uma entre P02-P08 (Intermediário)
- **Semana 3:** Todos fazem P09 (Integradora/Avançado)

---

## Referências do Curso

- **Notebook principal:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb` (Módulo 1, Seções 1.1 a 1.6)
- **Documentação completa:** `documentacao_completa.md` (Capítulo 2 – Python para Ciência de Dados)
- **Datasets:** Pasta `datasets/` (10 arquivos CSV)

---

## Critérios de Avaliação Sugeridos

| Nível | Peso | Descrição |
|-------|------|-----------|
| Básico (tarefas 1-4) | 40% | Domínio dos fundamentos |
| Intermediário (tarefas 5-8) | 35% | Aplicação de conceitos |
| Avançado (tarefas 9-12) | 25% | Criatividade e integração |

**Observação:** O código deve usar apenas Python puro (sem pandas, numpy ou outras bibliotecas de dados). O objetivo é praticar os fundamentos da linguagem.
