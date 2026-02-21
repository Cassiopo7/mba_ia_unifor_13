# Prática 03 – Análise de Temperaturas

## Objetivo
Praticar estruturas de controle (for, while, if/elif/else), funções com argumentos padrão e operações com tuplas.

## Dataset
`datasets/temperaturas_cidades.csv`

**Colunas:** Cidade, Estado, Data, Temp_Min, Temp_Max, Umidade, Choveu

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.3 – Estruturas de Controle (for, while, if/elif/else)
  - Seção 1.2 – Estruturas de Dados Fundamentais (tuplas para coordenadas, sets para cidades únicas)
  - Seção 1.5 – Funções Avançadas (argumentos padrão, docstrings)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.2 – Tuplas e Sets
  - Seção 2.3 – Funções (argumentos padrão, *args, **kwargs)

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar os dados em uma lista de listas
2. Usando um loop `for`, calcular a amplitude térmica (Temp_Max - Temp_Min) de cada registro
3. Usando `if/elif/else`, classificar cada dia como: "Frio" (max < 22), "Agradável" (22-30), "Quente" (> 30)
4. Contar quantos dias choveu e quantos não choveu

### Nível Intermediário
5. Criar um set com todas as cidades únicas do dataset
6. Usar tuplas para armazenar pares (cidade, temperatura_media) e ordená-los
7. Criar uma função `estatisticas_cidade(dados, cidade, metrica='media')` com argumento padrão que calcule média, máxima ou mínima da temperatura para uma cidade
8. Usando um loop `while`, encontrar a primeira sequência de 3 dias consecutivos sem chuva

### Nível Avançado
9. Criar uma função que receba `*cidades` (argumentos variáveis) e retorne um dicionário com estatísticas de cada cidade
10. Calcular a correlação simples entre umidade e ocorrência de chuva (sem bibliotecas externas)
11. Identificar os dias com temperatura extrema (outliers): temp_max > média + 2*desvio_padrão
12. Gerar um relatório em arquivo .txt com resumo por cidade e por estado

## Dicas
- Use unpacking de tuplas: `cidade, estado, *resto = linha`
- Sets são úteis para remover duplicatas: `set(lista)`
- Relembre a sintaxe de funções com *args na documentação

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo de relatório gerado
