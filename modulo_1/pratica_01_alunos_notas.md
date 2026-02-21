# Prática 01 – Análise de Notas de Alunos

## Objetivo
Praticar tipos de dados, listas, dicionários e funções para análise de dados acadêmicos.

## Dataset
`datasets/alunos_notas.csv`

**Colunas:** Nome, Matricula, Disciplina, Nota1, Nota2, Nota3, Nota4, Frequencia

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.1 – Tipos de Dados e Operações Básicas (operações aritméticas para cálculo de médias)
  - Seção 1.2 – Estruturas de Dados Fundamentais (listas para armazenar notas, dicionários para perfil do aluno)
  - Seção 1.5 – Funções Avançadas (função `calcular_estatisticas` como referência)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.2 – Estruturas de Dados Fundamentais (listas, dicionários)
  - Seção 2.3 – Funções (estrutura, argumentos padrão, docstrings)

## Tarefas

### Nível Básico
1. Ler o arquivo CSV e armazenar os dados em uma lista de dicionários (sem usar pandas)
2. Calcular a média das 4 notas de cada aluno
3. Criar uma lista com os nomes dos alunos aprovados (média >= 7.0 E frequência >= 75%)
4. Contar quantos alunos foram reprovados por nota e quantos por frequência

### Nível Intermediário
5. Criar uma função `calcular_situacao(nota1, nota2, nota3, nota4, frequencia)` que retorne "Aprovado", "Reprovado por Nota", "Reprovado por Frequência" ou "Reprovado por Nota e Frequência"
6. Usando list comprehension, criar uma lista de tuplas (nome, media) apenas dos alunos com média acima de 8.0
7. Criar um dicionário onde a chave é a disciplina e o valor é a média geral daquela disciplina
8. Encontrar o aluno com a maior e a menor média geral

### Nível Avançado
9. Criar uma função `relatorio_turma(dados, disciplina)` que receba os dados e o nome de uma disciplina e retorne um dicionário com: média da turma, maior nota, menor nota, quantidade de aprovados, quantidade de reprovados
10. Usar `map` e `lambda` para criar uma lista com as médias de todos os alunos
11. Usar `filter` para obter apenas os registros de uma disciplina específica
12. Gerar um arquivo de texto `resultado_alunos.txt` com o nome, média e situação de cada aluno

## Dicas
- Relembre como ler arquivos na Seção 1.6 do notebook
- Use a função `split()` para separar os campos de cada linha do CSV
- Lembre-se de converter strings para float ao trabalhar com notas

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo `resultado_alunos.txt` gerado pelo exercício 12
