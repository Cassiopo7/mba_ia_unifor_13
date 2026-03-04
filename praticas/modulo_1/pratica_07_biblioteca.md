# Prática 07 – Sistema de Biblioteca

## Objetivo
Praticar manipulação de strings, operações com listas e dicionários, e compreensões para gestão de acervo.

## Dataset
`datasets/biblioteca_livros.csv`

**Colunas:** ISBN, Titulo, Autor, Genero, Ano_Publicacao, Paginas, Disponivel, Emprestimos

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.2 – Estruturas de Dados Fundamentais (listas, dicionários)
  - Seção 1.4 – Compreensões e Programação Funcional (list e dict comprehension)
  - Seção 1.6 – Manipulação de Arquivos (leitura de CSV e escrita de relatórios)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.2 – Listas e Dicionários (operações, iteração)
  - Seção 4.2 – Transformações Avançadas (operações com strings)

## Tarefas

### Nível Básico
1. Ler o CSV e organizar os livros em uma lista de dicionários
2. Contar quantos livros estão disponíveis e quantos emprestados
3. Encontrar o livro mais antigo e o mais recente
4. Calcular o total de empréstimos de todos os livros

### Nível Intermediário
5. Criar um dicionário {autor: [lista_de_livros]} agrupando livros por autor
6. Usando list comprehension, listar livros com mais de 300 páginas que estão disponíveis
7. Buscar livros cujo título contém uma palavra específica (case insensitive) usando compreensão
8. Calcular a média de páginas por gênero

### Nível Avançado
9. Identificar os 5 livros mais emprestados (mais populares)
10. Criar uma função `recomendar_livro(dados, genero_favorito, max_paginas=500)` que recomende livros disponíveis baseado em preferências
11. Implementar busca parcial por autor e título usando operações de string (lower, find, in)
12. Gerar um relatório `acervo_biblioteca.txt` com: total de livros, livros por gênero, autores mais presentes, livros mais populares

## Dicas
- Use `.lower()` para comparações case insensitive
- `'palavra' in string` verifica se contém a substring
- Dicionários podem ter listas como valores: `dict[key] = dict.get(key, []) + [item]`

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo `acervo_biblioteca.txt` gerado
