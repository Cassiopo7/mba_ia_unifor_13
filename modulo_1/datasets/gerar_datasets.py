"""
Script para gerar 10 datasets CSV com dados realistas brasileiros.
Seed: 42 para reprodutibilidade.
Encoding: UTF-8, delimitador: virgula.
"""

import csv
import random
import os
from datetime import date, timedelta

random.seed(42)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# Dados auxiliares compartilhados
# ============================================================

NOMES_MASCULINOS = [
    "Lucas", "Gabriel", "Pedro", "Rafael", "Matheus", "Joao", "Gustavo",
    "Felipe", "Bruno", "Carlos", "Andre", "Ricardo", "Thiago", "Daniel",
    "Eduardo", "Leonardo", "Marcos", "Rodrigo", "Fernando", "Diego",
    "Vinicius", "Henrique", "Paulo", "Roberto", "Alexandre", "Caio",
    "Renato", "Fabio", "Leandro", "Sergio", "Miguel", "Arthur",
    "Bernardo", "Heitor", "Davi", "Enzo", "Samuel", "Nicolas",
    "Murilo", "Otavio"
]

NOMES_FEMININOS = [
    "Ana", "Maria", "Juliana", "Fernanda", "Camila", "Beatriz", "Larissa",
    "Mariana", "Carolina", "Amanda", "Leticia", "Gabriela", "Patricia",
    "Bruna", "Isabela", "Tatiana", "Vanessa", "Raquel", "Luciana",
    "Priscila", "Aline", "Carla", "Daniela", "Renata", "Natalia",
    "Cristina", "Luana", "Bianca", "Helena", "Manuela", "Laura",
    "Valentina", "Alice", "Sophia", "Livia", "Clara", "Cecilia",
    "Lorena", "Marina", "Isadora"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Costa",
    "Ferreira", "Rodrigues", "Almeida", "Nascimento", "Araujo", "Carvalho",
    "Gomes", "Martins", "Rocha", "Ribeiro", "Barbosa", "Barros", "Moreira",
    "Monteiro", "Teixeira", "Cardoso", "Correia", "Mendes", "Vieira",
    "Nunes", "Dias", "Freitas", "Andrade", "Campos", "Pinto", "Lopes",
    "Castro", "Melo", "Ramos", "Duarte", "Reis", "Moura", "Cunha"
]

CIDADES_ESTADOS = [
    ("Fortaleza", "CE"), ("Sao Paulo", "SP"), ("Rio de Janeiro", "RJ"),
    ("Belo Horizonte", "MG"), ("Salvador", "BA"), ("Curitiba", "PR"),
    ("Recife", "PE"), ("Porto Alegre", "RS"), ("Manaus", "AM"),
    ("Belem", "PA"), ("Goiania", "GO"), ("Brasilia", "DF"),
    ("Natal", "RN"), ("Joao Pessoa", "PB"), ("Maceio", "AL"),
    ("Teresina", "PI"), ("Sao Luis", "MA"), ("Campinas", "SP"),
    ("Florianopolis", "SC"), ("Vitoria", "ES")
]


def nome_completo():
    """Gera um nome completo brasileiro aleatorio."""
    if random.random() < 0.5:
        primeiro = random.choice(NOMES_MASCULINOS)
    else:
        primeiro = random.choice(NOMES_FEMININOS)
    sobrenome = random.choice(SOBRENOMES)
    return f"{primeiro} {sobrenome}"


def nome_completo_com_sexo():
    """Retorna (nome_completo, sexo)."""
    if random.random() < 0.5:
        primeiro = random.choice(NOMES_MASCULINOS)
        sexo = "M"
    else:
        primeiro = random.choice(NOMES_FEMININOS)
        sexo = "F"
    sobrenome = random.choice(SOBRENOMES)
    return f"{primeiro} {sobrenome}", sexo


def data_aleatoria(inicio, fim):
    """Retorna uma data aleatoria entre inicio e fim (objetos date)."""
    delta = (fim - inicio).days
    return inicio + timedelta(days=random.randint(0, delta))


def salvar_csv(nome_arquivo, cabecalho, linhas):
    """Salva lista de listas como CSV UTF-8."""
    caminho = os.path.join(OUTPUT_DIR, nome_arquivo)
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(cabecalho)
        writer.writerows(linhas)
    print(f"  -> {nome_arquivo}: {len(linhas)} linhas salvas.")


