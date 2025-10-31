# Projeto 06: Sistema de Controle de Pacientes - Área Médica

## 📋 Objetivo

Desenvolver um sistema para controle de pacientes em uma clínica que permita cadastrar pacientes, registrar consultas, calcular estatísticas de atendimentos e gerar relatórios médicos básicos.

## 🗺️ Diagrama de Contexto

```
┌─────────────────────────────────────────────────────────┐
│        Sistema de Controle de Pacientes                │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐                 │
│  │  Pacientes e │───▶│  Processamento│                │
│  │  Consultas   │    │  e Cálculos   │                │
│  └──────────────┘    └──────────────┘                 │
│         │                    │                        │
│         │                    ▼                        │
│         │    ┌──────────────────────────┐             │
│         │    │  Estatísticas e          │             │
│         │    │  Relatórios              │             │
│         │    └──────────────────────────┘             │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Funcionalidades Básicas

1. **Cadastro de Pacientes** - Registrar pacientes (nome, idade, sexo, telefone, histórico)
2. **Registro de Consultas** - Registrar consultas (paciente, médico, data, sintomas, diagnóstico)
3. **Estatísticas** - Calcular atendimentos por médico, doenças mais comuns, pacientes por faixa etária
4. **Relatórios** - Relatório de paciente, relatório geral, histórico médico

## 📊 Estrutura de Dados

```python
# Entrada
paciente = {
    'cpf': '12345678900',
    'nome': 'João Silva',
    'idade': 35,
    'sexo': 'M',
    'telefone': '85999999999'
}

consulta = {
    'paciente_cpf': '12345678900',
    'medico': 'Dr. Maria Santos',
    'data': '2024-01-15',
    'sintomas': 'Dor de cabeça, febre',
    'diagnostico': 'Gripe',
    'medicacao': 'Paracetamol'
}

# Saída
estatisticas = {
    'total_pacientes': 150,
    'total_consultas': 450,
    'doencas_comuns': {'Gripe': 45, 'Hipertensão': 30},
    'atendimentos_por_medico': {'Dr. Maria Santos': 120}
}
```

## 💻 Requisitos Técnicos

- Python 3.8+
- Tipos de dados, estruturas de controle, funções, compreensões, manipulação de arquivos

## 📦 Entregáveis

1. Código Python (`sistema_pacientes.py`)
2. Dados de exemplo (`pacientes.txt`)
3. Relatórios gerados
4. Documentação

## 💡 Dicas

- Use dicionários para pacientes e listas para consultas
- Use set para armazenar CPFs únicos
- Agrupe dados usando dict comprehension
- Implemente funções para cada cálculo estatístico

## 🏗️ Esqueleto do Projeto

```python
# sistema_pacientes.py

pacientes = {}  # {cpf: dados_paciente}
consultas = []  # Lista de consultas

def cadastrar_paciente(cpf, nome, idade, sexo, telefone):
    """Cadastra novo paciente."""
    pass

def registrar_consulta(paciente_cpf, medico, data, sintomas, diagnostico):
    """Registra nova consulta."""
    pass

def calcular_doencas_comuns(limite=5):
    """Identifica doenças mais comuns."""
    pass

def calcular_atendimentos_por_medico():
    """Calcula atendimentos por médico."""
    pass

def gerar_historico_paciente(cpf):
    """Gera histórico médico do paciente."""
    pass

def main():
    """Função principal."""
    pass
```

