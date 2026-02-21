# Prática 10 – Análise de Dados Clínicos

## Objetivo
Praticar funções com múltiplos retornos, manipulação de dados numéricos, classificação condicional e geração de relatórios.

## Dataset
`datasets/pacientes_clinica.csv`

**Colunas:** ID, Nome, Idade, Sexo, Tipo_Sanguineo, Pressao_Sistolica, Pressao_Diastolica, Glicemia, IMC, Fumante

## Referências do Curso
- **Notebook:** `Programacao_Intensiva_Ciencia_de_Dados.ipynb`
  - Seção 1.1 – Tipos de Dados e Operações Básicas (operações com números decimais)
  - Seção 1.3 – Estruturas de Controle (if/elif/else para classificações clínicas)
  - Seção 1.5 – Funções Avançadas (funções com múltiplos retornos usando dicionário)
  - Seção 1.6 – Manipulação de Arquivos (geração de relatórios)
- **Documentação:** `documentacao_completa.md`
  - Seção 2.3 – Funções (retornos múltiplos, documentação)
  - Seção 2.4 – Programação Funcional (filter para triagem)

## Tarefas

### Nível Básico
1. Ler o CSV e armazenar os dados dos pacientes em estrutura adequada
2. Calcular a idade média dos pacientes e a distribuição por sexo
3. Contar quantos pacientes são fumantes
4. Encontrar a pressão sistólica máxima e mínima

### Nível Intermediário
5. Classificar cada paciente pelo IMC:
   - Abaixo do peso: IMC < 18.5
   - Normal: 18.5 ≤ IMC < 25
   - Sobrepeso: 25 ≤ IMC < 30
   - Obesidade: IMC ≥ 30
6. Classificar a pressão arterial:
   - Normal: sistólica < 120 E diastólica < 80
   - Elevada: sistólica 120-129 E diastólica < 80
   - Hipertensão Estágio 1: sistólica 130-139 OU diastólica 80-89
   - Hipertensão Estágio 2: sistólica ≥ 140 OU diastólica ≥ 90
7. Classificar a glicemia:
   - Normal: < 100
   - Pré-diabetes: 100-125
   - Diabetes: ≥ 126
8. Criar uma função `perfil_paciente(paciente)` que retorne um dicionário com todas as classificações

### Nível Avançado
9. Usar `filter` para identificar pacientes em situação de risco (hipertensos + fumantes + IMC >= 30)
10. Calcular a distribuição de tipos sanguíneos e comparar com a distribuição brasileira típica
11. Criar uma função `triagem(dados, criterios_risco)` que receba critérios configuráveis e retorne pacientes que necessitam atenção
12. Gerar relatório `triagem_pacientes.txt` com: estatísticas gerais, classificação por faixa de risco, lista de pacientes prioritários

## Dicas
- Use if/elif/else aninhados para classificações complexas
- Uma função pode retornar um dicionário com múltiplos valores
- Distribução sanguínea típica no Brasil: O+ (36%), A+ (34%), B+ (8%), AB+ (3%), O- (9%), A- (8%), B- (1%), AB- (1%)

## Entrega
- Notebook (.ipynb) ou script Python (.py) com todas as soluções
- Arquivo `triagem_pacientes.txt` gerado
