#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para converter projetos .md em pastas com README.md e diagramas Mermaid
"""

import os
import re
from pathlib import Path

# Mapeamento de projetos para seus diagramas Mermaid
DIAGRAMAS_MERMAID = {
    'projeto_02_analise_vendas_loja': '''```mermaid
graph TD
    A[Sistema de Análise de Vendas] --> B[Vendas<br/>Entrada]
    B --> C[Processamento<br/>e Análises]
    C --> D[Estatísticas e<br/>Rankings]
    D --> E[Relatórios<br/>Saída]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
    style E fill:#f5e1ff
```''',
    
    'projeto_03_controle_qualidade_produtos': '''```mermaid
graph TD
    A[Sistema de Controle de Qualidade] --> B[Inspeções<br/>Entrada]
    B --> C[Processamento<br/>e Cálculos]
    C --> D[Índices de Qualidade<br/>e Classificações]
    D --> E[Relatórios<br/>e Alertas]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
    style E fill:#f5e1ff
```''',
    
    'projeto_04_sistema_jogo_adivinhacao': '''```mermaid
graph TD
    A[Sistema de Jogo de Adivinhação] --> B[Jogadores<br/>e Jogadas]
    B --> C[Processamento<br/>do Jogo]
    C --> D[Validações e<br/>Resultados]
    D --> E[Estatísticas e<br/>Rankings]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
    style E fill:#f5e1ff
```''',
    
    'projeto_05_controle_obras_engenharia': '''```mermaid
graph TD
    A[Sistema de Controle de Obras] --> B[Obras e<br/>Etapas]
    B --> C[Processamento<br/>e Cálculos]
    C --> D[Progresso e Status<br/>de Obras]
    D --> E[Relatórios<br/>e Alertas]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
    style E fill:#f5e1ff
```''',
    
    'projeto_06_controle_pacientes_medico': '''```mermaid
graph TD
    A[Sistema de Controle de Pacientes] --> B[Pacientes e<br/>Consultas]
    B --> C[Processamento<br/>e Cálculos]
    C --> D[Estatísticas e<br/>Relatórios]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
```''',
    
    'projeto_07_monitoramento_seguranca_publica': '''```mermaid
graph TD
    A[Sistema de Monitoramento de Segurança] --> B[Ocorrências<br/>Entrada]
    B --> C[Processamento<br/>e Análises]
    C --> D[Estatísticas e<br/>Relatórios]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
```''',
    
    'projeto_08_gestao_estoque': '''```mermaid
graph TD
    A[Sistema de Gestão de Estoque] --> B[Produtos e<br/>Movimentações]
    B --> C[Processamento<br/>e Cálculos]
    C --> D[Níveis de Estoque<br/>e Alertas]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
```''',
    
    'projeto_09_analise_desempenho_escolar': '''```mermaid
graph TD
    A[Sistema de Análise de Desempenho Escolar] --> B[Alunos e<br/>Notas]
    B --> C[Processamento<br/>e Cálculos]
    C --> D[Médias e Estatísticas<br/>de Desempenho]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
```''',
    
    'projeto_10_monitoramento_temperatura_umidade': '''```mermaid
graph TD
    A[Sistema de Monitoramento Ambiental] --> B[Leituras de<br/>Sensores]
    B --> C[Processamento<br/>e Cálculos]
    C --> D[Médias, Extremos<br/>e Alertas]
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e7ffe1
    style D fill:#fff5e1
```'''
}

def converter_diagrama_ascii_para_mermaid(conteudo, nome_projeto):
    """Converte diagrama ASCII para Mermaid, se disponível"""
    # Substituir o bloco de diagrama ASCII pelo diagrama Mermaid
    padrao_diagrama = r'```\n.*?```'
    
    if nome_projeto in DIAGRAMAS_MERMAID:
        diagrama_mermaid = DIAGRAMAS_MERMAID[nome_projeto]
        # Substituir a primeira ocorrência do diagrama ASCII
        conteudo = re.sub(padrao_diagrama, diagrama_mermaid, conteudo, count=1, flags=re.DOTALL)
    
    return conteudo

def processar_projeto(arquivo_md, pasta_destino):
    """Processa um arquivo .md e cria README.md na pasta de destino"""
    nome_projeto = Path(arquivo_md).stem
    
    # Ler conteúdo original
    with open(arquivo_md, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Converter diagrama
    conteudo = converter_diagrama_ascii_para_mermaid(conteudo, nome_projeto)
    
    # Criar README.md na pasta de destino
    readme_path = Path(pasta_destino) / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"✓ Processado: {nome_projeto}")

def main():
    base_dir = Path(__file__).parent
    
    # Processar todos os projetos
    for i in range(2, 11):
        nome_projeto = f'projeto_{i:02d}_{"analise_vendas_loja" if i == 2 else "controle_qualidade_produtos" if i == 3 else "sistema_jogo_adivinhacao" if i == 4 else "controle_obras_engenharia" if i == 5 else "controle_pacientes_medico" if i == 6 else "monitoramento_seguranca_publica" if i == 7 else "gestao_estoque" if i == 8 else "analise_desempenho_escolar" if i == 9 else "monitoramento_temperatura_umidade"}'
        
        arquivo_md = base_dir / f'{nome_projeto}.md'
        pasta_destino = base_dir / nome_projeto
        
        if arquivo_md.exists() and pasta_destino.exists():
            processar_projeto(arquivo_md, pasta_destino)
        else:
            print(f"⚠ Arquivo ou pasta não encontrado: {nome_projeto}")

if __name__ == '__main__':
    main()
