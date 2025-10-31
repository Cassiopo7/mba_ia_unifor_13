# Projeto 05: Sistema de Controle de Obras de Engenharia Civil

## 📋 Objetivo

Desenvolver um sistema para controle de obras de engenharia civil que permita registrar obras, acompanhar etapas, calcular progresso, gerenciar recursos e gerar relatórios de status das obras.

## 🗺️ Diagrama de Contexto

```
┌─────────────────────────────────────────────────────────┐
│      Sistema de Controle de Obras                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐                 │
│  │   Obras e    │───▶│  Processamento│                │
│  │   Etapas     │    │  e Cálculos   │                │
│  └──────────────┘    └──────────────┘                 │
│         │                    │                        │
│         │                    ▼                        │
│         │    ┌──────────────────────────┐             │
│         │    │  Progresso e Status     │             │
│         │    │  de Obras                │             │
│         │    └──────────────────────────┘             │
│         │                    │                        │
│         └────────────────────┘                        │
│                    │                                   │
│                    ▼                                   │
│            ┌──────────────┐                          │
│            │  Relatórios  │                          │
│            │  e Alertas   │                          │
│            └──────────────┘                          │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Funcionalidades Básicas

1. **Cadastro de Obras**
   - Registrar obra (nome, localização, tipo, data_inicio, orçamento)
   - Definir etapas da obra
   - Atribuir responsáveis

2. **Gestão de Etapas**
   - Registrar etapas (fundação, estrutura, acabamento, etc.)
   - Marcar etapas como concluídas
   - Registrar percentual de conclusão por etapa
   - Calcular progresso geral da obra

3. **Controle de Recursos**
   - Registrar materiais utilizados
   - Registrar mão de obra
   - Calcular custos por etapa
   - Comparar orçado vs realizado

4. **Cálculos**
   - Calcular percentual de conclusão geral
   - Calcular custo total realizado
   - Calcular desvio orçamentário
   - Calcular tempo decorrido vs previsto

5. **Análises**
   - Identificar obras atrasadas
   - Identificar obras acima do orçamento
   - Obras por status (Em planejamento, Em execução, Concluída)
   - Obras por tipo

6. **Relatórios**
   - Relatório de progresso por obra
   - Relatório de custos
   - Relatório de obras atrasadas
   - Relatório geral de todas as obras

## 📊 Estrutura de Dados

### Entrada

```python
# Cadastro de obra
obra = {
    'codigo': 'OBR001',
    'nome': 'Edifício Residencial',
    'localizacao': 'Fortaleza, CE',
    'tipo': 'Residencial',
    'data_inicio': '2024-01-15',
    'data_prevista': '2024-12-15',
    'orcamento': 5000000.00,
    'responsavel': 'Eng. João Silva'
}

# Etapa da obra
etapa = {
    'obra_codigo': 'OBR001',
    'nome': 'Fundação',
    'percentual_conclusao': 100,
    'custo_realizado': 500000.00,
    'custo_orcado': 450000.00,
    'status': 'Concluída',
    'data_conclusao': '2024-02-20'
}
```

### Saída

```python
# Obra completa com progresso
obra_completa = {
    'codigo': 'OBR001',
    'nome': 'Edifício Residencial',
    'progresso_geral': 45.5,
    'custo_realizado': 2275000.00,
    'desvio_orcamento': -725000.00,
    'status': 'Em execução',
    'etapas': [
        {'nome': 'Fundação', 'progresso': 100, 'status': 'Concluída'},
        {'nome': 'Estrutura', 'progresso': 60, 'status': 'Em execução'},
        {'nome': 'Acabamento', 'progresso': 0, 'status': 'Pendente'}
    ]
}

# Relatório de obras
relatorio = {
    'total_obras': 10,
    'obras_concluidas': 3,
    'obras_em_execucao': 5,
    'obras_planejadas': 2,
    'custo_total_orcado': 50000000.00,
    'custo_total_realizado': 22000000.00
}
```

## 💻 Requisitos Técnicos

- Python 3.8+
- Módulo `datetime` para cálculos de datas
- Conhecimentos em:
  - Tipos de dados (int, float, str, dict, list)
  - Estruturas de controle (if/else, for, while)
  - Funções com parâmetros e retorno
  - Compreensões de lista e dicionário
  - Operações com strings (formatação de datas)
  - Operações matemáticas

## 📦 Entregáveis

1. **Código Python** (`sistema_obras.py`)
   - Módulo completo com todas as funcionalidades
   - Cálculos de progresso e custos
   - Sistema de relatórios

2. **Dados de Exemplo** (`obras_exemplo.txt`)
   - Arquivo com obras de exemplo
   - Formato estruturado

3. **Relatórios Gerados** (`relatorios/`)
   - Relatório de progresso
   - Relatório de custos
   - Relatório de obras atrasadas

4. **Documentação** (`README.md`)
   - Instruções de uso
   - Explicação dos cálculos

## 💡 Dicas

1. Use dicionários aninhados para organizar obras e etapas
2. Calcule progresso geral como média ponderada das etapas
3. Use list comprehension para filtrar obras por status
4. Use dict comprehension para agrupar obras por tipo
5. Implemente função para calcular dias entre datas:
   ```python
   from datetime import datetime
   dias = (datetime.strptime(data2, '%Y-%m-%d') - 
           datetime.strptime(data1, '%Y-%m-%d')).days
   ```
6. Use funções para calcular percentuais e desvios
7. Implemente validações (progresso entre 0-100, datas válidas)

## 🏗️ Esqueleto do Projeto

```python
# sistema_obras.py

