# Prática 06 – Vendas de Cafeteria

## Objetivo
Praticar map, filter, reduce, lambda e operações com listas para análise de vendas.

## Dataset
`datasets/vendas_cafeteria.csv`

**Colunas:** Data, Produto, Categoria, Quantidade, Preco_Unitario, Forma_Pagamento, Turno

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.4 – Compreensões e Programação Funcional (lambda, map, filter, reduce)
  - Seção 1.1 – Tipos de Dados e Operações Básicas (operações aritméticas)
  - Seção 1.5 – Funções Avançadas (funções com argumentos padrão)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.4 – Programação Funcional (map, filter, reduce com exemplos)
  - Seção 2.3 – Funções Lambda

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar os dados em uma lista de dicionários
2. Calcular o faturamento de cada venda (quantidade × preço_unitário) e adicionar como nova chave
3. Calcular o faturamento total da cafeteria
4. Listar todos os produtos vendidos e a quantidade total de cada um

### Nível Intermediário
5. Usar `lambda` com `map` para calcular o faturamento de cada linha (como lista)
6. Usar `filter` com `lambda` para encontrar todas as vendas do turno da manhã com valor acima de R$20
7. Usar `reduce` para somar todo o faturamento (sem usar sum())
8. Criar uma função `resumo_turno(dados, turno)` que retorne total de vendas, faturamento e ticket médio

### Nível Avançado
9. Combinar `map` e `filter`: primeiro filtrar vendas de "Bebidas", depois calcular o faturamento de cada uma
10. Encontrar a forma de pagamento mais utilizada e o turno mais lucrativo
11. Criar uma função que calcule a receita por dia e identifique o dia com maior e menor faturamento
12. Gerar um arquivo `relatorio_cafeteria.txt` com resumo por turno, por produto e por forma de pagamento

## Dicas
- `reduce(lambda x, y: x + y, lista)` soma todos os elementos
- Combine filter e map em sequência: `list(map(func, filter(cond, dados)))`
- Lembre-se: `map` retorna iterator, precisa de `list()` para visualizar

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo `relatorio_cafeteria.txt` gerado