# ============================================================
# 1. alunos_notas.csv  (40 linhas)
# ============================================================
def gerar_alunos_notas():
    disciplinas = ["Matematica", "Portugues", "Historia", "Ciencias", "Ingles"]
    linhas = []
    matriculas_usadas = set()
    for _ in range(40):
        nome = nome_completo()
        while True:
            mat = f"2024{random.randint(10000, 99999)}"
            if mat not in matriculas_usadas:
                matriculas_usadas.add(mat)
                break
        disc = random.choice(disciplinas)
        notas = [round(random.uniform(0, 10), 1) for _ in range(4)]
        freq = random.randint(50, 100)
        linhas.append([nome, mat, disc, *notas, freq])
    salvar_csv("alunos_notas.csv",
               ["Nome", "Matricula", "Disciplina", "Nota1", "Nota2", "Nota3", "Nota4", "Frequencia"],
               linhas)


# ============================================================
# 2. produtos_loja.csv  (35 linhas)
# ============================================================
def gerar_produtos_loja():
    produtos_por_categoria = {
        "Eletronicos": [
            ("Fone de Ouvido Bluetooth", 89.90, 249.90),
            ("Carregador Portatil", 49.90, 149.90),
            ("Caixa de Som Bluetooth", 79.90, 399.90),
            ("Mouse Sem Fio", 39.90, 159.90),
            ("Teclado Mecanico", 129.90, 499.90),
            ("Webcam HD", 99.90, 299.90),
            ("Pen Drive 64GB", 29.90, 79.90),
            ("Cabo HDMI 2m", 19.90, 59.90),
        ],
        "Alimentos": [
            ("Cafe Torrado 500g", 12.90, 34.90),
            ("Chocolate ao Leite 200g", 7.90, 19.90),
            ("Biscoito Integral 300g", 5.90, 14.90),
            ("Azeite Extra Virgem 500ml", 19.90, 49.90),
            ("Granola Premium 800g", 14.90, 29.90),
            ("Mel Puro 500g", 18.90, 39.90),
            ("Castanha de Caju 200g", 15.90, 34.90),
        ],
        "Vestuario": [
            ("Camiseta Algodao", 29.90, 89.90),
            ("Calca Jeans", 79.90, 199.90),
            ("Tenis Esportivo", 99.90, 349.90),
            ("Bermuda Tactel", 39.90, 99.90),
            ("Vestido Casual", 59.90, 179.90),
            ("Jaqueta Corta-Vento", 89.90, 249.90),
            ("Meia Kit 3 Pares", 14.90, 39.90),
        ],
        "Limpeza": [
            ("Detergente 500ml", 2.49, 5.99),
            ("Desinfetante 2L", 7.90, 16.90),
            ("Sabao em Po 1kg", 9.90, 22.90),
            ("Agua Sanitaria 2L", 4.90, 9.90),
            ("Esponja Multiuso 3un", 3.49, 7.90),
            ("Limpador Multiuso 500ml", 5.90, 12.90),
        ],
        "Papelaria": [
            ("Caderno 200 folhas", 14.90, 39.90),
            ("Caneta Esferografica Kit 10", 9.90, 24.90),
            ("Borracha Branca", 1.50, 4.90),
            ("Lapis de Cor 24 cores", 12.90, 34.90),
            ("Regua 30cm", 2.90, 7.90),
            ("Pasta Arquivo", 6.90, 19.90),
        ],
    }
    fornecedores = [
        "Distribuidora Central", "Atacadao do Norte", "Fornecedora Nacional",
        "Mega Distribuidora", "Brasil Atacado", "Nordeste Suprimentos",
        "Sul Distribuidora", "Ponto Comercial", "Rede Abastece", "Top Fornecedora"
    ]
    linhas = []
    codigos_usados = set()
    todos_produtos = []
    for cat, prods in produtos_por_categoria.items():
        for p in prods:
            todos_produtos.append((cat, p))

    escolhidos = random.sample(todos_produtos, min(35, len(todos_produtos)))
    while len(escolhidos) < 35:
        cat, p = random.choice(todos_produtos)
        escolhidos.append((cat, p))

    for cat, (nome_prod, preco_min, preco_max) in escolhidos:
        while True:
            cod = f"P{random.randint(1000, 9999)}"
            if cod not in codigos_usados:
                codigos_usados.add(cod)
                break
        preco = round(random.uniform(preco_min, preco_max), 2)
        qtd = random.randint(0, 500)
        forn = random.choice(fornecedores)
        ativo = random.choice([True, False])
        linhas.append([cod, nome_prod, cat, preco, qtd, forn, ativo])

    salvar_csv("produtos_loja.csv",
               ["Codigo", "Produto", "Categoria", "Preco", "Quantidade_Estoque", "Fornecedor", "Ativo"],
               linhas)


