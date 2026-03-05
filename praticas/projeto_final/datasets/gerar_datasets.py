"""
Gerador de Datasets Investigativos — Projeto Final
MBA Ciência de Dados - UNIFOR - Turma 13
Professor: Cássio Pinheiro

Gera 30 CSVs (3 por projeto) com padrões ocultos plantados para investigação.
Cada projeto é uma operação investigativa onde o aluno precisa cruzar datasets
para descobrir fraudes, anomalias ou crises.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
import hashlib

np.random.seed(42)
random.seed(42)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# PROJETO 01 — Operação Bisturi: Auditoria de Fraude Hospitalar
# Padrões ocultos:
#   - Hospitais "Regional Norte", "Municipal Leste", "Clínica Esperança"
#     têm padrões incompatíveis (muitas internações + poucos leitos + custo alto)
#   - Procedimentos duplicados no mesmo paciente/dia
#   - Picos de faturamento em março e setembro (fechamento de meta)
# ============================================================
def gerar_projeto_01():
    unidades = [f"Hospital {c}" for c in [
        "São José", "Santa Casa", "Regional Norte", "Regional Sul",
        "Universitário", "Municipal Centro", "Municipal Leste", "Maternidade Vida",
        "Pronto-Socorro 24h", "Clínica Esperança", "Hospital do Coração", "Oncológico",
        "Infantil Anjo", "Ortopédico Plus", "Saúde Mental"
    ]]
    especialidades = ["Clínica Médica", "Cirurgia Geral", "Pediatria", "Ortopedia",
                      "Cardiologia", "Obstetrícia", "Neurologia", "Oncologia"]

    # Unidades suspeitas de fraude
    SUSPEITAS = ["Hospital Regional Norte", "Hospital Municipal Leste", "Hospital Clínica Esperança"]

    # --- Dataset 1: indicadores_hospitalares.csv ---
    rows = []
    for ano in [2022, 2023, 2024]:
        for mes in range(1, 13):
            for unidade in unidades:
                is_suspect = unidade in SUSPEITAS
                for esp in random.sample(especialidades, random.randint(3, 6)):
                    leitos_total = random.randint(20, 80)
                    if is_suspect:
                        leitos_total = random.randint(15, 35)  # Poucos leitos

                    base_ocupacao = random.gauss(0.72, 0.12)
                    if mes in [6, 7]:
                        base_ocupacao += 0.08
                    ocupacao = np.clip(base_ocupacao, 0.3, 0.98)

                    internacoes = int(leitos_total * ocupacao * random.uniform(1.5, 3.0))
                    if is_suspect:
                        internacoes = int(internacoes * random.uniform(2.5, 4.0))  # Muitas internações vs leitos

                    tempo_medio = max(1, random.gauss(5.5, 2.5))
                    taxa_reinternacao = max(0, random.gauss(0.08, 0.04))
                    obitos = max(0, int(internacoes * random.gauss(0.03, 0.015)))

                    custo_medio_internacao = round(max(500, random.gauss(3500, 1000)), 2)
                    if is_suspect:
                        custo_medio_internacao = round(custo_medio_internacao * random.uniform(1.8, 2.5), 2)

                    # Picos de faturamento em meses de fechamento de meta
                    if is_suspect and mes in [3, 9]:
                        internacoes = int(internacoes * 1.6)
                        custo_medio_internacao *= 1.3

                    faixa_etaria = random.choice(["0-14", "15-29", "30-49", "50-64", "65+"])
                    tipo_internacao = random.choice(["Urgência", "Eletiva", "Urgência", "Urgência"])

                    rows.append({
                        "ano": ano, "mes": mes, "unidade": unidade,
                        "especialidade": esp, "leitos_disponiveis": leitos_total,
                        "taxa_ocupacao": round(ocupacao, 3),
                        "internacoes": internacoes,
                        "tempo_medio_internacao_dias": round(tempo_medio, 1),
                        "taxa_reinternacao_30d": round(taxa_reinternacao, 3),
                        "obitos": obitos,
                        "custo_medio_internacao": custo_medio_internacao,
                        "faixa_etaria_predominante": faixa_etaria,
                        "tipo_internacao": tipo_internacao
                    })

    df = pd.DataFrame(rows)
    mask_null = np.random.random(len(df)) < 0.03
    df.loc[mask_null, "taxa_reinternacao_30d"] = np.nan
    mask_null2 = np.random.random(len(df)) < 0.02
    df.loc[mask_null2, "tempo_medio_internacao_dias"] = np.nan
    dupes = df.sample(15)
    df = pd.concat([df, dupes], ignore_index=True)
    idx_out = df.sample(5).index
    df.loc[idx_out, "tempo_medio_internacao_dias"] = np.random.uniform(30, 60, 5).round(1)

    df.to_csv(f"{OUTPUT_DIR}/projeto_01_indicadores_hospitalares.csv", index=False)
    print(f"  P01 - indicadores_hospitalares: {len(df)} registros")

    # --- Dataset 2: registro_procedimentos.csv ---
    proc_rows = []
    proc_tipos = ["Consulta", "Exame Laboratorial", "Exame Imagem", "Cirurgia Simples",
                  "Cirurgia Complexa", "Internação UTI", "Procedimento Ambulatorial"]
    proc_custos = {"Consulta": 150, "Exame Laboratorial": 80, "Exame Imagem": 350,
                   "Cirurgia Simples": 2500, "Cirurgia Complexa": 12000,
                   "Internação UTI": 4500, "Procedimento Ambulatorial": 600}

    paciente_counter = 1
    for _ in range(12000):
        unidade = random.choice(unidades)
        is_suspect = unidade in SUSPEITAS
        ano = random.choice([2022, 2023, 2024])
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        data = f"{ano}-{mes:02d}-{dia:02d}"
        paciente_id = f"PAC-{random.randint(1, 3000):05d}"
        proc = random.choice(proc_tipos)

        custo = max(20, random.gauss(proc_custos[proc], proc_custos[proc] * 0.3))
        if is_suspect:
            custo *= random.uniform(1.5, 2.2)  # Superfaturamento

        proc_rows.append({
            "procedimento_id": f"PROC-{len(proc_rows)+1:06d}",
            "unidade": unidade,
            "paciente_id": paciente_id,
            "data_procedimento": data,
            "tipo_procedimento": proc,
            "valor_cobrado": round(custo, 2),
            "convenio": random.choice(["SUS", "SUS", "SUS", "Plano A", "Plano B", "Particular"])
        })

    # Inserir procedimentos duplicados (pacientes fantasma) nas unidades suspeitas
    for _ in range(200):
        base = random.choice([r for r in proc_rows if r["unidade"] in SUSPEITAS])
        dup = base.copy()
        dup["procedimento_id"] = f"PROC-{len(proc_rows)+1:06d}"
        # Mesmo paciente, mesma data, mesmo procedimento = duplicata suspeita
        proc_rows.append(dup)

    df_proc = pd.DataFrame(proc_rows)
    df_proc.to_csv(f"{OUTPUT_DIR}/projeto_01_registro_procedimentos.csv", index=False)
    print(f"  P01 - registro_procedimentos: {len(df_proc)} registros")

    # --- Dataset 3: denuncias_anonimas.csv ---
    den_rows = []
    pistas = [
        ("Hospital Regional Norte", "Pacientes dizem que nunca foram internados mas constam no sistema"),
        ("Hospital Regional Norte", "Funcionário relatou pressão para registrar procedimentos fictícios"),
        ("Hospital Municipal Leste", "Médico cobra por cirurgias que não aconteceram"),
        ("Hospital Municipal Leste", "Equipamento de raio-X quebrado há 6 meses mas exames continuam sendo cobrados"),
        ("Hospital Clínica Esperança", "Ambulâncias vazias saem e voltam — possível transporte fantasma"),
        ("Hospital Clínica Esperança", "Farmácia recebe medicamentos mas pacientes relatam falta"),
        ("Hospital São José", "Reclamação sobre demora no atendimento — sem indícios de fraude"),
        ("Hospital Universitário", "Elogio ao atendimento do setor de cardiologia"),
    ]
    for i, (unidade, relato) in enumerate(pistas):
        den_rows.append({
            "denuncia_id": f"DEN-{i+1:04d}",
            "data_denuncia": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            "unidade_mencionada": unidade,
            "canal": random.choice(["Ouvidoria", "E-mail anônimo", "Telefone 0800"]),
            "relato_resumido": relato,
            "classificacao": "Fraude" if unidade in SUSPEITAS else "Outros",
            "status": random.choice(["Em análise", "Encaminhada", "Arquivada"])
        })

    df_den = pd.DataFrame(den_rows)
    df_den.to_csv(f"{OUTPUT_DIR}/projeto_01_denuncias_anonimas.csv", index=False)
    print(f"  P01 - denuncias_anonimas: {len(df_den)} registros")


# ============================================================
# PROJETO 02 — Operação Marketplace: Fraude em E-commerce
# Padrões ocultos:
#   - Cluster de vendedores (VEND-0042 a VEND-0046) com reviews idênticos
#   - Vendas concentradas entre 2h-5h da manhã
#   - Avaliações 5 estrelas de contas com < 7 dias de criação
# ============================================================
def gerar_projeto_02():
    categorias = ["Moda Feminina", "Moda Masculina", "Eletrônicos", "Casa & Decoração",
                  "Esporte & Lazer", "Beleza & Saúde", "Infantil", "Acessórios"]
    estados = ["CE", "SP", "RJ", "MG", "BA", "PE", "PA", "RS", "PR", "GO", "MA", "PI", "RN", "PB", "SE"]
    pesos_estados = [0.25, 0.15, 0.10, 0.08, 0.07, 0.06, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.03, 0.02]

    VENDEDORES_FRAUD = [f"VEND-{i:04d}" for i in range(42, 47)]  # 5 vendedores fraudulentos

    # --- Dataset 1: ecommerce_vendas.csv ---
    rows = []
    base_date = datetime(2023, 1, 1)
    for i in range(8000):
        dias = random.randint(0, 729)
        data = base_date + timedelta(days=dias)

        vendedor_id = f"VEND-{random.randint(1, 120):04d}"
        is_fraud = vendedor_id in VENDEDORES_FRAUD

        # Vendas fraudulentas concentradas em horários atípicos
        if is_fraud and random.random() < 0.7:
            hora = random.randint(2, 5)
        else:
            hora = random.choices(range(24), weights=[1,1,1,1,1,2,3,5,7,8,9,10,9,8,9,10,9,8,7,6,5,4,3,2])[0]
        minuto = random.randint(0, 59)

        cat = random.choices(categorias, weights=[0.18, 0.12, 0.20, 0.15, 0.10, 0.10, 0.08, 0.07])[0]
        estado = random.choices(estados, weights=pesos_estados)[0]

        preco_base = {"Moda Feminina": 120, "Moda Masculina": 150, "Eletrônicos": 450,
                      "Casa & Decoração": 200, "Esporte & Lazer": 180, "Beleza & Saúde": 80,
                      "Infantil": 90, "Acessórios": 60}
        preco = max(15, random.gauss(preco_base[cat], preco_base[cat] * 0.4))
        qtd = random.choices([1, 1, 1, 2, 2, 3], weights=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05])[0]

        status_opcoes = ["Entregue", "Entregue", "Entregue", "Entregue", "Entregue",
                         "Cancelado", "Devolvido", "Em trânsito"]
        status = random.choice(status_opcoes)
        nota = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.08, 0.15, 0.32, 0.40])[0] if status == "Entregue" else np.nan
        frete = round(random.uniform(5, 45), 2)

        rows.append({
            "pedido_id": f"PED-{i+1:06d}",
            "data_pedido": data.strftime("%Y-%m-%d"),
            "hora_pedido": f"{hora:02d}:{minuto:02d}",
            "vendedor_id": vendedor_id,
            "categoria": cat,
            "produto_id": f"PROD-{random.randint(1, 500):04d}",
            "preco_unitario": round(preco, 2),
            "quantidade": qtd,
            "valor_total": round(preco * qtd, 2),
            "frete": frete,
            "estado_cliente": estado,
            "status_pedido": status,
            "nota_avaliacao": nota
        })

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.02
    df.loc[mask, "preco_unitario"] = df.loc[mask, "preco_unitario"].astype(str) + " "
    mask_null = np.random.random(len(df)) < 0.03
    df.loc[mask_null, "frete"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_02_ecommerce_vendas.csv", index=False)
    print(f"  P02 - ecommerce_vendas: {len(df)} registros")

    # --- Dataset 2: vendedores_perfil.csv ---
    vend_rows = []
    for i in range(1, 121):
        vid = f"VEND-{i:04d}"
        is_fraud = vid in VENDEDORES_FRAUD

        data_cadastro = base_date - timedelta(days=random.randint(30, 1000))
        if is_fraud:
            # Cadastrados em datas muito próximas
            data_cadastro = datetime(2023, 3, 10) + timedelta(days=random.randint(0, 3))

        cidade = random.choice(["Fortaleza", "São Paulo", "Rio de Janeiro", "Recife", "Belo Horizonte",
                                "Salvador", "Curitiba", "Brasília", "Manaus", "Porto Alegre"])
        if is_fraud:
            cidade = "Fortaleza"  # Todos do mesmo lugar

        vend_rows.append({
            "vendedor_id": vid,
            "nome_loja": f"Loja {''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))}" if not is_fraud
                         else f"Loja {'XYZ'}{random.randint(1,5):02d}",
            "data_cadastro": data_cadastro.strftime("%Y-%m-%d"),
            "cidade": cidade,
            "estado": "CE" if is_fraud else random.choice(estados),
            "categoria_principal": random.choice(categorias),
            "total_vendas": random.randint(50, 2000) if not is_fraud else random.randint(800, 1500),
            "nota_media_loja": round(random.gauss(4.0, 0.5), 1) if not is_fraud else round(random.uniform(4.8, 5.0), 1),
            "reclamacoes": random.randint(0, 30) if not is_fraud else random.randint(0, 2),
            "verificado": random.choice([True, False]) if not is_fraud else False
        })

    df_vend = pd.DataFrame(vend_rows)
    df_vend.to_csv(f"{OUTPUT_DIR}/projeto_02_vendedores_perfil.csv", index=False)
    print(f"  P02 - vendedores_perfil: {len(df_vend)} registros")

    # --- Dataset 3: avaliacoes_suspeitas.csv ---
    aval_rows = []
    ips_fraud = [f"192.168.1.{random.randint(100, 105)}" for _ in range(3)]

    for i in range(3000):
        vendedor_id = f"VEND-{random.randint(1, 120):04d}"
        is_fraud_review = vendedor_id in VENDEDORES_FRAUD

        data_review = base_date + timedelta(days=random.randint(0, 729))
        data_conta_criada = data_review - timedelta(days=random.randint(30, 730))

        if is_fraud_review and random.random() < 0.6:
            # Conta recém-criada
            data_conta_criada = data_review - timedelta(days=random.randint(1, 6))
            nota = 5
            ip = random.choice(ips_fraud)
            texto = random.choice([
                "Excelente produto! Recomendo muito!",
                "Entrega rápida e produto de qualidade!",
                "Superou minhas expectativas! 10/10",
                "Melhor compra que já fiz! Recomendo!",
                "Produto incrível, vendedor nota 10!"
            ])
        else:
            nota = random.choices([1, 2, 3, 4, 5], weights=[0.08, 0.10, 0.15, 0.30, 0.37])[0]
            ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            texto = random.choice([
                "Produto ok, dentro do esperado.",
                "Demorou um pouco mas chegou bem.",
                "Não gostei da qualidade.",
                "Bom produto pelo preço.",
                "Recomendo, boa experiência.",
                "Veio com defeito, pedi troca.",
                "Excelente custo-benefício.",
                "Produto diferente da foto.",
                np.nan
            ])

        aval_rows.append({
            "avaliacao_id": f"AVAL-{i+1:05d}",
            "vendedor_id": vendedor_id,
            "comprador_id": f"COMP-{random.randint(1, 5000):05d}",
            "data_avaliacao": data_review.strftime("%Y-%m-%d"),
            "data_criacao_conta": data_conta_criada.strftime("%Y-%m-%d"),
            "nota": nota,
            "ip_origem": ip,
            "texto_avaliacao": texto
        })

    df_aval = pd.DataFrame(aval_rows)
    df_aval.to_csv(f"{OUTPUT_DIR}/projeto_02_avaliacoes_suspeitas.csv", index=False)
    print(f"  P02 - avaliacoes_suspeitas: {len(df_aval)} registros")


# ============================================================
# PROJETO 03 — Alerta Vermelho: Crise Ambiental Misteriosa
# Padrões ocultos:
#   - "Jurema" (industrial) emite SO2/NO2 altíssimos entre 22h-4h
#   - Correlação com internações respiratórias nos bairros próximos
#   - A indústria "QuimNorte Ltda" é a fonte (cadastro_industrias)
# ============================================================
def gerar_projeto_03():
    estacoes = {
        "Centro": "urbana", "Distrito Industrial": "industrial",
        "Aldeota": "residencial", "Messejana": "residencial",
        "Porto": "industrial", "Parque do Cocó": "parque",
        "Maraponga": "residencial", "Jurema": "industrial"
    }

    ESTACAO_CRIMINOSA = "Jurema"

    # --- Dataset 1: qualidade_ar.csv ---
    rows = []
    base_date = datetime(2023, 1, 1)
    for dia in range(730):
        data = base_date + timedelta(days=dia)
        mes = data.month
        seco = mes in [7, 8, 9, 10, 11, 12]

        for estacao, tipo in estacoes.items():
            for hora in [0, 6, 12, 18, 22]:  # Adicionando 22h
                base_mp25 = {"urbana": 22, "industrial": 35, "residencial": 15, "parque": 10}[tipo]
                base_mp10 = base_mp25 * 1.8

                if seco:
                    base_mp25 *= 1.3
                    base_mp10 *= 1.25

                if hora == 12:
                    mult = 1.2
                elif hora == 18:
                    mult = 1.15
                elif hora == 22:
                    mult = 0.8
                else:
                    mult = 0.85

                mp25 = max(1, random.gauss(base_mp25 * mult, base_mp25 * 0.25))
                mp10 = max(2, random.gauss(base_mp10 * mult, base_mp10 * 0.2))
                o3 = max(0, random.gauss(40 * mult, 15))
                no2 = max(0, random.gauss(25 * (1.3 if tipo == "industrial" else 1) * mult, 10))
                so2 = max(0, random.gauss(8 * (2.0 if tipo == "industrial" else 1), 4))
                temp = random.gauss(28 + (2 if seco else -1) + (3 if hora == 12 else -2 if hora in [0, 22] else 0), 2)
                umidade = random.gauss(70 + (-15 if seco else 10) + (-10 if hora == 12 else 5), 8)

                # PADRÃO OCULTO: Jurema com emissões altíssimas à noite
                if estacao == ESTACAO_CRIMINOSA and hora in [22, 0]:
                    so2 = max(5, random.gauss(55, 12))  # 5x o normal
                    no2 = max(5, random.gauss(70, 15))   # 3x o normal
                    mp25 *= 2.5
                    mp10 *= 2.2

                rows.append({
                    "data": data.strftime("%Y-%m-%d"),
                    "hora": hora,
                    "estacao": estacao,
                    "tipo_zona": tipo,
                    "mp25_ugm3": round(mp25, 1),
                    "mp10_ugm3": round(mp10, 1),
                    "o3_ugm3": round(o3, 1),
                    "no2_ugm3": round(no2, 1),
                    "so2_ugm3": round(so2, 1),
                    "temperatura_c": round(temp, 1),
                    "umidade_relativa_pct": round(np.clip(umidade, 20, 100), 1)
                })

    df = pd.DataFrame(rows)
    for col in ["mp25_ugm3", "mp10_ugm3", "o3_ugm3"]:
        mask = np.random.random(len(df)) < 0.04
        df.loc[mask, col] = np.nan
    idx_err = df.sample(20).index
    df.loc[idx_err, "no2_ugm3"] = -df.loc[idx_err, "no2_ugm3"].abs()

    df.to_csv(f"{OUTPUT_DIR}/projeto_03_qualidade_ar.csv", index=False)
    print(f"  P03 - qualidade_ar: {len(df)} registros")

    # --- Dataset 2: internacoes_respiratorias.csv ---
    bairros = ["Centro", "Aldeota", "Messejana", "Maraponga", "Jurema", "Montese",
               "Parquelândia", "Papicu", "Cocó", "Edson Queiroz"]
    BAIRROS_AFETADOS = ["Jurema", "Maraponga", "Messejana"]  # Próximos à fonte

    int_rows = []
    for dia in range(730):
        data = base_date + timedelta(days=dia)
        mes = data.month

        for bairro in bairros:
            is_affected = bairro in BAIRROS_AFETADOS
            # Base de internações diárias
            n_internacoes = np.random.poisson(2 if not is_affected else 5)

            # Bairros afetados têm mais internações (correlação com emissões noturnas)
            if is_affected and mes in [7, 8, 9, 10, 11, 12]:  # Período seco = pior dispersão
                n_internacoes = np.random.poisson(9)

            for _ in range(n_internacoes):
                idade = int(np.clip(random.gauss(55, 20), 2, 92))
                int_rows.append({
                    "internacao_id": f"INT-{len(int_rows)+1:06d}",
                    "data_internacao": data.strftime("%Y-%m-%d"),
                    "bairro_residencia": bairro,
                    "idade_paciente": idade,
                    "sexo": random.choice(["M", "F"]),
                    "diagnostico": random.choices(
                        ["Asma", "Bronquite", "DPOC", "Pneumonia", "Rinite Alérgica", "Infecção Respiratória"],
                        weights=[0.20, 0.15, 0.15, 0.20, 0.15, 0.15]
                    )[0],
                    "gravidade": random.choices(["Leve", "Moderada", "Grave"], weights=[0.4, 0.35, 0.25])[0],
                    "dias_internacao": max(1, int(random.gauss(4, 2))),
                    "uti": random.choices([0, 1], weights=[0.85, 0.15])[0]
                })

    df_int = pd.DataFrame(int_rows)
    df_int.to_csv(f"{OUTPUT_DIR}/projeto_03_internacoes_respiratorias.csv", index=False)
    print(f"  P03 - internacoes_respiratorias: {len(df_int)} registros")

    # --- Dataset 3: cadastro_industrias.csv ---
    ind_rows = [
        {"industria_id": "IND-001", "nome": "QuimNorte Ltda", "bairro": "Jurema",
         "tipo_atividade": "Química Industrial", "porte": "Grande",
         "licenca_ambiental": "Vencida", "data_ultima_fiscalizacao": "2021-08-15",
         "horario_operacao_declarado": "08:00-18:00", "emissoes_declaradas_ton_ano": 12.5},
        {"industria_id": "IND-002", "nome": "MetalForte S.A.", "bairro": "Distrito Industrial",
         "tipo_atividade": "Metalurgia", "porte": "Grande",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2024-03-20",
         "horario_operacao_declarado": "06:00-22:00", "emissoes_declaradas_ton_ano": 8.3},
        {"industria_id": "IND-003", "nome": "CerâmicaCE", "bairro": "Porto",
         "tipo_atividade": "Cerâmica", "porte": "Médio",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2024-01-10",
         "horario_operacao_declarado": "07:00-17:00", "emissoes_declaradas_ton_ano": 5.1},
        {"industria_id": "IND-004", "nome": "PlastCE Indústria", "bairro": "Jurema",
         "tipo_atividade": "Plásticos", "porte": "Médio",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2023-11-05",
         "horario_operacao_declarado": "08:00-18:00", "emissoes_declaradas_ton_ano": 3.2},
        {"industria_id": "IND-005", "nome": "TêxtilNordeste", "bairro": "Maraponga",
         "tipo_atividade": "Têxtil", "porte": "Pequeno",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2024-06-01",
         "horario_operacao_declarado": "07:00-17:00", "emissoes_declaradas_ton_ano": 1.8},
        {"industria_id": "IND-006", "nome": "AlimentosBR", "bairro": "Messejana",
         "tipo_atividade": "Alimentos", "porte": "Médio",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2024-04-22",
         "horario_operacao_declarado": "06:00-20:00", "emissoes_declaradas_ton_ano": 2.0},
        {"industria_id": "IND-007", "nome": "SolventeCE", "bairro": "Distrito Industrial",
         "tipo_atividade": "Química Industrial", "porte": "Pequeno",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2024-02-18",
         "horario_operacao_declarado": "08:00-17:00", "emissoes_declaradas_ton_ano": 4.5},
        {"industria_id": "IND-008", "nome": "AutoPeças CE", "bairro": "Porto",
         "tipo_atividade": "Autopeças", "porte": "Médio",
         "licenca_ambiental": "Vigente", "data_ultima_fiscalizacao": "2023-09-30",
         "horario_operacao_declarado": "08:00-18:00", "emissoes_declaradas_ton_ano": 3.8},
    ]

    df_ind = pd.DataFrame(ind_rows)
    df_ind.to_csv(f"{OUTPUT_DIR}/projeto_03_cadastro_industrias.csv", index=False)
    print(f"  P03 - cadastro_industrias: {len(df_ind)} registros")


# ============================================================
# PROJETO 04 — Operação Nota Inflada: Fraude Educacional
# Padrões ocultos:
#   - Escolas "Epsilon", "Zeta", "Eta" inflam notas internas
#   - Notas internas >> notas externas (SAEB) nessas escolas
#   - Salto repentino de notas em anos de meta (2023)
#   - Distribuição "perfeita demais" (variância muito baixa)
# ============================================================
def gerar_projeto_04():
    escolas = [f"Escola {c}" for c in ["Alpha", "Beta", "Gamma", "Delta", "Epsilon",
               "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu"]]
    series = ["6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Médio", "2º Médio", "3º Médio"]
    turnos = ["Manhã", "Tarde"]

    ESCOLAS_FRAUDE = ["Escola Epsilon", "Escola Zeta", "Escola Eta"]

    # --- Dataset 1: desempenho_educacional.csv ---
    rows = []
    aluno_id = 1
    for ano in [2021, 2022, 2023, 2024]:
        for escola in escolas:
            is_fraud = escola in ESCOLAS_FRAUDE
            for serie in series:
                for turno in turnos:
                    n_alunos = random.randint(25, 40)
                    for _ in range(n_alunos):
                        idade = int(serie[0]) + random.choice([10, 11, 12]) if "Ano" in serie else int(serie[0]) + 14 + random.choice([0, 1])
                        sexo = random.choice(["M", "F"])

                        renda_familiar = random.choices(
                            ["Até 1 SM", "1-2 SM", "2-3 SM", "3-5 SM", "5+ SM"],
                            weights=[0.20, 0.30, 0.25, 0.15, 0.10]
                        )[0]
                        esc_pais = random.choices(
                            ["Fundamental Incompleto", "Fundamental Completo", "Médio Completo", "Superior Completo", "Pós-graduação"],
                            weights=[0.15, 0.20, 0.35, 0.20, 0.10]
                        )[0]
                        internet = random.choices([1, 0], weights=[0.75, 0.25])[0]

                        base = 55
                        if renda_familiar in ["3-5 SM", "5+ SM"]:
                            base += 8
                        if esc_pais in ["Superior Completo", "Pós-graduação"]:
                            base += 6
                        if internet:
                            base += 4

                        frequencia = np.clip(random.gauss(0.85, 0.10), 0.40, 1.0)
                        if frequencia < 0.75:
                            base -= 15

                        nota_mat = np.clip(random.gauss(base, 12), 0, 100)
                        nota_port = np.clip(random.gauss(base + 3, 11), 0, 100)

                        # FRAUDE: inflar notas
                        if is_fraud:
                            inflacao = 15  # base inflation
                            if ano == 2023:  # ano de meta
                                inflacao = 25
                            nota_mat = np.clip(nota_mat + inflacao, 0, 100)
                            nota_port = np.clip(nota_port + inflacao, 0, 100)
                            # Variância artificialmente baixa (notas "perfeitas demais")
                            nota_mat = np.clip(nota_mat + random.gauss(0, 3), max(65, nota_mat - 5), 100)
                            nota_port = np.clip(nota_port + random.gauss(0, 3), max(65, nota_port - 5), 100)

                        rows.append({
                            "aluno_id": f"ALU-{aluno_id:05d}",
                            "ano_letivo": ano,
                            "escola": escola,
                            "serie": serie,
                            "turno": turno,
                            "idade": idade,
                            "sexo": sexo,
                            "renda_familiar": renda_familiar,
                            "escolaridade_pais": esc_pais,
                            "acesso_internet": internet,
                            "frequencia_pct": round(frequencia * 100, 1),
                            "nota_matematica": round(nota_mat, 1),
                            "nota_portugues": round(nota_port, 1),
                            "nota_media_geral": round((nota_mat + nota_port) / 2, 1)
                        })
                        aluno_id += 1

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.05
    df.loc[mask, "renda_familiar"] = np.nan
    mask2 = np.random.random(len(df)) < 0.03
    df.loc[mask2, "escolaridade_pais"] = np.nan
    dupes = df.sample(20)
    df = pd.concat([df, dupes], ignore_index=True)

    df.to_csv(f"{OUTPUT_DIR}/projeto_04_desempenho_educacional.csv", index=False)
    print(f"  P04 - desempenho_educacional: {len(df)} registros")

    # --- Dataset 2: historico_avaliacoes_externas.csv ---
    ext_rows = []
    for ano in [2021, 2022, 2023, 2024]:
        for escola in escolas:
            is_fraud = escola in ESCOLAS_FRAUDE
            for serie in ["5º Ano", "9º Ano", "3º Médio"]:
                # Nota externa (SAEB) - não pode ser inflada
                nota_ext_mat = np.clip(random.gauss(55, 12), 20, 95)
                nota_ext_port = np.clip(random.gauss(53, 11), 20, 95)

                # Nota interna média daquela escola/série
                nota_int_mat = nota_ext_mat + random.gauss(3, 5)  # Normalmente próximas
                nota_int_port = nota_ext_port + random.gauss(3, 5)

                if is_fraud:
                    # Gap enorme entre interna e externa
                    nota_int_mat = nota_ext_mat + random.gauss(22, 4)
                    nota_int_port = nota_ext_port + random.gauss(20, 4)
                    if ano == 2023:
                        nota_int_mat += 8
                        nota_int_port += 8

                ext_rows.append({
                    "ano": ano,
                    "escola": escola,
                    "serie_avaliada": serie,
                    "nota_saeb_matematica": round(nota_ext_mat, 1),
                    "nota_saeb_portugues": round(nota_ext_port, 1),
                    "nota_interna_media_matematica": round(np.clip(nota_int_mat, 0, 100), 1),
                    "nota_interna_media_portugues": round(np.clip(nota_int_port, 0, 100), 1),
                    "numero_alunos_avaliados": random.randint(60, 150),
                    "taxa_participacao_pct": round(np.clip(random.gauss(88, 8), 50, 100), 1)
                })

    df_ext = pd.DataFrame(ext_rows)
    df_ext.to_csv(f"{OUTPUT_DIR}/projeto_04_historico_avaliacoes_externas.csv", index=False)
    print(f"  P04 - historico_avaliacoes_externas: {len(df_ext)} registros")

    # --- Dataset 3: metas_bonificacao.csv ---
    meta_rows = []
    for ano in [2021, 2022, 2023, 2024]:
        for escola in escolas:
            is_fraud = escola in ESCOLAS_FRAUDE
            meta_nota = round(random.gauss(65, 5), 1)
            nota_alcancada = round(random.gauss(63, 8), 1)
            if is_fraud:
                nota_alcancada = meta_nota + random.gauss(8, 2)  # Sempre acima da meta

            atingiu = nota_alcancada >= meta_nota
            bonificacao = round(random.uniform(15000, 50000), 2) if atingiu else 0

            meta_rows.append({
                "ano": ano,
                "escola": escola,
                "meta_nota_media": meta_nota,
                "nota_media_alcancada": round(nota_alcancada, 1),
                "meta_atingida": atingiu,
                "valor_bonificacao_reais": bonificacao,
                "ranking_rede": random.randint(1, 12)
            })

    df_meta = pd.DataFrame(meta_rows)
    df_meta.to_csv(f"{OUTPUT_DIR}/projeto_04_metas_bonificacao.csv", index=False)
    print(f"  P04 - metas_bonificacao: {len(df_meta)} registros")


# ============================================================
# PROJETO 05 — Operação Frota Fantasma: Desvio em Manutenção
# Padrões ocultos:
#   - Oficinas "AutoCenter VIP", "MecaPremium", "ServiCar Express"
#     cobram 40-80% acima da tabela
#   - Veículos com inconsistência de km (aparecem em cidades diferentes)
#   - Mesmos serviços repetidos em curto intervalo (< 30 dias)
# ============================================================
def gerar_projeto_05():
    veiculos = []
    cidades_base = {}
    for i in range(200):
        tipo = random.choices(["Caminhão", "Van", "Utilitário"], weights=[0.4, 0.35, 0.25])[0]
        ano_fab = random.randint(2015, 2023)
        km_atual = random.randint(30000, 350000)
        cidade = random.choice(["Fortaleza", "Caucaia", "Maracanaú", "Sobral", "Juazeiro do Norte"])
        veiculos.append({"veiculo_id": f"VEI-{i+1:04d}", "tipo": tipo,
                         "ano_fabricacao": ano_fab, "km_atual": km_atual})
        cidades_base[f"VEI-{i+1:04d}"] = cidade

    componentes = ["Motor", "Freios", "Suspensão", "Elétrica", "Transmissão", "Pneus", "Arrefecimento", "Direção"]
    tipos_manut = ["Preventiva", "Corretiva"]

    OFICINAS_FRAUDE = ["AutoCenter VIP", "MecaPremium", "ServiCar Express"]
    oficinas_todas = OFICINAS_FRAUDE + ["Oficina Popular", "Mecânica Central", "Auto Elétrica Norte",
                                         "Retífica Ceará", "Pneus & Cia", "Freios Total", "Moto Peças"]

    # --- Dataset 1: frota_manutencao.csv ---
    rows = []
    base_date = datetime(2023, 7, 1)
    for _ in range(4500):
        v = random.choice(veiculos)
        oficina = random.choices(oficinas_todas,
                                  weights=[0.12, 0.10, 0.11] + [0.067] * 7)[0]
        is_fraud_oficina = oficina in OFICINAS_FRAUDE
        dias = random.randint(0, 547)
        data = base_date + timedelta(days=dias)

        comp = random.choice(componentes)
        tipo_m = random.choices(tipos_manut, weights=[0.35, 0.65])[0]

        custo_base_tab = {"Motor": 2500, "Freios": 800, "Suspensão": 1200, "Elétrica": 600,
                          "Transmissão": 3000, "Pneus": 1500, "Arrefecimento": 700, "Direção": 900}
        custo = max(50, random.gauss(custo_base_tab[comp] * (0.6 if tipo_m == "Preventiva" else 1.0),
                                      custo_base_tab[comp] * 0.3))

        if is_fraud_oficina:
            custo *= random.uniform(1.4, 1.8)  # 40-80% acima

        tempo_parado_h = max(1, random.gauss(24 if tipo_m == "Corretiva" else 8, 6))
        km_na_manut = v["km_atual"] + random.randint(-20000, 50000)

        cidade_servico = cidades_base[v["veiculo_id"]]
        # Inconsistência: veículos em manutenção em cidade diferente da base
        if is_fraud_oficina and random.random() < 0.3:
            cidade_servico = random.choice(["Recife", "Salvador", "Teresina"])

        rows.append({
            "manutencao_id": f"MAN-{len(rows)+1:05d}",
            "veiculo_id": v["veiculo_id"],
            "tipo_veiculo": v["tipo"],
            "ano_fabricacao": v["ano_fabricacao"],
            "data_manutencao": data.strftime("%Y-%m-%d"),
            "oficina": oficina,
            "tipo_manutencao": tipo_m,
            "componente": comp,
            "custo_reais": round(custo, 2),
            "tempo_parado_horas": round(tempo_parado_h, 1),
            "km_odometro": max(1000, km_na_manut),
            "cidade_servico": cidade_servico
        })

    # Inserir serviços repetidos (mesmo veículo + componente em < 30 dias)
    for _ in range(80):
        base_row = random.choice([r for r in rows if r["oficina"] in OFICINAS_FRAUDE])
        dup = base_row.copy()
        dup["manutencao_id"] = f"MAN-{len(rows)+1:05d}"
        orig_date = datetime.strptime(base_row["data_manutencao"], "%Y-%m-%d")
        dup["data_manutencao"] = (orig_date + timedelta(days=random.randint(3, 25))).strftime("%Y-%m-%d")
        rows.append(dup)

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.04
    df.loc[mask, "tempo_parado_horas"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_05_frota_manutencao.csv", index=False)
    print(f"  P05 - frota_manutencao: {len(df)} registros")

    # --- Dataset 2: oficinas_credenciadas.csv ---
    of_rows = []
    socios_fraude = ["João Silva Santos", "José Silva Santos"]  # Mesmo sobrenome = parentes
    for i, of_name in enumerate(oficinas_todas):
        is_fraud = of_name in OFICINAS_FRAUDE
        of_rows.append({
            "oficina_id": f"OF-{i+1:03d}",
            "nome_oficina": of_name,
            "cnpj": f"{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(100,999)}/0001-{random.randint(10,99)}",
            "socio_principal": random.choice(socios_fraude) if is_fraud else f"Sócio {random.randint(1,50)}",
            "endereco": "Rua das Flores, 123" if is_fraud else f"Rua {random.randint(1,200)}, {random.randint(1,500)}",
            "cidade": "Fortaleza",
            "data_credenciamento": (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1000))).strftime("%Y-%m-%d"),
            "avaliacao_media": round(random.gauss(3.5, 0.8), 1) if not is_fraud else round(random.gauss(4.5, 0.2), 1),
            "total_servicos_realizados": random.randint(100, 800)
        })

    df_of = pd.DataFrame(of_rows)
    df_of.to_csv(f"{OUTPUT_DIR}/projeto_05_oficinas_credenciadas.csv", index=False)
    print(f"  P05 - oficinas_credenciadas: {len(df_of)} registros")

    # --- Dataset 3: tabela_precos_referencia.csv ---
    ref_rows = []
    for comp in componentes:
        for tipo_m in tipos_manut:
            custo_ref = {"Motor": 2500, "Freios": 800, "Suspensão": 1200, "Elétrica": 600,
                         "Transmissão": 3000, "Pneus": 1500, "Arrefecimento": 700, "Direção": 900}
            mult = 0.6 if tipo_m == "Preventiva" else 1.0
            ref_rows.append({
                "componente": comp,
                "tipo_manutencao": tipo_m,
                "preco_referencia_min": round(custo_ref[comp] * mult * 0.7, 2),
                "preco_referencia_medio": round(custo_ref[comp] * mult, 2),
                "preco_referencia_max": round(custo_ref[comp] * mult * 1.3, 2),
                "fonte": "Tabela SINDIREPA 2024",
                "data_atualizacao": "2024-01-15"
            })

    df_ref = pd.DataFrame(ref_rows)
    df_ref.to_csv(f"{OUTPUT_DIR}/projeto_05_tabela_precos_referencia.csv", index=False)
    print(f"  P05 - tabela_precos_referencia: {len(df_ref)} registros")


# ============================================================
# PROJETO 06 — Operação Curto-Circuito: Furto de Energia + Apagão
# Padrões ocultos:
#   - UCs 4500-4550 com queda abrupta de 80-90% (gato)
#   - Transformador T-023 sobrecarregado (região dos furtos)
#   - Correlação furtos <-> apagões na região "Barra do Ceará"
# ============================================================
def gerar_projeto_06():
    bairros = ["Meireles", "Aldeota", "Centro", "Barra do Ceará", "Mondubim",
               "Messejana", "Parangaba", "Montese", "Edson Queiroz", "Papicu"]
    UCS_FURTO = list(range(4500, 4551))

    # Atribuir bairros fixos a UCs
    uc_bairro = {}
    for uc_id in range(1, 5001):
        if uc_id in UCS_FURTO:
            uc_bairro[uc_id] = "Barra do Ceará"  # Concentrados no mesmo bairro
        else:
            uc_bairro[uc_id] = random.choice(bairros)

    # --- Dataset 1: consumo_energia.csv ---
    rows = []
    for uc_id in range(1, 5001):
        classe = random.choices(["Residencial", "Comercial", "Industrial"],
                                weights=[0.70, 0.22, 0.08])[0]
        if uc_id in UCS_FURTO:
            classe = "Residencial"

        base_consumo = {"Residencial": 180, "Comercial": 1200, "Industrial": 8000}[classe]

        for ano in [2023, 2024]:
            for mes in range(1, 13):
                sazonal = 1.0
                if mes in [9, 10, 11, 12, 1, 2]:
                    sazonal = 1.15 if classe == "Residencial" else 1.08
                elif mes in [5, 6, 7]:
                    sazonal = 0.90

                consumo = max(10, random.gauss(base_consumo * sazonal, base_consumo * 0.2))

                # GATO: queda abrupta a partir de jul/2024
                if uc_id in UCS_FURTO and (ano == 2024 and mes >= 7):
                    consumo *= random.uniform(0.05, 0.15)  # 85-95% de redução

                temp_media = random.gauss(27 + (3 if mes in [10, 11, 12] else -2 if mes in [6, 7] else 0), 1.5)

                rows.append({
                    "uc_id": f"UC-{uc_id:05d}",
                    "classe": classe,
                    "bairro": uc_bairro[uc_id],
                    "ano": ano,
                    "mes": mes,
                    "consumo_kwh": round(consumo, 1),
                    "temperatura_media_c": round(temp_media, 1)
                })

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.02
    df.loc[mask, "consumo_kwh"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_06_consumo_energia.csv", index=False)
    print(f"  P06 - consumo_energia: {len(df)} registros")

    # --- Dataset 2: ocorrencias_rede.csv ---
    oc_rows = []
    base_date = datetime(2023, 1, 1)
    for _ in range(500):
        data = base_date + timedelta(days=random.randint(0, 729))
        bairro = random.choice(bairros)

        # Mais ocorrências em Barra do Ceará a partir de jul/2024
        if random.random() < 0.3:
            bairro = "Barra do Ceará"
            if data >= datetime(2024, 7, 1):
                pass  # Vai gerar mais abaixo

        tipo = random.choices(
            ["Queda de energia", "Flutuação de tensão", "Curto-circuito",
             "Manutenção programada", "Reclamação de consumidor", "Furto detectado"],
            weights=[0.25, 0.15, 0.10, 0.20, 0.20, 0.10]
        )[0]

        oc_rows.append({
            "ocorrencia_id": f"OC-{len(oc_rows)+1:05d}",
            "data_ocorrencia": data.strftime("%Y-%m-%d"),
            "bairro": bairro,
            "tipo_ocorrencia": tipo,
            "transformador_id": f"T-{random.randint(1,50):03d}",
            "duracao_horas": round(max(0.5, random.gauss(3, 2)), 1),
            "ucs_afetadas": random.randint(10, 500),
            "causa_provavel": random.choice(["Sobrecarga", "Falha equipamento", "Clima", "Vandalismo", "Indeterminada"])
        })

    # Adicionar surto de ocorrências em Barra do Ceará
    for _ in range(80):
        data = datetime(2024, 7, 1) + timedelta(days=random.randint(0, 180))
        oc_rows.append({
            "ocorrencia_id": f"OC-{len(oc_rows)+1:05d}",
            "data_ocorrencia": data.strftime("%Y-%m-%d"),
            "bairro": "Barra do Ceará",
            "tipo_ocorrencia": random.choices(
                ["Queda de energia", "Flutuação de tensão", "Curto-circuito", "Furto detectado"],
                weights=[0.35, 0.20, 0.20, 0.25]
            )[0],
            "transformador_id": "T-023",  # Sempre o mesmo transformador!
            "duracao_horas": round(max(0.5, random.gauss(5, 3)), 1),
            "ucs_afetadas": random.randint(50, 300),
            "causa_provavel": random.choice(["Sobrecarga", "Sobrecarga", "Sobrecarga", "Indeterminada"])
        })

    df_oc = pd.DataFrame(oc_rows)
    df_oc.to_csv(f"{OUTPUT_DIR}/projeto_06_ocorrencias_rede.csv", index=False)
    print(f"  P06 - ocorrencias_rede: {len(df_oc)} registros")

    # --- Dataset 3: cadastro_transformadores.csv ---
    transf_rows = []
    for i in range(1, 51):
        tid = f"T-{i:03d}"
        bairro = random.choice(bairros)
        capacidade = random.choice([75, 112.5, 150, 225, 300])

        if tid == "T-023":
            bairro = "Barra do Ceará"
            capacidade = 75  # Capacidade pequena para o número de UCs

        ucs_conectadas = random.randint(30, 200)
        if tid == "T-023":
            ucs_conectadas = 280  # Muito acima da capacidade

        transf_rows.append({
            "transformador_id": tid,
            "bairro": bairro,
            "capacidade_kva": capacidade,
            "ucs_conectadas": ucs_conectadas,
            "ano_instalacao": random.randint(2005, 2022),
            "ultima_manutencao": (datetime(2024, 1, 1) - timedelta(days=random.randint(30, 1000))).strftime("%Y-%m-%d"),
            "status": "Operacional" if tid != "T-023" else "Sobrecarga frequente"
        })

    df_transf = pd.DataFrame(transf_rows)
    df_transf.to_csv(f"{OUTPUT_DIR}/projeto_06_cadastro_transformadores.csv", index=False)
    print(f"  P06 - cadastro_transformadores: {len(df_transf)} registros")


# ============================================================
# PROJETO 07 — Dossiê Exodus: Crise de Talentos e Discriminação
# Padrões ocultos:
#   - Gap salarial de gênero (~15% em cargos iguais)
#   - Dept "Vendas" com turnover anormal + gestor problemático
#   - Mulheres com tempo até promoção ~40% maior
# ============================================================
def gerar_projeto_07():
    departamentos = ["Engenharia", "Produto", "Marketing", "Vendas", "Suporte",
                     "RH", "Financeiro", "Operações"]
    cargos = ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente"]

    DEPT_TOXICO = "Vendas"

    # --- Dataset 1: people_analytics.csv ---
    rows = []
    for i in range(1200):
        dept = random.choice(departamentos)
        cargo = random.choices(cargos, weights=[0.25, 0.30, 0.25, 0.12, 0.08])[0]

        idade = int(np.clip(random.gauss(33, 7), 22, 60))
        sexo = random.choice(["M", "F"])

        tempo_empresa_meses = int(np.clip(random.gauss(36, 24), 1, 180))

        salario_base = {"Júnior": 4000, "Pleno": 7000, "Sênior": 11000,
                        "Coordenador": 14000, "Gerente": 20000}
        salario = max(2500, random.gauss(salario_base[cargo], salario_base[cargo] * 0.15))

        # GAP SALARIAL: mulheres ganham ~15% menos no mesmo cargo
        if sexo == "F":
            salario *= random.uniform(0.82, 0.88)

        satisfacao_trabalho = int(np.clip(random.gauss(3.5, 1.0), 1, 5))
        satisfacao_ambiente = int(np.clip(random.gauss(3.3, 1.1), 1, 5))
        equilibrio_vida = int(np.clip(random.gauss(3.0, 1.2), 1, 5))

        # Departamento tóxico
        if dept == DEPT_TOXICO:
            satisfacao_trabalho = int(np.clip(satisfacao_trabalho - 1.5, 1, 5))
            satisfacao_ambiente = int(np.clip(satisfacao_ambiente - 2, 1, 5))

        promovido_2anos = random.choices([1, 0], weights=[0.25, 0.75])[0]
        horas_extras_mes = int(np.clip(random.gauss(8, 6), 0, 40))

        prob_saida = 0.12
        if satisfacao_trabalho <= 2: prob_saida += 0.15
        if equilibrio_vida <= 2: prob_saida += 0.10
        if dept == DEPT_TOXICO: prob_saida += 0.25  # Turnover anormal
        if promovido_2anos: prob_saida -= 0.08
        if horas_extras_mes > 20: prob_saida += 0.10

        saiu = 1 if random.random() < prob_saida else 0
        data_admissao = datetime(2024, 12, 1) - timedelta(days=tempo_empresa_meses * 30)
        data_saida = (data_admissao + timedelta(days=tempo_empresa_meses * 30)).strftime("%Y-%m-%d") if saiu else np.nan

        rows.append({
            "funcionario_id": f"FUN-{i+1:05d}",
            "departamento": dept,
            "cargo": cargo,
            "idade": idade,
            "sexo": sexo,
            "tempo_empresa_meses": tempo_empresa_meses,
            "salario_mensal": round(salario, 2),
            "satisfacao_trabalho": satisfacao_trabalho,
            "satisfacao_ambiente": satisfacao_ambiente,
            "equilibrio_vida_trabalho": equilibrio_vida,
            "promovido_ultimos_2anos": promovido_2anos,
            "horas_extras_mes": horas_extras_mes,
            "num_projetos": random.randint(1, 7),
            "avaliacao_desempenho": round(np.clip(random.gauss(3.5, 0.8), 1, 5), 1),
            "saiu_da_empresa": saiu,
            "data_admissao": data_admissao.strftime("%Y-%m-%d"),
            "data_saida": data_saida
        })

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.04
    df.loc[mask, "satisfacao_trabalho"] = np.nan
    mask2 = np.random.random(len(df)) < 0.03
    df.loc[mask2, "avaliacao_desempenho"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_07_people_analytics.csv", index=False)
    print(f"  P07 - people_analytics: {len(df)} registros")

    # --- Dataset 2: pesquisa_clima_anonima.csv ---
    clima_rows = []
    comentarios_toxicos = [
        "Meu gestor grita e humilha na frente de todos.",
        "Ambiente de medo. Ninguém quer falar nada.",
        "Chefe faz piadas machistas e ninguém toma providência.",
        "Já vi colega chorando depois de reunião com o gerente.",
        "O gestor dá as melhores metas para os amigos dele.",
        "Trabalho sob pressão absurda, sem reconhecimento.",
        "Fiz a mesma coisa que meu colega homem e ele foi promovido, eu não.",
        "Pedem resultado impossível e depois culpam a equipe.",
    ]
    comentarios_normais = [
        "Ambiente agradável, boa equipe.",
        "Poderia ter mais oportunidades de crescimento.",
        "Salário está abaixo do mercado.",
        "Gosto do trabalho mas as metas são apertadas.",
        "Boa liderança, me sinto valorizado.",
        "Falta comunicação entre departamentos.",
        "Home office ajudou muito na qualidade de vida.",
        "Precisa melhorar os benefícios.",
        np.nan
    ]

    for i in range(400):
        dept = random.choice(departamentos)
        is_toxic_dept = dept == DEPT_TOXICO

        nota_geral = int(np.clip(random.gauss(3.5, 1.0), 1, 5))
        nota_lideranca = int(np.clip(random.gauss(3.3, 1.1), 1, 5))

        if is_toxic_dept:
            nota_geral = int(np.clip(random.gauss(2.0, 0.7), 1, 5))
            nota_lideranca = int(np.clip(random.gauss(1.5, 0.5), 1, 5))

        comentario = random.choice(comentarios_toxicos) if is_toxic_dept and random.random() < 0.6 \
                     else random.choice(comentarios_normais)

        clima_rows.append({
            "resposta_id": f"RESP-{i+1:04d}",
            "data_pesquisa": random.choice(["2024-06-01", "2024-12-01"]),
            "departamento": dept,
            "tempo_empresa_faixa": random.choice(["< 1 ano", "1-3 anos", "3-5 anos", "5+ anos"]),
            "sexo": random.choice(["M", "F"]),
            "nota_satisfacao_geral": nota_geral,
            "nota_lideranca": nota_lideranca,
            "nota_remuneracao": int(np.clip(random.gauss(3.0, 1.0), 1, 5)),
            "nota_crescimento": int(np.clip(random.gauss(3.2, 1.1), 1, 5)),
            "recomendaria_empresa": random.choices([1, 0], weights=[0.6, 0.4] if not is_toxic_dept else [0.2, 0.8])[0],
            "comentario_aberto": comentario
        })

    df_clima = pd.DataFrame(clima_rows)
    df_clima.to_csv(f"{OUTPUT_DIR}/projeto_07_pesquisa_clima_anonima.csv", index=False)
    print(f"  P07 - pesquisa_clima_anonima: {len(df_clima)} registros")

    # --- Dataset 3: historico_promocoes.csv ---
    promo_rows = []
    for i in range(600):
        func_id = f"FUN-{random.randint(1, 1200):05d}"
        sexo = random.choice(["M", "F"])
        dept = random.choice(departamentos)

        cargo_origem = random.choices(cargos[:4], weights=[0.35, 0.30, 0.25, 0.10])[0]
        idx_cargo = cargos.index(cargo_origem)
        cargo_destino = cargos[min(idx_cargo + 1, len(cargos) - 1)]

        meses_para_promocao = int(np.clip(random.gauss(24, 8), 6, 60))

        # PADRÃO: mulheres demoram ~40% mais para ser promovidas
        if sexo == "F":
            meses_para_promocao = int(meses_para_promocao * random.uniform(1.3, 1.5))

        salario_antes = random.gauss({"Júnior": 4000, "Pleno": 7000, "Sênior": 11000, "Coordenador": 14000}[cargo_origem],
                                      1000)
        aumento_pct = random.gauss(15, 5)
        salario_depois = salario_antes * (1 + aumento_pct / 100)

        promo_rows.append({
            "funcionario_id": func_id,
            "sexo": sexo,
            "departamento": dept,
            "cargo_anterior": cargo_origem,
            "cargo_novo": cargo_destino,
            "data_promocao": (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1800))).strftime("%Y-%m-%d"),
            "meses_no_cargo_anterior": meses_para_promocao,
            "salario_anterior": round(salario_antes, 2),
            "salario_novo": round(salario_depois, 2),
            "aumento_percentual": round(aumento_pct, 1),
            "avaliacao_no_momento": round(np.clip(random.gauss(3.8, 0.7), 1, 5), 1)
        })

    df_promo = pd.DataFrame(promo_rows)
    df_promo.to_csv(f"{OUTPUT_DIR}/projeto_07_historico_promocoes.csv", index=False)
    print(f"  P07 - historico_promocoes: {len(df_promo)} registros")


# ============================================================
# PROJETO 08 — Alerta Epidemiológico: Surto de Diabetes
# Padrões ocultos:
#   - Região "Zona Oeste" com UBS fechada = falha de acompanhamento
#   - Pacientes sem acompanhamento regular têm 3x mais complicações
#   - Faixa 40-55 subdiagnosticada (muitos com glicemia alta não diagnosticados)
# ============================================================
def gerar_projeto_08():
    regioes = ["Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste", "Centro"]
    REGIAO_CRISE = "Zona Oeste"

    # --- Dataset 1: diabetes_clinico.csv ---
    rows = []
    for i in range(2000):
        idade = int(np.clip(random.gauss(48, 14), 18, 85))
        sexo = random.choice(["M", "F"])
        regiao = random.choice(regioes)
        imc = round(np.clip(random.gauss(27, 5), 16, 50), 1)

        atividade_fisica = random.choices(
            ["Sedentário", "Leve", "Moderada", "Intensa"],
            weights=[0.35, 0.30, 0.25, 0.10]
        )[0]
        historico_familiar = random.choices([1, 0], weights=[0.35, 0.65])[0]
        tabagismo = random.choices(["Nunca", "Ex-fumante", "Fumante"], weights=[0.55, 0.25, 0.20])[0]

        risco = 0.15
        if idade > 50: risco += 0.12
        if imc > 30: risco += 0.15
        if imc > 35: risco += 0.10
        if historico_familiar: risco += 0.10
        if atividade_fisica == "Sedentário": risco += 0.08
        if atividade_fisica == "Intensa": risco -= 0.08
        if tabagismo == "Fumante": risco += 0.05

        diabetes = 1 if random.random() < risco else 0

        # SUBDIAGNÓSTICO: faixa 40-55 tem diabetes não diagnosticada
        if 40 <= idade <= 55 and random.random() < 0.15:
            diabetes = 0  # Não diagnosticado, mas com indicadores altos

        glicemia_base = 95 if not diabetes else 145
        # Subdiagnosticados: glicemia alta mas sem diagnóstico
        if 40 <= idade <= 55 and diabetes == 0 and random.random() < 0.2:
            glicemia_base = 130  # Pré-diabético não acompanhado

        glicemia = round(np.clip(random.gauss(glicemia_base, 20), 60, 350), 1)
        hba1c_base = 5.4 if not diabetes else 7.8
        hba1c = round(np.clip(random.gauss(hba1c_base, 0.8), 4.0, 14.0), 1)

        pressao_sist = int(np.clip(random.gauss(125 + (15 if diabetes else 0), 15), 90, 200))
        pressao_diast = int(np.clip(random.gauss(80 + (8 if diabetes else 0), 10), 55, 120))
        colesterol_total = round(np.clip(random.gauss(195 + (20 if diabetes else 0), 35), 100, 350), 1)
        hdl = round(np.clip(random.gauss(50 + (-8 if diabetes else 5), 12), 20, 100), 1)
        ldl = round(np.clip(random.gauss(120 + (15 if diabetes else 0), 30), 40, 250), 1)
        triglicerideos = round(np.clip(random.gauss(150 + (50 if diabetes else 0), 60), 40, 600), 1)

        # Acompanhamento regular
        acompanhamento_regular = random.choices([1, 0], weights=[0.65, 0.35])[0]
        if regiao == REGIAO_CRISE:
            acompanhamento_regular = random.choices([1, 0], weights=[0.20, 0.80])[0]  # UBS fechou

        ultima_consulta_dias = random.randint(15, 90) if acompanhamento_regular else random.randint(120, 400)

        rows.append({
            "paciente_id": f"PAC-{i+1:05d}",
            "idade": idade,
            "sexo": sexo,
            "regiao": regiao,
            "imc": imc,
            "atividade_fisica": atividade_fisica,
            "historico_familiar_diabetes": historico_familiar,
            "tabagismo": tabagismo,
            "glicemia_jejum_mgdl": glicemia,
            "hba1c_pct": hba1c,
            "pressao_sistolica": pressao_sist,
            "pressao_diastolica": pressao_diast,
            "colesterol_total_mgdl": colesterol_total,
            "hdl_mgdl": round(hdl, 1),
            "ldl_mgdl": ldl,
            "triglicerideos_mgdl": round(triglicerideos, 1),
            "diagnostico_diabetes": diabetes,
            "acompanhamento_regular": acompanhamento_regular,
            "dias_desde_ultima_consulta": ultima_consulta_dias
        })

    df = pd.DataFrame(rows)
    for col in ["hba1c_pct", "colesterol_total_mgdl", "triglicerideos_mgdl"]:
        mask = np.random.random(len(df)) < 0.05
        df.loc[mask, col] = np.nan
    idx = df.sample(5).index
    df.loc[idx, "imc"] = [0, -1, 999, 5, 80]

    df.to_csv(f"{OUTPUT_DIR}/projeto_08_diabetes_clinico.csv", index=False)
    print(f"  P08 - diabetes_clinico: {len(df)} registros")

    # --- Dataset 2: atendimentos_emergencia.csv ---
    emerg_rows = []
    base_date = datetime(2024, 1, 1)
    complicacoes = ["Cetoacidose Diabética", "Hipoglicemia Severa", "Pé Diabético",
                    "Nefropatia", "Retinopatia", "Neuropatia", "AVC", "Infarto"]

    for _ in range(3000):
        paciente_id = f"PAC-{random.randint(1, 2000):05d}"
        data = base_date + timedelta(days=random.randint(0, 365))
        regiao = random.choice(regioes)

        complicacao = random.choice(complicacoes)
        gravidade = random.choices(["Leve", "Moderada", "Grave", "Crítica"],
                                    weights=[0.25, 0.35, 0.25, 0.15])[0]

        # Zona Oeste: mais emergências, mais graves
        if regiao == REGIAO_CRISE:
            gravidade = random.choices(["Leve", "Moderada", "Grave", "Crítica"],
                                        weights=[0.10, 0.25, 0.35, 0.30])[0]

        dias_internacao = max(1, int(random.gauss(3, 2)))
        if gravidade in ["Grave", "Crítica"]:
            dias_internacao = max(3, int(random.gauss(7, 3)))

        desfecho = "Alta" if gravidade != "Crítica" or random.random() > 0.15 else "Óbito"

        emerg_rows.append({
            "atendimento_id": f"ATD-{len(emerg_rows)+1:05d}",
            "paciente_id": paciente_id,
            "data_atendimento": data.strftime("%Y-%m-%d"),
            "regiao": regiao,
            "complicacao": complicacao,
            "gravidade": gravidade,
            "dias_internacao": dias_internacao,
            "uti": 1 if gravidade in ["Grave", "Crítica"] and random.random() < 0.5 else 0,
            "desfecho": desfecho,
            "tinha_acompanhamento_previo": random.choices([1, 0], weights=[0.4, 0.6] if regiao != REGIAO_CRISE else [0.15, 0.85])[0]
        })

    # Adicionar surto de emergências na Zona Oeste (2º semestre)
    for _ in range(500):
        data = datetime(2024, 7, 1) + timedelta(days=random.randint(0, 180))
        emerg_rows.append({
            "atendimento_id": f"ATD-{len(emerg_rows)+1:05d}",
            "paciente_id": f"PAC-{random.randint(1, 2000):05d}",
            "data_atendimento": data.strftime("%Y-%m-%d"),
            "regiao": REGIAO_CRISE,
            "complicacao": random.choice(complicacoes),
            "gravidade": random.choices(["Moderada", "Grave", "Crítica"], weights=[0.30, 0.40, 0.30])[0],
            "dias_internacao": max(2, int(random.gauss(6, 3))),
            "uti": random.choices([0, 1], weights=[0.5, 0.5])[0],
            "desfecho": random.choices(["Alta", "Óbito"], weights=[0.85, 0.15])[0],
            "tinha_acompanhamento_previo": 0
        })

    df_emerg = pd.DataFrame(emerg_rows)
    df_emerg.to_csv(f"{OUTPUT_DIR}/projeto_08_atendimentos_emergencia.csv", index=False)
    print(f"  P08 - atendimentos_emergencia: {len(df_emerg)} registros")

    # --- Dataset 3: unidades_saude_cobertura.csv ---
    ubs_rows = []
    ubs_nomes = {
        "Zona Norte": ["UBS Vila Nova", "UBS Parque Norte", "UBS Jardim América"],
        "Zona Sul": ["UBS Boa Vista", "UBS Sul Center"],
        "Zona Leste": ["UBS Leste I", "UBS Leste II", "UBS Jardim Leste"],
        "Zona Oeste": ["UBS Oeste Central", "UBS Vila Oeste"],  # Uma fechou!
        "Centro": ["UBS Centro", "UBS Praça da Saúde"]
    }

    for regiao, nomes in ubs_nomes.items():
        for nome in nomes:
            is_fechada = (nome == "UBS Oeste Central")
            ubs_rows.append({
                "ubs_id": f"UBS-{len(ubs_rows)+1:03d}",
                "nome_unidade": nome,
                "regiao": regiao,
                "status": "Fechada temporariamente" if is_fechada else "Ativa",
                "data_fechamento": "2024-03-15" if is_fechada else np.nan,
                "medicos_disponiveis": 0 if is_fechada else random.randint(2, 8),
                "enfermeiros": 0 if is_fechada else random.randint(3, 12),
                "pacientes_cadastrados": random.randint(800, 3000),
                "pacientes_diabetes_acompanhados": random.randint(50, 300) if not is_fechada else 0,
                "consultas_mes_medio": random.randint(200, 800) if not is_fechada else 0,
                "capacidade_maxima_dia": random.randint(30, 80)
            })

    df_ubs = pd.DataFrame(ubs_rows)
    df_ubs.to_csv(f"{OUTPUT_DIR}/projeto_08_unidades_saude_cobertura.csv", index=False)
    print(f"  P08 - unidades_saude_cobertura: {len(df_ubs)} registros")


# ============================================================
# PROJETO 09 — Operação Lava-Imóvel: Lavagem de Dinheiro
# Padrões ocultos:
#   - CPFs "fantasma" com renda incompatível (renda < 5k, compra > 1M)
#   - Transações 40-60% acima do preço de mercado
#   - CNPJs ligados (mesmo endereço/sócio)
#   - Imóveis revendidos em < 6 meses com lucro > 50%
# ============================================================
def gerar_projeto_09():
    bairros = {
        "Meireles": 12000, "Aldeota": 10500, "Cocó": 9500, "Dionísio Torres": 9000,
        "Varjota": 8500, "Luciano Cavalcante": 8000, "Fátima": 7000, "Centro": 5500,
        "Papicu": 6500, "Edson Queiroz": 7500, "Parquelândia": 6000, "Benfica": 5000,
        "Montese": 4500, "Parangaba": 4000, "Maraponga": 4200, "Messejana": 3800,
        "Eusébio": 5500, "Aquiraz (Beach Park)": 7000, "Caucaia": 3000, "Maracanaú": 2800
    }

    COMPRADORES_SUSPEITOS = [f"CPF-{i:05d}" for i in range(9001, 9021)]  # 20 CPFs suspeitos
    CNPJS_SUSPEITOS = [f"CNPJ-{i:05d}" for i in range(8001, 8006)]  # 5 CNPJs ligados

    # --- Dataset 1: mercado_imobiliario.csv ---
    rows = []
    for i in range(3500):
        bairro = random.choice(list(bairros.keys()))
        preco_m2_base = bairros[bairro]

        tipo = random.choices(["Apartamento", "Casa", "Cobertura", "Flat/Studio"],
                              weights=[0.55, 0.25, 0.08, 0.12])[0]

        if tipo == "Apartamento":
            area = int(np.clip(random.gauss(75, 25), 30, 200))
            quartos = random.choices([1, 2, 3, 4], weights=[0.10, 0.30, 0.45, 0.15])[0]
        elif tipo == "Casa":
            area = int(np.clip(random.gauss(150, 50), 60, 400))
            quartos = random.choices([2, 3, 4, 5], weights=[0.15, 0.40, 0.35, 0.10])[0]
        elif tipo == "Cobertura":
            area = int(np.clip(random.gauss(180, 40), 100, 350))
            quartos = random.choices([3, 4, 5], weights=[0.30, 0.50, 0.20])[0]
        else:
            area = int(np.clip(random.gauss(35, 8), 20, 55))
            quartos = 1

        condicao = random.choices(["Novo", "Usado"], weights=[0.35, 0.65])[0]
        mult_condicao = 1.15 if condicao == "Novo" else 1.0

        preco_m2 = max(1500, random.gauss(preco_m2_base * mult_condicao, preco_m2_base * 0.15))
        preco_total = area * preco_m2

        # Comprador
        is_suspicious = random.random() < 0.06  # ~6% de transações suspeitas
        comprador_id = random.choice(COMPRADORES_SUSPEITOS) if is_suspicious else f"CPF-{random.randint(1, 8000):05d}"
        comprador_cnpj = random.choice(CNPJS_SUSPEITOS) if is_suspicious and random.random() < 0.4 else np.nan

        if is_suspicious:
            preco_total *= random.uniform(1.4, 1.6)  # 40-60% acima do mercado

        ano_transacao = random.choices([2022, 2023, 2024], weights=[0.25, 0.40, 0.35])[0]
        mes_transacao = random.randint(1, 12)

        rows.append({
            "transacao_id": f"TX-{i+1:05d}",
            "imovel_id": f"IMO-{i+1:05d}",
            "bairro": bairro,
            "tipo_imovel": tipo,
            "area_m2": area,
            "quartos": quartos,
            "condicao": condicao,
            "preco_total": round(preco_total, 2),
            "preco_m2": round(preco_total / area, 2),
            "comprador_id": comprador_id,
            "comprador_cnpj": comprador_cnpj,
            "forma_pagamento": random.choice(["Financiamento", "À vista", "À vista"]) if not is_suspicious
                              else random.choice(["À vista", "À vista", "À vista"]),  # Suspeitos pagam à vista
            "ano_transacao": ano_transacao,
            "mes_transacao": mes_transacao,
            "dias_no_mercado": int(np.clip(random.gauss(90, 60), 5, 400))
        })

    # Imóveis revendidos rapidamente (flip suspeito)
    for _ in range(40):
        base_tx = random.choice([r for r in rows if r["comprador_id"] in COMPRADORES_SUSPEITOS])
        flip = {
            "transacao_id": f"TX-{len(rows)+1:05d}",
            "imovel_id": base_tx["imovel_id"],  # Mesmo imóvel!
            "bairro": base_tx["bairro"],
            "tipo_imovel": base_tx["tipo_imovel"],
            "area_m2": base_tx["area_m2"],
            "quartos": base_tx["quartos"],
            "condicao": base_tx["condicao"],
            "preco_total": round(base_tx["preco_total"] * random.uniform(1.5, 1.8), 2),  # Lucro 50-80%
            "preco_m2": round(base_tx["preco_total"] * random.uniform(1.5, 1.8) / base_tx["area_m2"], 2),
            "comprador_id": f"CPF-{random.randint(1, 8000):05d}",
            "comprador_cnpj": np.nan,
            "forma_pagamento": "Financiamento",
            "ano_transacao": base_tx["ano_transacao"] + (1 if base_tx["mes_transacao"] > 6 else 0),
            "mes_transacao": (base_tx["mes_transacao"] + random.randint(2, 5)) % 12 + 1,
            "dias_no_mercado": random.randint(5, 30)  # Vendido rapidamente
        }
        rows.append(flip)

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.03
    df.loc[mask, "dias_no_mercado"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_09_mercado_imobiliario.csv", index=False)
    print(f"  P09 - mercado_imobiliario: {len(df)} registros")

    # --- Dataset 2: compradores_perfil.csv ---
    comp_rows = []
    for cpf in set([r["comprador_id"] for r in rows]):
        is_sus = cpf in COMPRADORES_SUSPEITOS
        renda_mensal = round(random.gauss(8000, 3000), 2)
        if is_sus:
            renda_mensal = round(random.gauss(3500, 1000), 2)  # Renda incompatível

        comp_rows.append({
            "comprador_id": cpf,
            "renda_mensal_declarada": max(1500, renda_mensal),
            "idade": random.randint(25, 65),
            "estado_civil": random.choice(["Solteiro", "Casado", "Divorciado"]),
            "profissao": random.choice(["Empresário", "Autônomo", "Servidor", "Comerciante",
                                         "Engenheiro", "Advogado", "Médico", "Outros"]) if not is_sus
                        else random.choice(["Autônomo", "Empresário", "Não informado"]),
            "numero_imoveis_adquiridos": random.randint(1, 2) if not is_sus else random.randint(3, 8),
            "possui_restricao_credito": random.choices([0, 1], weights=[0.9, 0.1])[0],
            "pep": random.choices([0, 1], weights=[0.95, 0.05])[0]  # Pessoa Exposta Politicamente
        })

    df_comp = pd.DataFrame(comp_rows)
    df_comp.to_csv(f"{OUTPUT_DIR}/projeto_09_compradores_perfil.csv", index=False)
    print(f"  P09 - compradores_perfil: {len(df_comp)} registros")

    # --- Dataset 3: historico_precos_bairro.csv ---
    hist_rows = []
    for bairro, base_preco in bairros.items():
        for ano in [2022, 2023, 2024]:
            for trimestre in [1, 2, 3, 4]:
                # Valorização natural ~5% ao ano
                mult_ano = 1 + (ano - 2022) * 0.05
                preco_ref = base_preco * mult_ano * random.gauss(1, 0.03)

                hist_rows.append({
                    "bairro": bairro,
                    "ano": ano,
                    "trimestre": trimestre,
                    "preco_m2_referencia": round(preco_ref, 2),
                    "numero_transacoes": random.randint(10, 80),
                    "variacao_trimestral_pct": round(random.gauss(1.2, 2), 1)
                })

    df_hist = pd.DataFrame(hist_rows)
    df_hist.to_csv(f"{OUTPUT_DIR}/projeto_09_historico_precos_bairro.csv", index=False)
    print(f"  P09 - historico_precos_bairro: {len(df_hist)} registros")


# ============================================================
# PROJETO 10 — Dossiê Desvio: Onde Foi o Dinheiro Público?
# Padrões ocultos:
#   - Municípios "Município 101-105" com alto repasse + indicadores estagnados
#   - Licitações com empresas de fachada (mesmo endereço/sócio)
#   - Contratos fracionados para escapar de licitação (< R$80k)
# ============================================================
def gerar_projeto_10():
    municipios_reais = [
        "Fortaleza", "Caucaia", "Juazeiro do Norte", "Maracanaú", "Sobral",
        "Crato", "Itapipoca", "Maranguape", "Iguatu", "Quixadá",
        "Pacatuba", "Aquiraz", "Canindé", "Russas", "Tianguá",
        "Crateús", "Aracati", "Horizonte", "Pacajus", "Eusébio",
        "São Gonçalo do Amarante", "Cascavel", "Barbalha", "Icó", "Camocim",
        "Limoeiro do Norte", "Tauá", "Morada Nova", "Brejo Santo", "Baturité",
        "Acaraú", "Granja", "Pentecoste", "Beberibe", "Trairi",
        "Redenção", "Viçosa do Ceará", "Lavras da Mangabeira", "Jaguaribe", "Missão Velha"
    ]
    for i in range(len(municipios_reais), 184):
        municipios_reais.append(f"Município {i+1}")

    MUNICIPIOS_DESVIO = [f"Município {i}" for i in range(101, 106)]

    # --- Dataset 1: indicadores_municipais.csv ---
    rows = []
    for mun in municipios_reais:
        is_capital = mun == "Fortaleza"
        is_grande = mun in municipios_reais[:10]
        is_desvio = mun in MUNICIPIOS_DESVIO

        pop = random.randint(5000, 50000)
        if is_grande: pop = random.randint(80000, 300000)
        if is_capital: pop = 2700000

        pib_pc = random.gauss(12000 if is_capital else 18000 if is_grande else 8000, 3000)
        pib_pc = max(3000, pib_pc)

        idh = np.clip(random.gauss(0.72 if is_capital else 0.68 if is_grande else 0.62, 0.05), 0.45, 0.85)

        taxa_analfabetismo = np.clip(random.gauss(12 if is_capital else 15 if is_grande else 22, 5), 2, 45)
        anos_estudo = np.clip(random.gauss(9.5 if is_capital else 8 if is_grande else 6.5, 1.5), 3, 14)
        mortalidade_infantil = np.clip(random.gauss(12 if is_capital else 14 if is_grande else 18, 4), 3, 40)
        expectativa_vida = np.clip(random.gauss(75 if is_capital else 73 if is_grande else 71, 2.5), 60, 82)
        gini = np.clip(random.gauss(0.52, 0.06), 0.35, 0.70)
        cobertura_esgoto = np.clip(random.gauss(70 if is_capital else 50 if is_grande else 25, 15), 0, 100)
        cobertura_agua = np.clip(random.gauss(95 if is_capital else 85 if is_grande else 65, 10), 20, 100)

        # DESVIO: indicadores estagnados apesar de repasses altos
        if is_desvio:
            idh = np.clip(random.gauss(0.55, 0.03), 0.45, 0.62)  # IDH baixo
            taxa_analfabetismo = np.clip(random.gauss(28, 3), 20, 40)  # Alto analfabetismo
            cobertura_esgoto = np.clip(random.gauss(15, 5), 5, 30)  # Péssimo esgoto
            mortalidade_infantil = np.clip(random.gauss(25, 3), 18, 35)  # Alta mortalidade

        for ano in [2020, 2021, 2022, 2023]:
            rows.append({
                "municipio": mun,
                "ano": ano,
                "populacao": pop + int(pop * (ano - 2020) * 0.01),
                "pib_per_capita": round(pib_pc * (1 + (ano - 2020) * 0.02), 2),
                "idh": round(idh + (ano - 2020) * 0.002 * (0.1 if is_desvio else 1), 3),  # Quase não melhora
                "taxa_analfabetismo_pct": round(taxa_analfabetismo - (ano - 2020) * 0.3 * (0.1 if is_desvio else 1), 1),
                "anos_estudo_medio": round(anos_estudo + (ano - 2020) * 0.1 * (0.1 if is_desvio else 1), 1),
                "mortalidade_infantil_por_mil": round(mortalidade_infantil - (ano - 2020) * 0.2 * (0.1 if is_desvio else 1), 1),
                "expectativa_vida_anos": round(expectativa_vida, 1),
                "indice_gini": round(gini, 3),
                "cobertura_esgoto_pct": round(cobertura_esgoto + (ano - 2020) * 1 * (0.1 if is_desvio else 1), 1),
                "cobertura_agua_pct": round(cobertura_agua, 1)
            })

    df = pd.DataFrame(rows)
    mask = np.random.random(len(df)) < 0.08
    df.loc[mask, "cobertura_esgoto_pct"] = np.nan
    mask2 = np.random.random(len(df)) < 0.05
    df.loc[mask2, "indice_gini"] = np.nan
    idx = df.sample(3).index
    df.loc[idx, "idh"] = [1.5, -0.2, 999]

    df.to_csv(f"{OUTPUT_DIR}/projeto_10_indicadores_municipais.csv", index=False)
    print(f"  P10 - indicadores_municipais: {len(df)} registros")

    # --- Dataset 2: repasses_federais.csv ---
    programas = ["Saúde Básica", "Educação Fundamental", "Saneamento", "Assistência Social",
                 "Infraestrutura", "Cultura", "Esporte"]
    rep_rows = []
    for mun in municipios_reais:
        is_desvio = mun in MUNICIPIOS_DESVIO
        for ano in [2020, 2021, 2022, 2023]:
            for prog in random.sample(programas, random.randint(3, 6)):
                valor_base = random.gauss(500000, 200000)
                if is_desvio:
                    valor_base *= random.uniform(1.8, 2.5)  # Recebe MUITO repasse

                rep_rows.append({
                    "municipio": mun,
                    "ano": ano,
                    "programa": prog,
                    "valor_repassado": round(max(50000, valor_base), 2),
                    "valor_executado_declarado": round(max(50000, valor_base) * random.uniform(0.85, 1.0), 2),
                    "fonte": random.choice(["FPM", "FUNDEB", "SUS", "PAC", "Emenda Parlamentar"])
                })

    df_rep = pd.DataFrame(rep_rows)
    df_rep.to_csv(f"{OUTPUT_DIR}/projeto_10_repasses_federais.csv", index=False)
    print(f"  P10 - repasses_federais: {len(df_rep)} registros")

    # --- Dataset 3: licitacoes_municipais.csv ---
    EMPRESAS_FACHADA = [
        {"nome": "Construtora ABC Ltda", "cnpj": "12.345.678/0001-01", "socio": "José Almeida", "endereco": "Rua Fictícia, 100"},
        {"nome": "Serviços XYZ ME", "cnpj": "12.345.679/0001-02", "socio": "Maria Almeida", "endereco": "Rua Fictícia, 100"},
        {"nome": "Empreendimentos JK", "cnpj": "12.345.680/0001-03", "socio": "José Almeida Jr", "endereco": "Rua Fictícia, 102"},
        {"nome": "Consultoria Alfa", "cnpj": "12.345.681/0001-04", "socio": "Ana Almeida", "endereco": "Rua Fictícia, 100"},
    ]

    empresas_legit = [
        {"nome": f"Empresa {random.choice(['Sol', 'Norte', 'Sul', 'Mar', 'Terra', 'Rio'])} {random.choice(['Construções', 'Serviços', 'Soluções', 'Engenharia'])}",
         "cnpj": f"{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(100,999)}/0001-{random.randint(10,99)}",
         "socio": f"Sócio {j}", "endereco": f"Rua {j}, {random.randint(1,500)}"}
        for j in range(1, 31)
    ]

    lic_rows = []
    for mun in municipios_reais:
        is_desvio = mun in MUNICIPIOS_DESVIO
        n_licitacoes = random.randint(5, 20)
        if is_desvio:
            n_licitacoes = random.randint(25, 40)  # Muito mais licitações

        for _ in range(n_licitacoes):
            ano = random.choice([2020, 2021, 2022, 2023])
            objeto = random.choice([
                "Construção de escola", "Reforma de UBS", "Pavimentação de via",
                "Aquisição de equipamentos", "Serviços de consultoria",
                "Fornecimento de merenda", "Manutenção predial", "Transporte escolar",
                "Material didático", "Limpeza urbana"
            ])

            if is_desvio:
                empresa = random.choice(EMPRESAS_FACHADA)
                # Contratos fracionados: abaixo de R$80k para dispensar licitação
                valor = round(random.uniform(50000, 79000), 2) if random.random() < 0.6 else round(random.uniform(80000, 500000), 2)
                modalidade = "Dispensa" if valor < 80000 else random.choice(["Pregão", "Tomada de Preços"])
            else:
                empresa = random.choice(empresas_legit)
                valor = round(random.gauss(200000, 100000), 2)
                valor = max(30000, valor)
                modalidade = random.choice(["Pregão", "Tomada de Preços", "Concorrência", "Dispensa"])

            lic_rows.append({
                "licitacao_id": f"LIC-{len(lic_rows)+1:05d}",
                "municipio": mun,
                "ano": ano,
                "objeto": objeto,
                "valor_contrato": valor,
                "modalidade": modalidade,
                "empresa_vencedora": empresa["nome"],
                "cnpj_vencedora": empresa["cnpj"],
                "socio_principal": empresa["socio"],
                "endereco_empresa": empresa["endereco"],
                "numero_participantes": random.randint(3, 8) if not is_desvio else random.randint(1, 3),
                "status": random.choices(["Concluído", "Em execução", "Atrasado"],
                                          weights=[0.5, 0.3, 0.2] if not is_desvio else [0.3, 0.2, 0.5])[0]
            })

    df_lic = pd.DataFrame(lic_rows)
    df_lic.to_csv(f"{OUTPUT_DIR}/projeto_10_licitacoes_municipais.csv", index=False)
    print(f"  P10 - licitacoes_municipais: {len(df_lic)} registros")


# ============================================================
# EXECUTAR TODOS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("GERADOR DE DATASETS INVESTIGATIVOS — Projeto Final")
    print("MBA Ciência de Dados — UNIFOR — Turma 13")
    print("=" * 60)
    print()

    print("Projeto 01 — Operação Bisturi (Fraude Hospitalar)")
    gerar_projeto_01()
    print()

    print("Projeto 02 — Operação Marketplace (Fraude E-commerce)")
    gerar_projeto_02()
    print()

    print("Projeto 03 — Alerta Vermelho (Crise Ambiental)")
    gerar_projeto_03()
    print()

    print("Projeto 04 — Operação Nota Inflada (Fraude Educacional)")
    gerar_projeto_04()
    print()

    print("Projeto 05 — Operação Frota Fantasma (Desvio Manutenção)")
    gerar_projeto_05()
    print()

    print("Projeto 06 — Operação Curto-Circuito (Furto Energia)")
    gerar_projeto_06()
    print()

    print("Projeto 07 — Dossiê Exodus (Discriminação + Turnover)")
    gerar_projeto_07()
    print()

    print("Projeto 08 — Alerta Epidemiológico (Surto Diabetes)")
    gerar_projeto_08()
    print()

    print("Projeto 09 — Operação Lava-Imóvel (Lavagem Dinheiro)")
    gerar_projeto_09()
    print()

    print("Projeto 10 — Dossiê Desvio (Dinheiro Público)")
    gerar_projeto_10()
    print()

    print("=" * 60)
    print("RESUMO DOS DATASETS GERADOS")
    print("=" * 60)
    total_csvs = 0
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith(".csv"):
            path = os.path.join(OUTPUT_DIR, f)
            df = pd.read_csv(path)
            print(f"  {f}: {df.shape[0]:>6} linhas x {df.shape[1]:>2} colunas")
            total_csvs += 1
    print(f"\nTotal: {total_csvs} arquivos CSV gerados com sucesso!")
