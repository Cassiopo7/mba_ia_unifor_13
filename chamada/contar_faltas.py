#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para contar faltas de alunos nos encontros
"""

import os
import re
from collections import defaultdict

def processar_arquivo_chamada(caminho_arquivo):
    """Processa um arquivo de chamada e retorna listas de presentes e ausentes"""
    presentes = []
    ausentes = []
    encontro = None
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            
        # Extrair número do encontro
        for linha in linhas:
            if 'Encontro:' in linha:
                encontro = int(linha.split('Encontro:')[1].strip())
                break
        
        # Processar seção de presentes
        em_presentes = False
        em_ausentes = False
        
        for linha in linhas:
            linha = linha.strip()
            
            if 'PRESENTES:' in linha:
                em_presentes = True
                em_ausentes = False
                continue
            elif 'AUSENTES:' in linha:
                em_presentes = False
                em_ausentes = True
                continue
            elif linha.startswith('---'):
                continue
            
            # Extrair matrícula e nome
            match = re.match(r'\d+\.\s*\[([^\]]+)\]\s*(.+)', linha)
            if match:
                matricula = match.group(1)
                nome = match.group(2).strip()
                
                if em_presentes:
                    presentes.append((matricula, nome))
                elif em_ausentes:
                    ausentes.append((matricula, nome))
    
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")
    
    return encontro, presentes, ausentes

def contar_faltas():
    """Conta as faltas de cada aluno em todos os encontros"""
    pasta_data = 'data'
    faltas_por_aluno = defaultdict(int)
    total_encontros = 0
    alunos_info = {}  # Para armazenar nome completo de cada aluno
    
    # Processar cada arquivo de chamada
    arquivos = sorted([f for f in os.listdir(pasta_data) if f.startswith('chamada_') and f.endswith('.txt')])
    
    for arquivo in arquivos:
        caminho = os.path.join(pasta_data, arquivo)
        encontro, presentes, ausentes = processar_arquivo_chamada(caminho)
        
        if encontro:
            total_encontros += 1
            print(f"\n📅 Processando Encontro {encontro}...")
            print(f"   Presentes: {len(presentes)}, Ausentes: {len(ausentes)}")
            
            # Registrar ausentes
            for matricula, nome in ausentes:
                faltas_por_aluno[matricula] += 1
                alunos_info[matricula] = nome
    
    # Gerar relatório
    print("\n" + "="*70)
    print("📊 RELATÓRIO DE FALTAS POR ALUNO")
    print("="*70)
    print(f"\nTotal de encontros analisados: {total_encontros}")
    print(f"Total de alunos com faltas registradas: {len(faltas_por_aluno)}")
    print("\n" + "-"*70)
    
    # Ordenar por número de faltas (decrescente)
    faltas_ordenadas = sorted(faltas_por_aluno.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n{'Matrícula':<15} {'Nome':<45} {'Faltas':<10} {'Taxa de Presença':<15}")
    print("-"*70)
    
    for matricula, num_faltas in faltas_ordenadas:
        nome = alunos_info.get(matricula, "Nome não encontrado")
        taxa_presenca = ((total_encontros - num_faltas) / total_encontros * 100) if total_encontros > 0 else 0
        print(f"{matricula:<15} {nome:<45} {num_faltas:<10} {taxa_presenca:.1f}%")
    
    # Estatísticas gerais
    print("\n" + "="*70)
    print("📈 ESTATÍSTICAS GERAIS")
    print("="*70)
    
    if faltas_ordenadas:
        max_faltas = faltas_ordenadas[0][1]
        alunos_com_max_faltas = [mat for mat, faltas in faltas_ordenadas if faltas == max_faltas]
        
        print(f"\nMaior número de faltas: {max_faltas}")
        print(f"Alunos com {max_faltas} faltas:")
        for matricula in alunos_com_max_faltas:
            print(f"  - [{matricula}] {alunos_info.get(matricula, 'Nome não encontrado')}")
        
        # Alunos sem faltas
        alunos_sem_faltas = []
        todas_matriculas = set()
        for arquivo in arquivos:
            caminho = os.path.join(pasta_data, arquivo)
            _, presentes, ausentes = processar_arquivo_chamada(caminho)
            for mat, nome in presentes + ausentes:
                todas_matriculas.add((mat, nome))
        
        alunos_com_faltas = set(faltas_por_aluno.keys())
        alunos_sem_faltas = [(mat, nome) for mat, nome in todas_matriculas if mat not in alunos_com_faltas]
        
        if alunos_sem_faltas:
            print(f"\n✅ Alunos sem faltas ({len(alunos_sem_faltas)}):")
            for matricula, nome in sorted(alunos_sem_faltas):
                print(f"  - [{matricula}] {nome}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    contar_faltas()

