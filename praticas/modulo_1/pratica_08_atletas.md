# Prática 08 – Análise de Desempenho de Atletas

## Objetivo
Praticar funções avançadas, ordenação com sorted/lambda, tuplas e operações estatísticas básicas.

## Dataset
`datasets/atletas_corrida.csv`

**Colunas:** Nome, Idade, Sexo, Categoria, Tempo_5km, Tempo_10km, Cidade, Equipe

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.5 – Funções Avançadas (função `calcular_estatisticas` como modelo de função documentada)
  - Seção 1.2 – Estruturas de Dados Fundamentais (tuplas para dados imutáveis, listas para rankings)
  - Seção 1.4 – Compreensões e Programação Funcional (sorted com key=lambda)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.3 – Funções (docstrings, argumentos padrão, *args)
  - Seção 2.2 – Tuplas (unpacking, imutabilidade)

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar em estrutura de dados adequada
2. Calcular o tempo médio na prova de 5km e 10km
3. Encontrar o atleta mais rápido e mais lento em cada prova
4. Contar quantos atletas há por categoria

### Nível Intermediário
5. Criar ranking dos 10 melhores atletas no 5km usando `sorted` com `lambda`
6. Calcular a diferença de tempo entre 5km e 10km para cada atleta (ritmo)
7. Usando tuplas, armazenar (nome, tempo_5km, tempo_10km) e ordenar por tempo total
8. Criar uma função `desempenho_categoria(dados, categoria)` documentada com docstring que retorne estatísticas completas

### Nível Avançado
9. Criar uma função com *args que aceite múltiplos nomes de atletas e compare seus desempenhos
10. Implementar cálculo de mediana sem usar bibliotecas externas (como no notebook, Seção 1.5)
11. Classificar o ritmo de cada atleta: "Elite" (5km < 20min), "Avançado" (20-25), "Intermediário" (25-35), "Iniciante" (>35)
12. Gerar ranking por equipe (tempo médio dos membros) e por cidade

## Dicas
- `sorted(lista, key=lambda x: x['Tempo_5km'])` ordena por tempo
- Tuplas são ideais para dados que não mudam: `ranking = [(nome, tempo) for ...]`
- A mediana requer ordenar os dados primeiro

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