# ============================================================
# 3. temperaturas_cidades.csv  (45 linhas)
# ============================================================
def gerar_temperaturas_cidades():
    linhas = []
    for _ in range(45):
        cidade, estado = random.choice(CIDADES_ESTADOS)
        dt = data_aleatoria(date(2025, 1, 1), date(2025, 3, 31))
        temp_min = round(random.uniform(15, 28), 1)
        temp_max = round(random.uniform(temp_min + 3, 40), 1)
        umidade = random.randint(30, 100)
        choveu = random.choice(["Sim", "Nao"])
        linhas.append([cidade, estado, dt.strftime("%Y-%m-%d"), temp_min, temp_max, umidade, choveu])
    salvar_csv("temperaturas_cidades.csv",
               ["Cidade", "Estado", "Data", "Temp_Min", "Temp_Max", "Umidade", "Choveu"],
               linhas)


# ============================================================
# 4. funcionarios_empresa.csv  (40 linhas)
# ============================================================
def gerar_funcionarios_empresa():
    departamentos_cargos = {
        "TI": ["Desenvolvedor", "Analista de Sistemas", "DBA", "Suporte Tecnico", "Tech Lead"],
        "RH": ["Analista de RH", "Recrutador", "Gerente de RH", "Assistente de DP"],
        "Financeiro": ["Analista Financeiro", "Contador", "Gerente Financeiro", "Tesoureiro"],
        "Marketing": ["Analista de Marketing", "Designer", "Social Media", "Gerente de Marketing"],
        "Vendas": ["Vendedor", "Gerente de Vendas", "Consultor Comercial", "Representante"],
        "Operacoes": ["Analista de Operacoes", "Supervisor", "Gerente de Operacoes", "Logistica"],
    }
    linhas = []
    for i in range(1, 41):
        nome = nome_completo()
        depto = random.choice(list(departamentos_cargos.keys()))
        cargo = random.choice(departamentos_cargos[depto])
        salario = round(random.uniform(1500, 15000), 2)
        dt_adm = data_aleatoria(date(2015, 1, 1), date(2024, 12, 31))
        cidade, _ = random.choice(CIDADES_ESTADOS)
        ativo = random.choice([True, False])
        linhas.append([i, nome, depto, cargo, salario, dt_adm.strftime("%Y-%m-%d"), cidade, ativo])
    salvar_csv("funcionarios_empresa.csv",
               ["ID", "Nome", "Departamento", "Cargo", "Salario", "Data_Admissao", "Cidade", "Ativo"],
               linhas)


# ============================================================
# 5. filmes_streaming.csv  (35 linhas)
# ============================================================
def gerar_filmes_streaming():
    titulos_por_genero = {
        "Acao": [
            "Furia nas Ruas", "Operacao Resgate", "Forca Maxima", "Alvo Final",
            "Contra-Ataque", "Zona de Combate", "Cacada Mortal", "Impacto Brutal"
        ],
        "Comedia": [
            "Minha Sogra e um Desastre", "O Estagiario Atrapalhado", "Ferias em Familia",
            "Confusao Total", "O Golpe Perfeito", "Vizinhos Loucos", "Casamento Surpresa"
        ],
        "Drama": [
            "Caminhos Cruzados", "A Ultima Carta", "Alem das Montanhas",
            "Promessas ao Vento", "O Peso do Silencio", "Recomeco", "Entre Dois Mundos"
        ],
        "Terror": [
            "A Casa Abandonada", "Sombras do Passado", "O Ritual",
            "Pesadelo Sem Fim", "Sussurros na Escuridao", "A Entidade"
        ],
        "Ficcao": [
            "Horizonte Perdido", "A Colonia", "Viajantes do Tempo",
            "Planeta Desconhecido", "O Ultimo Codigo", "Dimensao Paralela"
        ],
        "Documentario": [
            "Brasil Selvagem", "A Historia do Samba", "Oceanos em Perigo",
            "Mundos Ocultos", "Raizes do Nordeste", "A Era Digital"
        ],
    }
    idiomas = ["Portugues", "Ingles", "Espanhol", "Frances", "Japones", "Coreano"]
    linhas = []
    todos_filmes = []
    for gen, titulos in titulos_por_genero.items():
        for t in titulos:
            todos_filmes.append((t, gen))
    escolhidos = random.sample(todos_filmes, 35)
    for titulo, genero in escolhidos:
        ano = random.randint(1990, 2024)
        duracao = random.randint(80, 200)
        avaliacao = round(random.uniform(1.0, 10.0), 1)
        idioma = random.choice(idiomas)
        assistido = random.choice(["Sim", "Nao"])
        linhas.append([titulo, genero, ano, duracao, avaliacao, idioma, assistido])
    salvar_csv("filmes_streaming.csv",
               ["Titulo", "Genero", "Ano", "Duracao_Min", "Avaliacao", "Idioma", "Assistido"],
               linhas)


