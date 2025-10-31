# Projeto 10: Sistema de Monitoramento de Temperatura e Umidade

## 📋 Objetivo

Desenvolver um sistema para monitoramento de temperatura e umidade que permita registrar leituras de sensores, calcular médias, identificar extremos, detectar alertas e gerar relatórios de condições ambientais.

## 🗺️ Diagrama de Contexto

```
┌─────────────────────────────────────────────────────────┐
│    Sistema de Monitoramento Ambiental                  │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐                 │
│  │  Leituras de │───▶│  Processamento│                │
│  │  Sensores    │    │  e Cálculos   │                │
│  └──────────────┘    └──────────────┘                 │
│         │                    │                        │
│         │                    ▼                        │
│         │    ┌──────────────────────────┐             │
│         │    │  Médias, Extremos e      │             │
│         │    │  Alertas                │             │
│         │    └──────────────────────────┘             │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Funcionalidades Básicas

1. **Registro de Leituras** - Registrar leituras (sensor_id, temperatura, umidade, data, hora)
2. **Cálculos** - Calcular média, mínima, máxima por período e sensor
3. **Detecção de Alertas** - Identificar leituras fora da faixa normal
4. **Análises Temporais** - Médias por hora do dia, variação ao longo do tempo
5. **Relatórios** - Relatório por sensor, relatório geral, histórico de alertas

## 📊 Estrutura de Dados

```python
# Entrada
leitura = {
    'sensor_id': 'SENSOR001',
    'temperatura': 25.5,
    'umidade': 65.0,
    'data': '2024-01-15',
    'hora': '14:30',
    'localizacao': 'Sala 101'
}

# Saída
estatisticas_sensor = {
    'sensor_id': 'SENSOR001',
    'temperatura_media': 24.8,
    'temperatura_minima': 22.0,
    'temperatura_maxima': 28.5,
    'umidade_media': 63.5,
    'alertas': 3
}

alertas = [
    {
        'sensor_id': 'SENSOR001',
        'tipo': 'Temperatura Alta',
        'valor': 32.5,
        'limite': 30.0,
        'data': '2024-01-15',
        'hora': '15:00'
    }
]
```

## 💻 Requisitos Técnicos

- Python 3.8+
- Tipos de dados, estruturas de controle, funções, compreensões, manipulação de arquivos

## 📦 Entregáveis

1. Código Python (`sistema_monitoramento.py`)
2. Dados de exemplo (`leituras.txt`)
3. Relatórios gerados
4. Documentação

## 💡 Dicas

- Use listas para armazenar leituras
- Use dict comprehension para agrupar por sensor
- Implemente funções para calcular estatísticas (média, min, max)
- Use filter() para identificar alertas
- Compare valores com limites configuráveis

## 🏗️ Esqueleto do Projeto

```python
# sistema_monitoramento.py

leituras = []  # Lista de todas as leituras
sensores = {}  # {sensor_id: dados_sensor}

# Limites configuráveis
LIMITE_TEMP_MIN = 18.0
LIMITE_TEMP_MAX = 30.0
LIMITE_UMIDADE_MIN = 40.0
LIMITE_UMIDADE_MAX = 80.0

def cadastrar_sensor(sensor_id, localizacao):
    """Cadastra novo sensor."""
    pass

def registrar_leitura(sensor_id, temperatura, umidade, data, hora):
    """Registra nova leitura de sensor."""
    pass

def calcular_estatisticas_sensor(sensor_id):
    """Calcula estatísticas de um sensor."""
    pass

def detectar_alertas(sensor_id=None):
    """Detecta leituras fora dos limites."""
    pass

def calcular_media_por_hora(sensor_id):
    """Calcula média de temperatura por hora do dia."""
    pass

def identificar_extremos():
    """Identifica temperaturas e umidades extremas."""
    pass

def gerar_relatorio_sensor(sensor_id):
    """Gera relatório completo de um sensor."""
    pass

def gerar_relatorio_geral():
    """Gera relatório geral de todos os sensores."""
    pass

def main():
    """Função principal."""
    pass
```

## 📝 Exemplo de Uso

```python
# Cadastrar sensor
cadastrar_sensor('SENSOR001', 'Sala 101')

# Registrar leituras
registrar_leitura('SENSOR001', 25.5, 65.0, '2024-01-15', '14:30')
registrar_leitura('SENSOR001', 32.5, 75.0, '2024-01-15', '15:00')  # Alerta!

# Gerar relatório
relatorio = gerar_relatorio_sensor('SENSOR001')
print(f"Temperatura média: {relatorio['temperatura_media']:.1f}°C")
print(f"Alertas: {relatorio['total_alertas']}")
```

