# Projeto 07: Sistema de Monitoramento de Segurança Pública

## 📋 Objetivo

Desenvolver um sistema para monitoramento de ocorrências de segurança pública que permita registrar incidentes, calcular estatísticas por tipo, região e período, além de gerar relatórios e identificar padrões.

## 🗺️ Diagrama de Contexto

```
┌─────────────────────────────────────────────────────────┐
│      Sistema de Monitoramento de Segurança             │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐                 │
│  │  Ocorrências │───▶│  Processamento│                │
│  │  (Entrada)   │    │  e Análises   │                │
│  └──────────────┘    └──────────────┘                 │
│         │                    │                        │
│         │                    ▼                        │
│         │    ┌──────────────────────────┐             │
│         │    │  Estatísticas e         │             │
│         │    │  Relatórios             │             │
│         │    └──────────────────────────┘             │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Funcionalidades Básicas

1. **Registro de Ocorrências** - Registrar incidentes (tipo, localização, data, hora, descrição, gravidade)
2. **Análises por Tipo** - Calcular ocorrências por tipo (roubo, furto, acidente, etc.)
3. **Análises por Região** - Agrupar ocorrências por bairro/região
4. **Análises Temporais** - Ocorrências por dia da semana, horário, mês
5. **Identificação de Padrões** - Locais mais críticos, horários de maior incidência
6. **Relatórios** - Relatório geral, por região, por tipo, relatório temporal

## 📊 Estrutura de Dados

```python
# Entrada
ocorrencia = {
    'id': 1,
    'tipo': 'Roubo',
    'localizacao': 'Centro',
    'data': '2024-01-15',
    'hora': '14:30',
    'descricao': 'Roubo de celular',
    'gravidade': 'Alta'
}

# Saída
estatisticas = {
    'total_ocorrencias': 500,
    'por_tipo': {'Roubo': 150, 'Furto': 200},
    'por_regiao': {'Centro': 120, 'Aldeota': 80},
    'horarios_criticos': {'14:00-18:00': 180}
}
```

## 💻 Requisitos Técnicos

- Python 3.8+
- Tipos de dados, estruturas de controle, funções, compreensões, manipulação de arquivos

## 📦 Entregáveis

1. Código Python (`sistema_seguranca.py`)
2. Dados de exemplo (`ocorrencias.txt`)
3. Relatórios gerados
4. Documentação

## 💡 Dicas

- Use dicionários para agrupar por tipo, região, horário
- Use list comprehension para filtrar ocorrências
- Implemente funções para extrair hora, dia da semana
- Use sorted() para criar rankings de locais críticos

## 🏗️ Esqueleto do Projeto

```python
# sistema_seguranca.py

ocorrencias = []
contador_id = 1

TIPOS_OCORRENCIA = ['Roubo', 'Furto', 'Acidente', 'Vandalismo']
GRAVIDADE = ['Baixa', 'Média', 'Alta', 'Crítica']

def registrar_ocorrencia(tipo, localizacao, data, hora, descricao, gravidade):
    """Registra nova ocorrência."""
    pass

def calcular_ocorrencias_por_tipo():
    """Calcula ocorrências agrupadas por tipo."""
    pass

def calcular_ocorrencias_por_regiao():
    """Calcula ocorrências agrupadas por região."""
    pass

def identificar_locais_criticos(limite=5):
    """Identifica locais com mais ocorrências."""
    pass

def analisar_horarios_criticos():
    """Analisa horários de maior incidência."""
    pass

def gerar_relatorio_geral():
    """Gera relatório geral de ocorrências."""
    pass

def main():
    """Função principal."""
    pass
```

