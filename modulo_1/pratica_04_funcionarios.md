# Prática 04 – Análise de Dados de Funcionários

## Objetivo
Praticar dicionários avançados, sets para operações de conjunto, funções com **kwargs e manipulação de arquivos.

## Dataset
`datasets/funcionarios_empresa.csv`

**Colunas:** ID, Nome, Departamento, Cargo, Salario, Data_Admissao, Cidade, Ativo

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.2 – Estruturas de Dados Fundamentais (dicionários, sets e operações de conjunto)
  - Seção 1.5 – Funções Avançadas (função `calcular_estatisticas` como modelo)
  - Seção 1.6 – Manipulação de Arquivos (leitura e escrita)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.2 – Dicionários e Sets (operações de conjunto: união, interseção, diferença)
  - Seção 2.3 – Funções (**kwargs, documentação)

## Tarefas

### Nível Básico
1. Ler o CSV e criar um dicionário onde a chave é o ID e o valor é um dicionário com os dados do funcionário
2. Calcular o salário médio de todos os funcionários
3. Listar todos os departamentos únicos usando set
4. Contar quantos funcionários estão ativos e inativos

### Nível Intermediário
5. Criar sets de funcionários por departamento e usar operações de conjunto para encontrar: cidades que têm funcionários em TODOS os departamentos (interseção)
6. Criar uma função `filtrar_funcionarios(**criterios)` que aceite critérios variáveis como departamento, salario_min, ativo, etc.
7. Calcular o salário médio por departamento usando dicionário
8. Identificar os 5 funcionários com maior e menor salário

### Nível Avançado
9. Calcular o tempo de empresa de cada funcionário (diferença de datas usando apenas Python puro)
10. Criar uma função que gere um arquivo CSV `relatorio_departamentos.csv` com: departamento, qtd_funcionarios, salario_medio, salario_max, salario_min
11. Implementar uma busca por nome parcial (case insensitive) usando compreensão de listas
12. Criar um sistema de menu simples (usando while + input simulado) que permita consultar dados por departamento, por faixa salarial ou gerar relatório

## Dicas
- Para operações com datas, use `datetime.strptime()` do módulo `datetime`
- Sets: `set_a & set_b` (interseção), `set_a | set_b` (união), `set_a - set_b` (diferença)
- `**kwargs` permite passar argumentos nomeados variáveis

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo `relatorio_departamentos.csv` gerado
