# Prática 09 – Controle de Gastos Pessoais

## Objetivo
Praticar todas as estruturas de dados (listas, dicionários, tuplas, sets), programação funcional completa e manipulação de arquivos.

## Dataset
`datasets/gastos_pessoais.csv`

**Colunas:** Data, Descricao, Categoria, Valor, Tipo, Forma_Pagamento, Essencial

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.1 – Tipos de Dados e Operações Básicas (operações com floats)
  - Seção 1.2 – Estruturas de Dados Fundamentais (TODAS: listas, dicionários, tuplas, sets)
  - Seção 1.3 – Estruturas de Controle (for, while, condicionais)
  - Seção 1.4 – Compreensões e Programação Funcional (TODAS: comprehensions, lambda, map, filter, reduce)
  - Seção 1.5 – Funções Avançadas (todos os tipos de argumentos)
  - Seção 1.6 – Manipulação de Arquivos (leitura e escrita)
- **Documentação:** `documentacao_completa.md`
  - Todas as seções do Capítulo 2 são relevantes

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar em uma lista de dicionários
2. Calcular o gasto total e o gasto médio por transação
3. Criar um set com todas as categorias e formas de pagamento únicas
4. Separar gastos essenciais e não essenciais em duas listas

### Nível Intermediário
5. Criar um dicionário de gastos por categoria: `{categoria: valor_total}`
6. Usando `filter`, encontrar todos os gastos variáveis acima de R$100
7. Usando `map`, criar uma lista de strings formatadas: "Data - Descricao: R$ Valor"
8. Usando `reduce`, calcular o total de gastos (soma acumulada)

### Nível Avançado
9. Implementar uma função `analisar_gastos(dados, **filtros)` que aceite filtros como categoria, tipo, essencial, valor_min, valor_max
10. Criar um orçamento mensal: calcular total por categoria e comparar com limites predefinidos (dicionário de limites)
11. Gerar uma tupla nomeada ou tupla simples para cada resumo de categoria: (categoria, total, media, quantidade, percentual_do_total)
12. Gerar relatório completo em arquivo `controle_financeiro.txt` com: resumo geral, gastos por categoria, gastos fixos vs variáveis, essenciais vs não essenciais, forma de pagamento mais usada

## Dicas
- Esta prática é integradora: combina TODOS os conceitos do Módulo 1
- Use `from functools import reduce` para o reduce
- Tuplas são boas para resumos imutáveis
- Sets eliminam duplicatas automaticamente

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo `controle_financeiro.txt` gerado
