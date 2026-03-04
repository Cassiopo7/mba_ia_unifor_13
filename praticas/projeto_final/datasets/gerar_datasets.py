"""
Gerador de Datasets para o Projeto Final
MBA Ciência de Dados - UNIFOR - Turma 13
Cada dataset contém problemas intencionais (nulos, tipos, duplicatas, outliers)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

OUTPUT_DIR = "/sessions/admiring-magical-faraday/mnt/Programacao Ciencia de Dados TURMA 13/praticas/projeto_final/datasets"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# PROJETO 1 — Indicadores Hospitalares
# ============================================================
def gerar_projeto_01():
    unidades = [f"Hospital {c}" for c in ["São José", "Santa Casa", "Regional Norte", "Regional Sul",
                "Universitário", "Municipal Centro", "Municipal Leste", "Maternidade Vida",
                "Pronto-Socorro 24h", "Clínica Esperança", "Hospital do Coração", "Oncológico",
                "Infantil Anjo", "Ortopédico Plus", "Saúde Mental"]]
    especialidades = ["Clínica Médica", "Cirurgia Geral", "Pediatria", "Ortopedia",
                      "Cardiologia", "Obstetrícia", "Neurologia", "Oncologia"]

    rows = []
    for ano in [2022, 2023, 2024]:
        for mes in range(1, 13):
            for unidade in unidades:
                for esp in random.sample(especialidades, random.randint(3, 6)):
                    leitos_total = random.randint(20, 80)
                    base_ocupacao = random.gauss(0.72, 0.12)
                    # sazonalidade
                    if mes in [6, 7]:  # inverno - mais respiratórios
                        base_ocupacao += 0.08
                    ocupacao = np.clip(base_ocupacao, 0.3, 0.98)

                    internacoes = int(leitos_total * ocupacao * random.uniform(1.5, 3.0))
                    tempo_medio = max(1, random.gauss(5.5, 2.5))
                    taxa_reinternacao = max(0, random.gauss(0.08, 0.04))
                    obitos = max(0, int(internacoes * random.gauss(0.03, 0.015)))

                    faixa_etaria_predominante = random.choice(["0-14", "15-29", "30-49", "50-64", "65+"])
                    tipo_internacao = random.choice(["Urgência", "Eletiva", "Urgência", "Urgência"])

                    rows.append({
                        "ano": ano, "mes": mes, "unidade": unidade,
                        "especialidade": esp, "leitos_disponiveis": leitos_total,
                        "taxa_ocupacao": round(ocupacao, 3),
                        "internacoes": internacoes,
                        "tempo_medio_internacao_dias": round(tempo_medio, 1),
                        "taxa_reinternacao_30d": round(taxa_reinternacao, 3),
                        "obitos": obitos,
                        "faixa_etaria_predominante": faixa_etaria_predominante,
                        "tipo_internacao": tipo_internacao
                    })

    df = pd.DataFrame(rows)
    # Inserir problemas
    mask_null = np.random.random(len(df)) < 0.03
    df.loc[mask_null, "taxa_reinternacao_30d"] = np.nan
    mask_null2 = np.random.random(len(df)) < 0.02
    df.loc[mask_null2, "tempo_medio_internacao_dias"] = np.nan
    # Duplicatas intencionais
    dupes = df.sample(15)
    df = pd.concat([df, dupes], ignore_index=True)
    # Outliers
    idx_out = df.sample(5).index
    df.loc[idx_out, "tempo_medio_internacao_dias"] = np.random.uniform(30, 60, 5).round(1)

    df.to_csv(f"{OUTPUT_DIR}/projeto_01_indicadores_hospitalares.csv", index=False)
    print(f"Projeto 01: {len(df)} registros")


# ============================================================
# PROJETO 2 — E-commerce Vendas
# ============================================================
def gerar_projeto_02():
    categorias = ["Moda Feminina", "Moda Masculina", "Eletrônicos", "Casa & Decoração",
                  "Esporte & Lazer", "Beleza & Saúde", "Infantil", "Acessórios"]
    estados = ["CE", "SP", "RJ", "MG", "BA", "PE", "PA", "RS", "PR", "GO", "MA", "PI", "RN", "PB", "SE"]
    pesos_estados = [0.25, 0.15, 0.10, 0.08, 0.07, 0.06, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.03, 0.02]

    status_opcoes = ["Entregue", "Entregue", "Entregue", "Entregue", "Entregue",
                     "Cancelado", "Devolvido", "Em trânsito"]

    rows = []
    base_date = datetime(2023, 1, 1)

    for i in range(8000):
        dias = random.randint(0, 729)
        data = base_date + timedelta(days=dias)
        hora = random.choices(range(24), weights=[1,1,1,1,1,2,3,5,7,8,9,10,9,8,9,10,9,8,7,6,5,4,3,2])[0]
        minuto = random.randint(0, 59)

        cat = random.choices(categorias, weights=[0.18, 0.12, 0.20, 0.15, 0.10, 0.10, 0.08, 0.07])[0]
        estado = random.choices(estados, weights=pesos_estados)[0]

        preco_base = {"Moda Feminina": 120, "Moda Masculina": 150, "Eletrônicos": 450,
                      "Casa & Decoração": 200, "Esporte & Lazer": 180, "Beleza & Saúde": 80,
                      "Infantil": 90, "Acessórios": 60}
        preco = max(15, random.gauss(preco_base[cat], preco_base[cat] * 0.4))
        qtd = random.choices([1, 1, 1, 2, 2, 3], weights=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05])[0]

        status = random.choice(status_opcoes)
        nota = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.08, 0.15, 0.32, 0.40])[0] if status == "Entregue" else np.nan
        frete = round(random.uniform(5, 45), 2)

        rows.append({
            "pedido_id": f"PED-{i+1:06d}",
            "data_pedido": data.strftime("%Y-%m-%d"),
            "hora_pedido": f"{hora:02d}:{minuto:02d}",
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
    # Problemas: alguns preços como string
    mask = np.random.random(len(df)) < 0.02
    df.loc[mask, "preco_unitario"] = df.loc[mask, "preco_unitario"].astype(str) + " "
    # Nulos no frete
    mask_null = np.random.random(len(df)) < 0.03
    df.loc[mask_null, "frete"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_02_ecommerce_vendas.csv", index=False)
    print(f"Projeto 02: {len(df)} registros")


# ============================================================
# PROJETO 3 — Qualidade do Ar
# ============================================================
def gerar_projeto_03():
    estacoes = {
        "Centro": "urbana", "Distrito Industrial": "industrial",
        "Aldeota": "residencial", "Messejana": "residencial",
        "Porto": "industrial", "Parque do Cocó": "parque",
        "Maraponga": "residencial", "Jurema": "industrial"
    }

    rows = []
    base_date = datetime(2023, 1, 1)

    for dia in range(730):  # 2 anos
        data = base_date + timedelta(days=dia)
        mes = data.month
        # Seco: jul-dez, Chuvoso: jan-jun (CE)
        seco = mes in [7, 8, 9, 10, 11, 12]

        for estacao, tipo in estacoes.items():
            for hora in [0, 6, 12, 18]:  # 4 medições/dia
                base_mp25 = {"urbana": 22, "industrial": 35, "residencial": 15, "parque": 10}[tipo]
                base_mp10 = base_mp25 * 1.8

                # Sazonalidade
                if seco:
                    base_mp25 *= 1.3
                    base_mp10 *= 1.25

                # Hora do dia
                if hora == 12:
                    mult = 1.2
                elif hora == 18:
                    mult = 1.15
                else:
                    mult = 0.85

                mp25 = max(1, random.gauss(base_mp25 * mult, base_mp25 * 0.25))
                mp10 = max(2, random.gauss(base_mp10 * mult, base_mp10 * 0.2))
                o3 = max(0, random.gauss(40 * mult, 15))
                no2 = max(0, random.gauss(25 * (1.3 if tipo == "industrial" else 1) * mult, 10))
                so2 = max(0, random.gauss(8 * (2.0 if tipo == "industrial" else 1), 4))
                temp = random.gauss(28 + (2 if seco else -1) + (3 if hora == 12 else -2 if hora == 0 else 0), 2)
                umidade = random.gauss(70 + (-15 if seco else 10) + (-10 if hora == 12 else 5), 8)

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
    # Falhas de sensor
    for col in ["mp25_ugm3", "mp10_ugm3", "o3_ugm3"]:
        mask = np.random.random(len(df)) < 0.04
        df.loc[mask, col] = np.nan
    # Valores negativos (erro de sensor)
    idx_err = df.sample(20).index
    df.loc[idx_err, "no2_ugm3"] = -df.loc[idx_err, "no2_ugm3"].abs()

    df.to_csv(f"{OUTPUT_DIR}/projeto_03_qualidade_ar.csv", index=False)
    print(f"Projeto 03: {len(df)} registros")


# ============================================================
# PROJETO 4 — Desempenho Educacional
# ============================================================
def gerar_projeto_04():
    escolas = [f"Escola {c}" for c in ["Alpha", "Beta", "Gamma", "Delta", "Epsilon",
               "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu"]]
    series = ["6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Médio", "2º Médio", "3º Médio"]
    turnos = ["Manhã", "Tarde"]

    rows = []
    aluno_id = 1

    for escola in escolas:
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

                    # Base de desempenho influenciada por fatores
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

                    rows.append({
                        "aluno_id": f"ALU-{aluno_id:05d}",
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
    # Nulos
    mask = np.random.random(len(df)) < 0.05
    df.loc[mask, "renda_familiar"] = np.nan
    mask2 = np.random.random(len(df)) < 0.03
    df.loc[mask2, "escolaridade_pais"] = np.nan
    # Duplicatas
    dupes = df.sample(20)
    df = pd.concat([df, dupes], ignore_index=True)

    df.to_csv(f"{OUTPUT_DIR}/projeto_04_desempenho_educacional.csv", index=False)
    print(f"Projeto 04: {len(df)} registros")


# ============================================================
# PROJETO 5 — Frota e Manutenção
# ============================================================
def gerar_projeto_05():
    veiculos = []
    for i in range(200):
        tipo = random.choices(["Caminhão", "Van", "Utilitário"], weights=[0.4, 0.35, 0.25])[0]
        ano_fab = random.randint(2015, 2023)
        km_atual = random.randint(30000, 350000)
        veiculos.append({"veiculo_id": f"VEI-{i+1:04d}", "tipo": tipo, "ano_fabricacao": ano_fab, "km_atual": km_atual})

    componentes = ["Motor", "Freios", "Suspensão", "Elétrica", "Transmissão", "Pneus", "Arrefecimento", "Direção"]
    tipos_manut = ["Preventiva", "Corretiva"]

    rows = []
    base_date = datetime(2023, 7, 1)

    for _ in range(4500):
        v = random.choice(veiculos)
        dias = random.randint(0, 547)  # 18 meses
        data = base_date + timedelta(days=dias)

        comp = random.choice(componentes)
        tipo_m = random.choices(tipos_manut, weights=[0.35, 0.65])[0]

        custo_base = {"Motor": 2500, "Freios": 800, "Suspensão": 1200, "Elétrica": 600,
                      "Transmissão": 3000, "Pneus": 1500, "Arrefecimento": 700, "Direção": 900}
        custo = max(50, random.gauss(custo_base[comp] * (0.6 if tipo_m == "Preventiva" else 1.0),
                                      custo_base[comp] * 0.3))

        tempo_parado_h = max(1, random.gauss(24 if tipo_m == "Corretiva" else 8, 6))
        km_na_manut = v["km_atual"] + random.randint(-20000, 50000)

        rows.append({
            "manutencao_id": f"MAN-{len(rows)+1:05d}",
            "veiculo_id": v["veiculo_id"],
            "tipo_veiculo": v["tipo"],
            "ano_fabricacao": v["ano_fabricacao"],
            "data_manutencao": data.strftime("%Y-%m-%d"),
            "tipo_manutencao": tipo_m,
            "componente": comp,
            "custo_reais": round(custo, 2),
            "tempo_parado_horas": round(tempo_parado_h, 1),
            "km_odometro": max(1000, km_na_manut)
        })

    df = pd.DataFrame(rows)
    # Outliers de custo
    idx = df.sample(8).index
    df.loc[idx, "custo_reais"] = np.random.uniform(15000, 35000, 8).round(2)
    # Nulos
    mask = np.random.random(len(df)) < 0.04
    df.loc[mask, "tempo_parado_horas"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_05_frota_manutencao.csv", index=False)
    print(f"Projeto 05: {len(df)} registros")


# ============================================================
# PROJETO 6 — Consumo de Energia
# ============================================================
def gerar_projeto_06():
    rows = []

    for uc_id in range(1, 5001):
        classe = random.choices(["Residencial", "Comercial", "Industrial"],
                                weights=[0.70, 0.22, 0.08])[0]

        base_consumo = {"Residencial": 180, "Comercial": 1200, "Industrial": 8000}[classe]

        for ano in [2023, 2024]:
            for mes in range(1, 13):
                # Sazonalidade: mais consumo no verão (CE: set-dez)
                sazonal = 1.0
                if mes in [9, 10, 11, 12, 1, 2]:
                    sazonal = 1.15 if classe == "Residencial" else 1.08
                elif mes in [5, 6, 7]:
                    sazonal = 0.90

                consumo = max(10, random.gauss(base_consumo * sazonal, base_consumo * 0.2))
                temp_media = random.gauss(27 + (3 if mes in [10, 11, 12] else -2 if mes in [6, 7] else 0), 1.5)

                rows.append({
                    "uc_id": f"UC-{uc_id:05d}",
                    "classe": classe,
                    "ano": ano,
                    "mes": mes,
                    "consumo_kwh": round(consumo, 1),
                    "temperatura_media_c": round(temp_media, 1)
                })

    df = pd.DataFrame(rows)
    # Anomalias (possíveis fraudes)
    anomalias_idx = df[df["classe"] == "Residencial"].sample(50).index
    df.loc[anomalias_idx, "consumo_kwh"] = df.loc[anomalias_idx, "consumo_kwh"] * random.uniform(0.01, 0.1)
    # Picos anormais
    picos_idx = df.sample(30).index
    df.loc[picos_idx, "consumo_kwh"] = df.loc[picos_idx, "consumo_kwh"] * random.uniform(3, 8)
    # Nulos
    mask = np.random.random(len(df)) < 0.02
    df.loc[mask, "consumo_kwh"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_06_consumo_energia.csv", index=False)
    print(f"Projeto 06: {len(df)} registros")


# ============================================================
# PROJETO 7 — People Analytics
# ============================================================
def gerar_projeto_07():
    departamentos = ["Engenharia", "Produto", "Marketing", "Vendas", "Suporte",
                     "RH", "Financeiro", "Operações"]
    cargos = ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente"]

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

        satisfacao_trabalho = int(np.clip(random.gauss(3.5, 1.0), 1, 5))
        satisfacao_ambiente = int(np.clip(random.gauss(3.3, 1.1), 1, 5))
        equilibrio_vida = int(np.clip(random.gauss(3.0, 1.2), 1, 5))

        promovido_2anos = random.choices([1, 0], weights=[0.25, 0.75])[0]
        horas_extras_mes = int(np.clip(random.gauss(8, 6), 0, 40))

        # Probabilidade de saída
        prob_saida = 0.12
        if satisfacao_trabalho <= 2: prob_saida += 0.15
        if equilibrio_vida <= 2: prob_saida += 0.10
        if tempo_empresa_meses < 12: prob_saida += 0.08
        if tempo_empresa_meses > 24 and tempo_empresa_meses < 36: prob_saida += 0.05
        if promovido_2anos: prob_saida -= 0.08
        if horas_extras_mes > 20: prob_saida += 0.10
        if dept in ["Vendas", "Suporte"]: prob_saida += 0.05

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
    # Nulos
    mask = np.random.random(len(df)) < 0.04
    df.loc[mask, "satisfacao_trabalho"] = np.nan
    mask2 = np.random.random(len(df)) < 0.03
    df.loc[mask2, "avaliacao_desempenho"] = np.nan

    df.to_csv(f"{OUTPUT_DIR}/projeto_07_people_analytics.csv", index=False)
    print(f"Projeto 07: {len(df)} registros")


# ============================================================
# PROJETO 8 — Diabetes Clínico
# ============================================================
def gerar_projeto_08():
    rows = []

    for i in range(2000):
        idade = int(np.clip(random.gauss(48, 14), 18, 85))
        sexo = random.choice(["M", "F"])
        imc = round(np.clip(random.gauss(27, 5), 16, 50), 1)

        atividade_fisica = random.choices(
            ["Sedentário", "Leve", "Moderada", "Intensa"],
            weights=[0.35, 0.30, 0.25, 0.10]
        )[0]

        historico_familiar = random.choices([1, 0], weights=[0.35, 0.65])[0]
        tabagismo = random.choices(["Nunca", "Ex-fumante", "Fumante"], weights=[0.55, 0.25, 0.20])[0]

        # Base de risco
        risco = 0.15
        if idade > 50: risco += 0.12
        if imc > 30: risco += 0.15
        if imc > 35: risco += 0.10
        if historico_familiar: risco += 0.10
        if atividade_fisica == "Sedentário": risco += 0.08
        if atividade_fisica == "Intensa": risco -= 0.08
        if tabagismo == "Fumante": risco += 0.05

        diabetes = 1 if random.random() < risco else 0

        # Indicadores clínicos
        glicemia_base = 95 if not diabetes else 145
        glicemia = round(np.clip(random.gauss(glicemia_base, 20), 60, 350), 1)

        hba1c_base = 5.4 if not diabetes else 7.8
        hba1c = round(np.clip(random.gauss(hba1c_base, 0.8), 4.0, 14.0), 1)

        pressao_sist = int(np.clip(random.gauss(125 + (15 if diabetes else 0), 15), 90, 200))
        pressao_diast = int(np.clip(random.gauss(80 + (8 if diabetes else 0), 10), 55, 120))

        colesterol_total = round(np.clip(random.gauss(195 + (20 if diabetes else 0), 35), 100, 350), 1)
        hdl = round(np.clip(random.gauss(50 + (-8 if diabetes else 5), 12), 20, 100), 1)
        ldl = round(np.clip(random.gauss(120 + (15 if diabetes else 0), 30), 40, 250), 1)
        triglicerideos = round(np.clip(random.gauss(150 + (50 if diabetes else 0), 60), 40, 600), 1)

        # Ajuste por atividade física
        if atividade_fisica in ["Moderada", "Intensa"]:
            hdl += random.uniform(3, 10)
            triglicerideos -= random.uniform(10, 30)

        rows.append({
            "paciente_id": f"PAC-{i+1:05d}",
            "idade": idade,
            "sexo": sexo,
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
            "diagnostico_diabetes": diabetes
        })

    df = pd.DataFrame(rows)
    # Nulos em exames
    for col in ["hba1c_pct", "colesterol_total_mgdl", "triglicerideos_mgdl"]:
        mask = np.random.random(len(df)) < 0.05
        df.loc[mask, col] = np.nan
    # Alguns IMC impossíveis
    idx = df.sample(5).index
    df.loc[idx, "imc"] = [0, -1, 999, 5, 80]

    df.to_csv(f"{OUTPUT_DIR}/projeto_08_diabetes_clinico.csv", index=False)
    print(f"Projeto 08: {len(df)} registros")


# ============================================================
# PROJETO 9 — Mercado Imobiliário
# ============================================================
def gerar_projeto_09():
    bairros = {
        "Meireles": 12000, "Aldeota": 10500, "Cocó": 9500, "Dionísio Torres": 9000,
        "Varjota": 8500, "Luciano Cavalcante": 8000, "Fátima": 7000, "Centro": 5500,
        "Papicu": 6500, "Edson Queiroz": 7500, "Parquelândia": 6000, "Benfica": 5000,
        "Montese": 4500, "Parangaba": 4000, "Maraponga": 4200, "Messejana": 3800,
        "Eusébio": 5500, "Aquiraz (Beach Park)": 7000, "Caucaia": 3000, "Maracanaú": 2800
    }

    rows = []
    for i in range(3500):
        bairro = random.choice(list(bairros.keys()))
        preco_m2_base = bairros[bairro]

        tipo = random.choices(["Apartamento", "Casa", "Cobertura", "Flat/Studio"],
                              weights=[0.55, 0.25, 0.08, 0.12])[0]

        if tipo == "Apartamento":
            area = int(np.clip(random.gauss(75, 25), 30, 200))
            quartos = random.choices([1, 2, 3, 4], weights=[0.10, 0.30, 0.45, 0.15])[0]
            vagas = random.choices([1, 2, 3], weights=[0.40, 0.45, 0.15])[0]
            andar = random.randint(1, 25)
        elif tipo == "Casa":
            area = int(np.clip(random.gauss(150, 50), 60, 400))
            quartos = random.choices([2, 3, 4, 5], weights=[0.15, 0.40, 0.35, 0.10])[0]
            vagas = random.choices([1, 2, 3, 4], weights=[0.20, 0.40, 0.30, 0.10])[0]
            andar = 0
        elif tipo == "Cobertura":
            area = int(np.clip(random.gauss(180, 40), 100, 350))
            quartos = random.choices([3, 4, 5], weights=[0.30, 0.50, 0.20])[0]
            vagas = random.choices([2, 3, 4], weights=[0.30, 0.50, 0.20])[0]
            andar = random.randint(15, 30)
        else:  # Flat/Studio
            area = int(np.clip(random.gauss(35, 8), 20, 55))
            quartos = 1
            vagas = random.choices([0, 1], weights=[0.40, 0.60])[0]
            andar = random.randint(1, 20)

        condicao = random.choices(["Novo", "Usado"], weights=[0.35, 0.65])[0]
        mult_condicao = 1.15 if condicao == "Novo" else 1.0

        # Preço
        preco_m2 = max(1500, random.gauss(preco_m2_base * mult_condicao, preco_m2_base * 0.15))
        if andar > 15: preco_m2 *= 1.08
        if quartos >= 4: preco_m2 *= 1.05

        preco_total = area * preco_m2

        # Data e tempo no mercado
        ano_anuncio = random.choices([2022, 2023, 2024], weights=[0.25, 0.40, 0.35])[0]
        mes_anuncio = random.randint(1, 12)
        dias_no_mercado = int(np.clip(random.gauss(90, 60), 5, 400))
        if preco_total > 1_000_000:
            dias_no_mercado = int(dias_no_mercado * 1.4)

        rows.append({
            "imovel_id": f"IMO-{i+1:05d}",
            "bairro": bairro,
            "tipo_imovel": tipo,
            "area_m2": area,
            "quartos": quartos,
            "vagas_garagem": vagas,
            "andar": andar,
            "condicao": condicao,
            "preco_total": round(preco_total, 2),
            "preco_m2": round(preco_m2, 2),
            "ano_anuncio": ano_anuncio,
            "mes_anuncio": mes_anuncio,
            "dias_no_mercado": dias_no_mercado,
            "vendido": random.choices([1, 0], weights=[0.65, 0.35])[0]
        })

    df = pd.DataFrame(rows)
    # Nulos
    mask = np.random.random(len(df)) < 0.03
    df.loc[mask, "vagas_garagem"] = np.nan
    mask2 = np.random.random(len(df)) < 0.04
    df.loc[mask2, "dias_no_mercado"] = np.nan
    # Outliers de preço
    idx = df.sample(5).index
    df.loc[idx, "preco_total"] = [100, 50, 999999999, 1, 75000000]

    df.to_csv(f"{OUTPUT_DIR}/projeto_09_mercado_imobiliario.csv", index=False)
    print(f"Projeto 09: {len(df)} registros")


# ============================================================
# PROJETO 10 — Indicadores Municipais
# ============================================================
def gerar_projeto_10():
    # 184 municípios do Ceará (nomes reais dos maiores + genéricos)
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
    # Completar até 184
    for i in range(len(municipios_reais), 184):
        municipios_reais.append(f"Município {i+1}")

    rows = []
    for mun in municipios_reais:
        # Fortaleza como outlier positivo
        is_capital = mun == "Fortaleza"
        is_grande = mun in municipios_reais[:10]

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

        taxa_urbanizacao = np.clip(random.gauss(95 if is_capital else 75 if is_grande else 55, 12), 15, 100)

        cobertura_esgoto = np.clip(random.gauss(70 if is_capital else 50 if is_grande else 25, 15), 0, 100)
        cobertura_agua = np.clip(random.gauss(95 if is_capital else 85 if is_grande else 65, 10), 20, 100)

        receita_pc = max(500, random.gauss(2500 if is_capital else 1800 if is_grande else 1200, 400))

        rows.append({
            "municipio": mun,
            "populacao": pop,
            "pib_per_capita": round(pib_pc, 2),
            "idh": round(idh, 3),
            "taxa_analfabetismo_pct": round(taxa_analfabetismo, 1),
            "anos_estudo_medio": round(anos_estudo, 1),
            "mortalidade_infantil_por_mil": round(mortalidade_infantil, 1),
            "expectativa_vida_anos": round(expectativa_vida, 1),
            "indice_gini": round(gini, 3),
            "taxa_urbanizacao_pct": round(taxa_urbanizacao, 1),
            "cobertura_esgoto_pct": round(cobertura_esgoto, 1),
            "cobertura_agua_pct": round(cobertura_agua, 1),
            "receita_per_capita": round(receita_pc, 2)
        })

    df = pd.DataFrame(rows)
    # Nulos
    mask = np.random.random(len(df)) < 0.08
    df.loc[mask, "cobertura_esgoto_pct"] = np.nan
    mask2 = np.random.random(len(df)) < 0.05
    df.loc[mask2, "indice_gini"] = np.nan
    # Valor impossível
    idx = df.sample(3).index
    df.loc[idx, "idh"] = [1.5, -0.2, 999]

    df.to_csv(f"{OUTPUT_DIR}/projeto_10_indicadores_municipais.csv", index=False)
    print(f"Projeto 10: {len(df)} registros")


# ============================================================
# EXECUTAR TODOS
# ============================================================
if __name__ == "__main__":
    print("Gerando datasets do Projeto Final...\n")
    gerar_projeto_01()
    gerar_projeto_02()
    gerar_projeto_03()
    gerar_projeto_04()
    gerar_projeto_05()
    gerar_projeto_06()
    gerar_projeto_07()
    gerar_projeto_08()
    gerar_projeto_09()
    gerar_projeto_10()
    print("\nTodos os datasets gerados com sucesso!")

    # Resumo
    print("\n--- RESUMO ---")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith(".csv"):
            path = os.path.join(OUTPUT_DIR, f)
            df = pd.read_csv(path)
            print(f"{f}: {df.shape[0]} linhas x {df.shape[1]} colunas")