from datetime import datetime

# ============================================
# Sistema de Controle de Obras
# ============================================

obras = {}  # {codigo: dados_da_obra}
etapas = []  # Lista de todas as etapas

# Status possíveis
STATUS_OBRA = ['Planejamento', 'Em execução', 'Concluída', 'Parada']
STATUS_ETAPA = ['Pendente', 'Em execução', 'Concluída']

# ============================================
# FUNÇÕES DE CADASTRO
# ============================================

def cadastrar_obra(codigo, nome, localizacao, tipo, data_inicio, 
                   data_prevista, orcamento, responsavel):
    """
    Cadastra uma nova obra.
    
    Args:
        codigo (str): Código único da obra
        nome (str): Nome da obra
        localizacao (str): Localização da obra
        tipo (str): Tipo da obra
        data_inicio (str): Data de início (YYYY-MM-DD)
        data_prevista (str): Data prevista de conclusão
        orcamento (float): Orçamento total
        responsavel (str): Responsável pela obra
    
    Returns:
        dict: Dados da obra cadastrada
    """
    # TODO: Validar código único
    # TODO: Criar dicionário da obra
    # TODO: Adicionar ao dicionário obras
    pass

def cadastrar_etapa(obra_codigo, nome, custo_orcado):
    """
    Cadastra uma nova etapa para uma obra.
    
    Args:
        obra_codigo (str): Código da obra
        nome (str): Nome da etapa
        custo_orcado (float): Custo orçado da etapa
    
    Returns:
        dict: Dados da etapa cadastrada
    """
    # TODO: Verificar se obra existe
    # TODO: Criar dicionário da etapa
    # TODO: Adicionar à lista etapas
    pass

# ============================================
# FUNÇÕES DE ATUALIZAÇÃO
# ============================================

def atualizar_progresso_etapa(obra_codigo, nome_etapa, percentual):
    """
    Atualiza percentual de conclusão de uma etapa.
    
    Args:
        obra_codigo (str): Código da obra
        nome_etapa (str): Nome da etapa
        percentual (float): Percentual de conclusão (0-100)
    """
    # TODO: Encontrar etapa
    # TODO: Validar percentual (0-100)
    # TODO: Atualizar percentual
    # TODO: Atualizar status se necessário
    pass

def registrar_custo_etapa(obra_codigo, nome_etapa, custo_realizado):
    """
    Registra custo realizado de uma etapa.
    
    Args:
        obra_codigo (str): Código da obra
        nome_etapa (str): Nome da etapa
        custo_realizado (float): Custo realizado
    """
    # TODO: Encontrar etapa
    # TODO: Atualizar custo realizado
    pass

# ============================================
# FUNÇÕES DE CÁLCULOS
# ============================================

def calcular_progresso_obra(codigo):
    """
    Calcula percentual de progresso geral da obra.
    
    Args:
        codigo (str): Código da obra
    
    Returns:
        float: Percentual de progresso (0-100)
    """
    # TODO: Filtrar etapas da obra
    # TODO: Calcular média dos percentuais
    # TODO: Retornar progresso
    pass

def calcular_custo_realizado(codigo):
    """
    Calcula custo total realizado de uma obra.
    
    Args:
        codigo (str): Código da obra
    
    Returns:
        float: Custo total realizado
    """
    # TODO: Filtrar etapas da obra
    # TODO: Somar custos realizados
    pass

def calcular_desvio_orcamento(codigo):
    """
    Calcula desvio entre orçado e realizado.
    
    Args:
        codigo (str): Código da obra
    
    Returns:
        float: Desvio (positivo = acima, negativo = abaixo)
    """
    # TODO: Obter orçamento da obra
    # TODO: Calcular custo realizado
    # TODO: Calcular diferença
    pass

def calcular_dias_decorridos(codigo):
    """
    Calcula dias decorridos desde o início da obra.
    
    Args:
        codigo (str): Código da obra
    
    Returns:
        int: Quantidade de dias
    """
    # TODO: Obter data de início
    # TODO: Obter data atual
    # TODO: Calcular diferença em dias
    pass

