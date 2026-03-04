# Prática 05 – Catálogo de Filmes

## Objetivo
Praticar compreensões avançadas (list, dict, set comprehension), tuplas, programação funcional e reduce.

## Dataset
`datasets/filmes_streaming.csv`

**Colunas:** Titulo, Genero, Ano, Duracao_Min, Avaliacao, Idioma, Assistido

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.4 – Compreensões e Programação Funcional (list, dict, set comprehension, reduce)
  - Seção 1.2 – Estruturas de Dados Fundamentais (tuplas para dados imutáveis)
  - Seção 1.3 – Estruturas de Controle (loops e condicionais)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.2 – Listas, Tuplas, Dicionários e Sets
  - Seção 2.4 – Programação Funcional (map, filter, reduce)

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar os dados em uma lista de dicionários
2. Usando list comprehension, criar uma lista apenas com os títulos dos filmes assistidos
3. Usando set comprehension, extrair todos os gêneros e idiomas únicos
4. Calcular a avaliação média de todos os filmes

### Nível Intermediário
5. Usando dict comprehension, criar um dicionário {genero: quantidade_de_filmes}
6. Criar uma lista de tuplas (titulo, avaliacao) ordenada por avaliação (maior para menor)
7. Usar `filter` para encontrar filmes com avaliação acima de 8.0 e duração menor que 120 min
8. Usar `map` para criar uma lista formatada: "Titulo (Ano) - Nota: X.X"

### Nível Avançado
9. Usar `reduce` para encontrar o filme com a maior avaliação (sem usar max())
10. Criar compreensão aninhada: para cada gênero, listar os filmes ordenados por avaliação
11. Implementar uma função de recomendação: dado um gênero favorito, retornar os 3 melhores filmes não assistidos daquele gênero
12. Calcular estatísticas por década (1990s, 2000s, 2010s, 2020s) usando dict comprehension e funções

## Dicas
- `from functools import reduce` para usar reduce
- Tuplas são imutáveis: ideal para dados que não mudam
- `sorted(lista, key=lambda x: x[1], reverse=True)` para ordenar por segundo elemento

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