# ============================================================
# 6. vendas_cafeteria.csv  (50 linhas)
# ============================================================
def gerar_vendas_cafeteria():
    produtos_cafe = {
        "Bebidas": [
            ("Cafe Expresso", 4.50, 7.00),
            ("Cappuccino", 7.00, 12.00),
            ("Suco Natural", 6.00, 10.00),
            ("Agua Mineral", 2.50, 4.50),
            ("Cha Gelado", 5.00, 8.00),
            ("Cafe com Leite", 5.00, 8.50),
            ("Chocolate Quente", 7.00, 11.00),
        ],
        "Lanches": [
            ("Sanduiche Natural", 8.00, 15.00),
            ("Pao de Queijo", 3.50, 6.00),
            ("Coxinha", 4.00, 7.00),
            ("Empada", 4.50, 7.50),
            ("Misto Quente", 6.00, 10.00),
        ],
        "Sobremesas": [
            ("Bolo de Cenoura", 5.00, 9.00),
            ("Brownie", 6.00, 10.00),
            ("Torta de Limao", 7.00, 12.00),
            ("Pudim", 5.50, 9.50),
            ("Cookie", 3.50, 6.50),
        ],
    }
    formas_pagamento = ["Dinheiro", "Cartao", "Pix"]
    turnos = ["Manha", "Tarde", "Noite"]
    linhas = []
    for _ in range(50):
        dt = data_aleatoria(date(2025, 1, 1), date(2025, 3, 31))
        cat = random.choice(list(produtos_cafe.keys()))
        nome_prod, pmin, pmax = random.choice(produtos_cafe[cat])
        qtd = random.randint(1, 10)
        preco_unit = round(random.uniform(pmin, pmax), 2)
        forma = random.choice(formas_pagamento)
        turno = random.choice(turnos)
        linhas.append([dt.strftime("%Y-%m-%d"), nome_prod, cat, qtd, preco_unit, forma, turno])
    salvar_csv("vendas_cafeteria.csv",
               ["Data", "Produto", "Categoria", "Quantidade", "Preco_Unitario", "Forma_Pagamento", "Turno"],
               linhas)


