# Projeto 09: Sistema de Análise de Desempenho Escolar

## 📋 Objetivo

Desenvolver um sistema para análise de desempenho escolar que permita registrar alunos, notas, calcular médias, identificar alunos com dificuldades e gerar relatórios de aproveitamento por turma e disciplina.

## 🗺️ Diagrama de Contexto

```
┌─────────────────────────────────────────────────────────┐
│      Sistema de Análise de Desempenho Escolar          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐                 │
│  │  Alunos e    │───▶│  Processamento│                │
│  │  Notas       │    │  e Cálculos   │                │
│  └──────────────┘    └──────────────┘                 │
│         │                    │                        │
│         │                    ▼                        │
│         │    ┌──────────────────────────┐             │
│         │    │  Médias e Estatísticas  │             │
│         │    │  de Desempenho          │             │
│         │    └──────────────────────────┘             │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Funcionalidades Básicas

1. **Cadastro de Alunos** - Registrar alunos (matricula, nome, turma, idade)
2. **Registro de Notas** - Registrar notas por disciplina e avaliação
3. **Cálculos** - Calcular média por disciplina, média geral, situação (aprovado/reprovado)
4. **Análises** - Identificar alunos com dificuldades, melhor desempenho por turma, média por disciplina
5. **Relatórios** - Relatório de aluno, relatório de turma, relatório geral

## 📊 Estrutura de Dados

```python
# Entrada
aluno = {
    'matricula': '2024001',
    'nome': 'João Silva',
    'turma': '3º Ano A',
    'idade': 16
}

nota = {
    'matricula': '2024001',
    'disciplina': 'Matemática',
    'avaliacao': 'Prova 1',
    'nota': 8.5,
    'data': '2024-01-15'
}

# Saída
desempenho_aluno = {
    'matricula': '2024001',
    'nome': 'João Silva',
    'medias_por_disciplina': {
        'Matemática': 8.5,
        'Português': 7.0
    },
    'media_geral': 7.75,
    'situacao': 'Aprovado'
}
```

## 💻 Requisitos Técnicos

- Python 3.8+
- Tipos de dados, estruturas de controle, funções, compreensões, manipulação de arquivos

## 📦 Entregáveis

1. Código Python (`sistema_escolar.py`)
2. Dados de exemplo (`alunos.txt`, `notas.txt`)
3. Relatórios gerados
4. Documentação

## 💡 Dicas

- Use dicionários aninhados para organizar notas por aluno e disciplina
- Calcule média ponderada se houver pesos diferentes
- Use list comprehension para filtrar alunos por situação
- Implemente função para classificar situação (aprovado >= 7.0)

## 🏗️ Esqueleto do Projeto

```python
# sistema_escolar.py

alunos = {}  # {matricula: dados_aluno}
notas = []  # Lista de todas as notas

NOTA_MINIMA_APROVACAO = 7.0

def cadastrar_aluno(matricula, nome, turma, idade):
    """Cadastra novo aluno."""
    pass

def registrar_nota(matricula, disciplina, avaliacao, nota, data):
    """Registra nota de avaliação."""
    pass

def calcular_media_disciplina(matricula, disciplina):
    """Calcula média em uma disciplina."""
    pass

def calcular_media_geral(matricula):
    """Calcula média geral do aluno."""
    pass

def classificar_situacao(matricula):
    """Classifica aluno como Aprovado/Reprovado."""
    pass

def identificar_alunos_dificuldades():
    """Identifica alunos com média abaixo de 5.0."""
    pass

def melhor_aluno_turma(turma):
    """Identifica melhor aluno da turma."""
    pass

def gerar_relatorio_aluno(matricula):
    """Gera relatório completo do aluno."""
    pass

def main():
    """Função principal."""
    pass
```