def calcular_atraso(codigo):
    """
    Calcula atraso em dias comparado com data prevista.
    
    Args:
        codigo (str): Código da obra
    
    Returns:
        int: Dias de atraso (negativo se adiantado)
    """
    # TODO: Obter data prevista
    # TODO: Calcular dias decorridos
    # TODO: Calcular diferença
    pass

# ============================================
# FUNÇÕES DE ANÁLISE
# ============================================

def obras_atrasadas():
    """
    Identifica obras com atraso.
    
    Returns:
        list: Lista de códigos de obras atrasadas
    """
    # TODO: Iterar sobre todas as obras
    # TODO: Verificar se está atrasada
    # TODO: Adicionar à lista
    pass

def obras_acima_orcamento():
    """
    Identifica obras acima do orçamento.
    
    Returns:
        list: Lista de códigos de obras acima do orçamento
    """
    # TODO: Calcular desvio para cada obra
    # TODO: Filtrar obras com desvio positivo
    pass

def obras_por_status():
    """
    Agrupa obras por status.
    
    Returns:
        dict: {status: [lista_de_codigos]}
    """
    # TODO: Agrupar obras por status
    # TODO: Usar dict comprehension
    pass

def obras_por_tipo():
    """
    Agrupa obras por tipo.
    
    Returns:
        dict: {tipo: [lista_de_codigos]}
    """
    # TODO: Agrupar obras por tipo
    # TODO: Usar dict comprehension
    pass

# ============================================
# FUNÇÕES DE RELATÓRIOS
# ============================================

def gerar_relatorio_obra(codigo):
    """
    Gera relatório completo de uma obra.
    
    Args:
        codigo (str): Código da obra
    
    Returns:
        dict: Relatório completo da obra
    """
    # TODO: Calcular todas as métricas
    # TODO: Obter lista de etapas
    # TODO: Criar dicionário de relatório
    pass

def gerar_relatorio_geral():
    """
    Gera relatório geral de todas as obras.
    
    Returns:
        dict: Relatório geral
    """
    # TODO: Calcular estatísticas gerais
    # TODO: Contar obras por status
    # TODO: Calcular totais de custos
    # TODO: Criar dicionário de relatório
    pass

def exibir_relatorio():
    """
    Exibe relatório formatado no console.
    """
    # TODO: Formatar e exibir informações
    # TODO: Usar f-strings para formatação
    pass

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def atualizar_status_obra(codigo):
    """
    Atualiza status da obra baseado no progresso.
    
    Args:
        codigo (str): Código da obra
    """
    # TODO: Calcular progresso
    # TODO: Verificar condições
    # TODO: Atualizar status
    pass

def formatar_moeda(valor):
    """
    Formata valor como moeda brasileira.
    
    Args:
        valor (float): Valor a formatar
    
    Returns:
        str: Valor formatado
    """
    # TODO: Formatar com 2 casas decimais
    # TODO: Adicionar símbolo R$
    pass

def dias_entre_datas(data1, data2):
    """
    Calcula dias entre duas datas.
    
    Args:
        data1 (str): Data inicial (YYYY-MM-DD)
        data2 (str): Data final (YYYY-MM-DD)
    
    Returns:
        int: Quantidade de dias
    """
    # TODO: Converter strings para datetime
    # TODO: Calcular diferença
    # TODO: Retornar dias
    pass

# ============================================
# FUNÇÃO PRINCIPAL
# ============================================

def main():
    """
    Função principal do programa.
    """
    # TODO: Menu interativo
    # TODO: Opções: cadastrar obra, etapa, atualizar, relatórios, sair
    pass

if __name__ == "__main__":
    main()
```

## 📝 Exemplo de Uso

```python
# Cadastrar obra
cadastrar_obra(
    codigo='OBR001',
    nome='Edifício Residencial',
    localizacao='Fortaleza, CE',
    tipo='Residencial',
    data_inicio='2024-01-15',
    data_prevista='2024-12-15',
    orcamento=5000000.00,
    responsavel='Eng. João Silva'
)

# Cadastrar etapas
cadastrar_etapa('OBR001', 'Fundação', 450000.00)
cadastrar_etapa('OBR001', 'Estrutura', 2000000.00)
cadastrar_etapa('OBR001', 'Acabamento', 2550000.00)

# Atualizar progresso
atualizar_progresso_etapa('OBR001', 'Fundação', 100)
atualizar_progresso_etapa('OBR001', 'Estrutura', 60)

# Gerar relatório
relatorio = gerar_relatorio_obra('OBR001')
print(f"Progresso: {relatorio['progresso_geral']:.1f}%")
print(f"Custo realizado: {formatar_moeda(relatorio['custo_realizado'])}")
```