# ============================================================
# 7. biblioteca_livros.csv  (35 linhas)
# ============================================================
def gerar_biblioteca_livros():
    livros = [
        ("Dom Casmurro", "Machado de Assis", "Romance"),
        ("Memorias Postumas de Bras Cubas", "Machado de Assis", "Romance"),
        ("Grande Sertao: Veredas", "Guimaraes Rosa", "Romance"),
        ("O Cortico", "Aluisio Azevedo", "Romance"),
        ("Capitaes da Areia", "Jorge Amado", "Romance"),
        ("Vidas Secas", "Graciliano Ramos", "Romance"),
        ("A Hora da Estrela", "Clarice Lispector", "Romance"),
        ("O Alquimista", "Paulo Coelho", "Ficcao"),
        ("Iracema", "Jose de Alencar", "Romance"),
        ("Macunaima", "Mario de Andrade", "Romance"),
        ("O Tempo e o Vento", "Erico Verissimo", "Romance"),
        ("Olhai os Lirios do Campo", "Erico Verissimo", "Romance"),
        ("Cem Anos de Solidao", "Gabriel Garcia Marquez", "Realismo Magico"),
        ("1984", "George Orwell", "Ficcao Cientifica"),
        ("O Senhor dos Aneis", "J.R.R. Tolkien", "Fantasia"),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia"),
        ("O Pequeno Principe", "Antoine de Saint-Exupery", "Fabula"),
        ("Crime e Castigo", "Fiodor Dostoievski", "Romance"),
        ("Orgulho e Preconceito", "Jane Austen", "Romance"),
        ("O Grande Gatsby", "F. Scott Fitzgerald", "Romance"),
        ("A Metamorfose", "Franz Kafka", "Ficcao"),
        ("O Apanhador no Campo de Centeio", "J.D. Salinger", "Romance"),
        ("A Revolucao dos Bichos", "George Orwell", "Satira"),
        ("Sapiens", "Yuval Noah Harari", "Nao Ficcao"),
        ("Breve Historia do Tempo", "Stephen Hawking", "Ciencia"),
        ("O Poder do Habito", "Charles Duhigg", "Autoajuda"),
        ("Pai Rico Pai Pobre", "Robert Kiyosaki", "Financas"),
        ("A Arte da Guerra", "Sun Tzu", "Estrategia"),
        ("O Morro dos Ventos Uivantes", "Emily Bronte", "Romance"),
        ("A Menina que Roubava Livros", "Markus Zusak", "Romance"),
        ("O Diario de Anne Frank", "Anne Frank", "Biografia"),
        ("Eu Sei Por Que o Passaro Canta na Gaiola", "Maya Angelou", "Autobiografia"),
        ("As Cronicas de Narnia", "C.S. Lewis", "Fantasia"),
        ("Duna", "Frank Herbert", "Ficcao Cientifica"),
        ("Ensaio Sobre a Cegueira", "Jose Saramago", "Romance"),
    ]
    linhas = []
    isbns_usados = set()
    for titulo, autor, genero in livros:
        while True:
            isbn = f"978-{random.randint(10, 99)}-{random.randint(1000, 9999)}-{random.randint(100, 999)}-{random.randint(0, 9)}"
            if isbn not in isbns_usados:
                isbns_usados.add(isbn)
                break
        ano_pub = random.randint(1850, 2024)
        paginas = random.randint(80, 800)
        disponivel = random.choice(["Sim", "Nao"])
        emprestimos = random.randint(0, 50)
        linhas.append([isbn, titulo, autor, genero, ano_pub, paginas, disponivel, emprestimos])
    salvar_csv("biblioteca_livros.csv",
               ["ISBN", "Titulo", "Autor", "Genero", "Ano_Publicacao", "Paginas", "Disponivel", "Emprestimos"],
               linhas)


# ============================================================
# 8. atletas_corrida.csv  (40 linhas)
# ============================================================
def gerar_atletas_corrida():
    equipes = [
        "Corredores do Parque", "Fortaleza Running", "Equipe Maratona",
        "Pelotao da Serra", "Runners Club", "Tribo da Corrida",
        "Pes de Vento", "Individual"
    ]

    def categoria_por_idade(idade):
        if idade < 20:
            return "Sub-20"
        elif idade < 30:
            return "Adulto"
        elif idade < 40:
            return "Master A"
        elif idade < 50:
            return "Master B"
        else:
            return "Master C"

    linhas = []
    for _ in range(40):
        nome, sexo = nome_completo_com_sexo()
        idade = random.randint(16, 65)
        cat = categoria_por_idade(idade)
        t5 = round(random.uniform(15, 45), 2)
        t10 = round(random.uniform(t5 + 10, 90), 2)
        cidade, _ = random.choice(CIDADES_ESTADOS)
        equipe = random.choice(equipes)
        linhas.append([nome, idade, sexo, cat, t5, t10, cidade, equipe])
    salvar_csv("atletas_corrida.csv",
               ["Nome", "Idade", "Sexo", "Categoria", "Tempo_5km", "Tempo_10km", "Cidade", "Equipe"],
               linhas)


