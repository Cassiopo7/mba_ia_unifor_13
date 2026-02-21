# Prática 02 – Gestão de Produtos de Loja

## Objetivo
Praticar compreensão de listas, operações com dicionários, lambda e filter para gestão de estoque.

## Dataset
`datasets/produtos_loja.csv`

**Colunas:** Codigo, Produto, Categoria, Preco, Quantidade_Estoque, Fornecedor, Ativo

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.2 – Estruturas de Dados Fundamentais (dicionários para representar produtos)
  - Seção 1.4 – Compreensões e Programação Funcional (list/dict comprehension, lambda, filter)
  - Seção 1.3 – Estruturas de Controle (condicionais para classificação)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.2 – Dicionários e Dict Comprehension
  - Seção 2.4 – Programação Funcional (map, filter, lambda)

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar cada produto como um dicionário em uma lista
2. Usando list comprehension, criar uma lista com os nomes dos produtos ativos
3. Calcular o valor total do estoque (preço × quantidade) para cada produto
4. Encontrar o produto mais caro e o mais barato

### Nível Intermediário
5. Usando dict comprehension, criar um dicionário {categoria: [lista_de_produtos]}
6. Usar `filter` com `lambda` para listar produtos com estoque abaixo de 10 unidades
7. Usar `map` com `lambda` para aplicar desconto de 15% em todos os preços e gerar nova lista
8. Calcular o valor total de estoque por categoria

### Nível Avançado
9. Criar uma função `buscar_produtos(dados, **criterios)` que aceite critérios variáveis (categoria, preco_max, preco_min, ativo) e retorne os produtos filtrados
10. Usar `reduce` para calcular o valor total de todo o estoque
11. Criar uma função que identifique produtos que precisam de reposição (estoque < 5) e gere um relatório
12. Classificar produtos por faixa de preço: "Barato" (<R$20), "Médio" (R$20-R$100), "Caro" (>R$100) usando compreensão de listas

## Dicas
- Ao converter "True"/"False" de string, use comparação de string, não bool() diretamente
- Lembre-se do uso de **kwargs na Seção 1.5 do notebook

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