# ============================================================
# 9. gastos_pessoais.csv  (50 linhas)
# ============================================================
def gerar_gastos_pessoais():
    categorias_descricoes = {
        "Alimentacao": [
            ("Supermercado mensal", 250, 800, "Variavel", "Sim"),
            ("Restaurante almoco", 15, 60, "Variavel", "Sim"),
            ("Delivery jantar", 20, 80, "Variavel", "Nao"),
            ("Feira livre", 30, 120, "Variavel", "Sim"),
            ("Padaria", 5, 25, "Variavel", "Sim"),
        ],
        "Transporte": [
            ("Combustivel", 100, 350, "Variavel", "Sim"),
            ("Uber/99", 10, 50, "Variavel", "Nao"),
            ("Estacionamento", 5, 25, "Variavel", "Nao"),
            ("Passagem onibus", 4, 10, "Variavel", "Sim"),
            ("Manutencao veiculo", 100, 500, "Variavel", "Sim"),
        ],
        "Moradia": [
            ("Aluguel", 800, 2500, "Fixo", "Sim"),
            ("Condominio", 200, 600, "Fixo", "Sim"),
            ("Conta de luz", 80, 300, "Variavel", "Sim"),
            ("Conta de agua", 40, 150, "Variavel", "Sim"),
            ("Internet", 80, 150, "Fixo", "Sim"),
        ],
        "Saude": [
            ("Plano de saude", 200, 800, "Fixo", "Sim"),
            ("Farmacia", 20, 150, "Variavel", "Sim"),
            ("Consulta medica", 100, 400, "Variavel", "Sim"),
            ("Academia", 60, 150, "Fixo", "Nao"),
        ],
        "Lazer": [
            ("Cinema", 20, 60, "Variavel", "Nao"),
            ("Streaming", 20, 55, "Fixo", "Nao"),
            ("Bar com amigos", 30, 120, "Variavel", "Nao"),
            ("Viagem fim de semana", 200, 800, "Variavel", "Nao"),
        ],
        "Educacao": [
            ("Mensalidade curso", 300, 2000, "Fixo", "Sim"),
            ("Livros", 30, 150, "Variavel", "Nao"),
            ("Curso online", 30, 200, "Variavel", "Nao"),
            ("Material escolar", 20, 100, "Variavel", "Sim"),
        ],
        "Vestuario": [
            ("Roupas", 50, 300, "Variavel", "Nao"),
            ("Calcados", 80, 400, "Variavel", "Nao"),
            ("Acessorios", 20, 100, "Variavel", "Nao"),
        ],
    }
    formas_pagamento = ["Dinheiro", "Cartao", "Pix", "Boleto", "Debito Automatico"]
    linhas = []
    for _ in range(50):
        dt = data_aleatoria(date(2025, 1, 1), date(2025, 3, 31))
        cat = random.choice(list(categorias_descricoes.keys()))
        desc, vmin, vmax, tipo, essencial = random.choice(categorias_descricoes[cat])
        valor = round(random.uniform(vmin, vmax), 2)
        forma = random.choice(formas_pagamento)
        linhas.append([dt.strftime("%Y-%m-%d"), desc, cat, valor, tipo, forma, essencial])
    salvar_csv("gastos_pessoais.csv",
               ["Data", "Descricao", "Categoria", "Valor", "Tipo", "Forma_Pagamento", "Essencial"],
               linhas)


# ============================================================
# 10. pacientes_clinica.csv  (40 linhas)
# ============================================================
def gerar_pacientes_clinica():
    tipos_sanguineos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    linhas = []
    for i in range(1, 41):
        nome, sexo = nome_completo_com_sexo()
        idade = random.randint(18, 85)
        tipo_sang = random.choice(tipos_sanguineos)
        pressao_sist = random.randint(90, 180)
        pressao_diast = random.randint(60, min(120, pressao_sist - 10))
        glicemia = random.randint(60, 250)
        imc = round(random.uniform(16, 40), 1)
        fumante = random.choice(["Sim", "Nao"])
        linhas.append([i, nome, idade, sexo, tipo_sang, pressao_sist, pressao_diast, glicemia, imc, fumante])
    salvar_csv("pacientes_clinica.csv",
               ["ID", "Nome", "Idade", "Sexo", "Tipo_Sanguineo", "Pressao_Sistolica",
                "Pressao_Diastolica", "Glicemia", "IMC", "Fumante"],
               linhas)


# ============================================================
# Execucao principal
# ============================================================
if __name__ == "__main__":
    print("Gerando datasets...\n")
    gerar_alunos_notas()
    gerar_produtos_loja()
    gerar_temperaturas_cidades()
    gerar_funcionarios_empresa()
    gerar_filmes_streaming()
    gerar_vendas_cafeteria()
    gerar_biblioteca_livros()
    gerar_atletas_corrida()
    gerar_gastos_pessoais()
    gerar_pacientes_clinica()
    print(f"\nTodos os 10 datasets foram gerados em:\n{OUTPUT_DIR}")
