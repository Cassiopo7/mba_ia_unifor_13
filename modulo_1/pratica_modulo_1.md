# 📚 Prática - Módulo 1: Fundamentos de Programação com Python

**Disciplina:** Programação para Ciência de Dados  
**Instrutor:** Cássio Pinheiro  
**Instituição:** MBA Ciência de Dados - Universidade de Fortaleza  
**Autor:** [@cassiopo7](https://github.com/cassiopo7)

---

## 📋 Índice

1. [Sobre a Prática](#sobre-a-prática)
2. [Pré-requisitos](#pré-requisitos)
3. [Exercícios](#exercícios)
   - [Exercício 1: Tipos de Dados e Operações Básicas](#exercício-1-tipos-de-dados-e-operações-básicas)
   - [Exercício 2: Estruturas de Dados Fundamentais](#exercício-2-estruturas-de-dados-fundamentais)
   - [Exercício 3: Estruturas de Controle](#exercício-3-estruturas-de-controle)
   - [Exercício 4: Compreensões e Programação Funcional](#exercício-4-compreensões-e-programação-funcional)
   - [Exercício 5: Funções Avançadas](#exercício-5-funções-avançadas)
   - [Exercício 6: Manipulação de Arquivos](#exercício-6-manipulação-de-arquivos)
4. [Desafio Final](#desafio-final)
5. [Como Contribuir](#como-contribuir)

---

## Sobre a Prática

Esta prática foi desenvolvida para consolidar os conhecimentos do **Módulo 1 - Fundamentos de Programação com Python**, abordando:

- ✅ Tipos de dados e operações básicas
- ✅ Estruturas de dados (listas, dicionários, tuplas, sets)
- ✅ Estruturas de controle (condicionais e laços)
- ✅ Compreensões e programação funcional
- ✅ Funções avançadas
- ✅ Manipulação de arquivos

**⚠️ Nível:** Avançado - Recomendado para trabalho em duplas  
**⏱️ Tempo estimado:** 4-6 horas  

---

## Pré-requisitos

- Python 3.8 ou superior instalado
- Editor de código ou IDE (VS Code, PyCharm, Jupyter Notebook, etc.)
- Conhecimento básico de terminal/comando de linha

### Verificar versão do Python

```bash
python --version
# ou
python3 --version
```

---

## Exercícios

### Exercício 1: Sistema de Análise Financeira Completo

**Objetivo:** Criar um sistema completo de análise financeira que integre múltiplos conceitos de Python.

**Complexidade:** ⭐⭐⭐⭐  
**Tempo estimado:** 60-90 minutos

#### Desafio:

Você foi contratado para desenvolver um sistema de análise financeira para uma pequena empresa. O sistema deve:

1. **Calculadora Financeira Avançada:**
   - Calcular juros compostos: `M = P * (1 + i)^n`
   - Calcular valor presente líquido (VPL) de uma série de fluxos de caixa
   - Calcular taxa interna de retorno (TIR) aproximada
   - Converter entre diferentes taxas (mensal, anual, diária)

2. **Análise de Despesas:**
   - Receber múltiplas transações financeiras (data, descrição, valor, categoria)
   - Calcular totais por categoria
   - Identificar meses com maior gasto
   - Calcular média mensal de gastos

3. **Relatórios Formatados:**
   - Gerar relatório em texto formatado
   - Exportar dados para arquivo CSV

**Estrutura de dados esperada:**
```python
transacoes = [
    {'data': '2024-01-15', 'descricao': 'Aluguel', 'valor': -1500.00, 'categoria': 'Moradia'},
    {'data': '2024-01-20', 'descricao': 'Salário', 'valor': 5000.00, 'categoria': 'Renda'},
    {'data': '2024-02-01', 'descricao': 'Supermercado', 'valor': -350.00, 'categoria': 'Alimentação'},
    # ... mais transações
]
```

**Requisitos técnicos:**
- Usar funções com documentação completa (docstrings)
- Implementar tratamento de erros robusto
- Utilizar compreensões onde apropriado
- Validar todos os inputs do usuário
- Formatar saídas usando f-strings

**Entregáveis:**
1. Função `calcular_juros_compostos(principal, taxa, periodo)`
2. Função `analisar_transacoes(transacoes)`
3. Função `gerar_relatorio(transacoes, arquivo_saida)`
4. Função `exportar_csv(transacoes, arquivo)`
5. Script principal com menu interativo

**Teste com os seguintes dados:**
```python
transacoes_teste = [
    {'data': '2024-01-15', 'descricao': 'Aluguel', 'valor': -1500.00, 'categoria': 'Moradia'},
    {'data': '2024-01-20', 'descricao': 'Salário', 'valor': 5000.00, 'categoria': 'Renda'},
    {'data': '2024-02-01', 'descricao': 'Supermercado', 'valor': -350.00, 'categoria': 'Alimentação'},
    {'data': '2024-02-05', 'descricao': 'Conta de Luz', 'valor': -120.00, 'categoria': 'Moradia'},
    {'data': '2024-02-15', 'descricao': 'Aluguel', 'valor': -1500.00, 'categoria': 'Moradia'},
    {'data': '2024-02-20', 'descricao': 'Salário', 'valor': 5000.00, 'categoria': 'Renda'},
    {'data': '2024-02-25', 'descricao': 'Restaurante', 'valor': -180.00, 'categoria': 'Alimentação'},
]
```

**Dicas:**
- Use `datetime` para manipular datas
- Considere usar `reduce` para cálculos acumulados
- Implemente validação de dados antes de processar
- Use dicionários para agrupar por categoria

---

### Exercício 2: Sistema de Gerenciamento Acadêmico Avançado

**Objetivo:** Desenvolver um sistema completo de gerenciamento acadêmico utilizando estruturas de dados complexas.

**Complexidade:** ⭐⭐⭐⭐⭐  
**Tempo estimado:** 90-120 minutos

#### Desafio:

Você precisa criar um sistema de gerenciamento acadêmico completo que gerencie alunos, cursos, disciplinas e notas. O sistema deve:

1. **Gerenciamento de Cursos:**
   - Cadastrar cursos com código, nome, carga horária
   - Cada curso tem múltiplas disciplinas
   - Cada disciplina tem código, nome, créditos, pré-requisitos

2. **Gerenciamento de Alunos:**
   - Cadastrar alunos com matrícula única, nome, CPF, email
   - Vincular aluno a um curso
   - Matricular aluno em disciplinas (respeitando pré-requisitos)
   - Registrar notas (múltiplas avaliações por disciplina)

3. **Sistema de Análise:**
   - Calcular CR (Coeficiente de Rendimento) por aluno
   - Calcular média da turma por disciplina
   - Identificar alunos em risco (CR < 6.0)
   - Gerar relatório de aprovação/reprovação
   - Calcular estatísticas de frequência por disciplina

4. **Operações Avançadas:**
   - Buscar alunos por intervalo de CR
   - Listar disciplinas sem pré-requisitos disponíveis para um aluno
   - Calcular progresso do aluno (% de disciplinas concluídas)
   - Identificar conflitos de horário (mesmo horário)

**Estrutura de dados sugerida:**
```python
# Sistema completo de dados
sistema_academico = {
    'cursos': {
        'CC001': {
            'nome': 'Ciência da Computação',
            'carga_horaria': 3200,
            'disciplinas': {
                'CC001-01': {
                    'nome': 'Programação I',
                    'creditos': 4,
                    'pre_requisitos': [],
                    'horario': 'Segunda 08:00-10:00'
                },
                'CC001-02': {
                    'nome': 'Estrutura de Dados',
                    'creditos': 4,
                    'pre_requisitos': ['CC001-01'],
                    'horario': 'Quarta 08:00-10:00'
                }
            }
        }
    },
    'alunos': {
        'MAT2024001': {
            'nome': 'João Silva',
            'cpf': '123.456.789-00',
            'email': 'joao@email.com',
            'curso': 'CC001',
            'matriculas': {
                'CC001-01': {
                    'notas': [8.5, 9.0, 7.5],
                    'frequencia': 85
                }
            }
        }
    }
}
```

**Requisitos técnicos:**
- Usar dicionários aninhados para estruturar dados
- Implementar funções de validação (CPF, email, matrícula única)
- Usar sets para verificar pré-requisitos
- Utilizar list comprehensions para filtros e transformações
- Criar funções que retornem múltiplos valores (tuplas)
- Implementar busca eficiente usando compreensões

**Entregáveis:**
1. Função `cadastrar_curso(codigo, nome, carga_horaria)`
2. Função `cadastrar_aluno(matricula, dados_aluno)`
3. Função `matricular_aluno(matricula, codigo_disciplina)`
4. Função `calcular_cr(matricula)`
5. Função `gerar_relatorio_aluno(matricula)`
6. Função `estatisticas_turma(codigo_disciplina)`
7. Função `exportar_dados_json(arquivo)` (salvar em JSON)
8. Função `importar_dados_json(arquivo)` (carregar de JSON)

**Casos de teste:**
- Matricular aluno sem pré-requisitos deve falhar
- Calcular CR considerando apenas disciplinas com nota final
- Verificar matrícula duplicada em mesma disciplina
- Validar formato de CPF e email

**Dicas:**
- Use `json` para persistência
- Implemente validação de CPF (11 dígitos)
- Use `any()` e `all()` para validações complexas
- Considere criar uma classe helper para validações

---

### Exercício 3: Processador de Texto e Análise de Dados

**Objetivo:** Criar um sistema completo de processamento e análise de texto usando estruturas de controle avançadas.

**Complexidade:** ⭐⭐⭐⭐  
**Tempo estimado:** 75-90 minutos

#### Desafio:

Desenvolva um processador de texto que analise documentos e gere estatísticas detalhadas. O sistema deve:

1. **Análise de Texto:**
   - Contar palavras, caracteres (com e sem espaços), parágrafos
   - Identificar palavras mais frequentes (top N)
   - Calcular média de palavras por frase
   - Identificar palavras únicas
   - Contar ocorrências de uma palavra específica

2. **Estatísticas Avançadas:**
   - Calcular índice de diversidade lexical (palavras únicas / total palavras)
   - Identificar palavras mais longas e mais curtas
   - Encontrar frases mais longas (por número de palavras)
   - Calcular frequência de pontuação

3. **Processamento de Múltiplos Arquivos:**
   - Processar múltiplos arquivos de texto
   - Comparar estatísticas entre arquivos
   - Identificar palavras em comum entre arquivos
   - Gerar relatório comparativo

4. **Filtros e Buscas:**
   - Buscar frases que contenham uma palavra específica
   - Filtrar palavras por tamanho mínimo/máximo
   - Buscar padrões usando condições complexas

**Exemplo de texto de teste:**
```
A ciência de dados é uma área interdisciplinar que utiliza métodos científicos, 
processos, algoritmos e sistemas para extrair conhecimento e insights de dados 
estruturados e não estruturados. A ciência de dados está relacionada à mineração 
de dados, aprendizado de máquina e big data.
```

**Requisitos técnicos:**
- Usar loops aninhados onde necessário
- Implementar funções recursivas para busca
- Usar estruturas condicionais complexas (elif, operadores lógicos)
- Validar entradas e tratar erros
- Criar menu interativo com while loop

**Entregáveis:**
1. Função `analisar_texto(texto)` - retorna dicionário com todas as estatísticas
2. Função `palavras_mais_frequentes(texto, n=10)` - top N palavras
3. Função `buscar_frases_com_palavra(texto, palavra)`
4. Função `comparar_arquivos(arquivo1, arquivo2)` - comparação de estatísticas
5. Função `gerar_relatorio(texto, arquivo_saida)` - relatório formatado
6. Script principal com menu interativo

**Casos de teste:**
- Processar arquivo vazio
- Arquivo com caracteres especiais
- Texto com múltiplos idiomas
- Arquivo muito grande (performance)

**Dicas:**
- Use `split()` para separar palavras
- Considere usar `Counter` do módulo `collections` para contagem
- Normalize texto (lowercase, remover pontuação)
- Implemente tratamento de encoding (UTF-8)

---

### Exercício 4: Pipeline de Processamento de Dados com Programação Funcional

**Objetivo:** Criar um pipeline completo de processamento de dados usando compreensões avançadas e programação funcional.

**Complexidade:** ⭐⭐⭐⭐⭐  
**Tempo estimado:** 90-120 minutos

#### Desafio:

Você precisa criar um sistema de pipeline de processamento de dados que transforme dados brutos em informações estruturadas e analisadas. O sistema deve:

1. **Pipeline de Transformação:**
   - Carregar dados de múltiplas fontes (lista de dicionários, CSV, JSON)
   - Aplicar transformações em cascata usando `map`, `filter`, `reduce`
   - Criar múltiplas visualizações dos dados usando compreensões

2. **Operações Funcionais Avançadas:**
   - Implementar funções de ordem superior (funções que recebem funções)
   - Criar decoradores para logging e validação
   - Implementar composição de funções
   - Criar pipeline funcional encadeado

3. **Análise com Compreensões:**
   - Gerar relatórios usando dict/set comprehensions aninhadas
   - Criar estruturas de dados complexas em uma linha
   - Otimizar código usando compreensões ao invés de loops

4. **Processamento Assíncrono Simulado:**
   - Processar múltiplos datasets em paralelo (simulado)
   - Agregar resultados usando reduce
   - Validar dados usando funções de alta ordem

**Dados de exemplo:**
```python
vendas_brutas = [
    {'produto': 'Notebook', 'preco': 3500.00, 'quantidade': 2, 'desconto': 0.1, 'categoria': 'Eletrônicos'},
    {'produto': 'Mouse', 'preco': 50.00, 'quantidade': 5, 'desconto': 0.0, 'categoria': 'Acessórios'},
    {'produto': 'Teclado', 'preco': 150.00, 'quantidade': 3, 'desconto': 0.15, 'categoria': 'Acessórios'},
    {'produto': 'Monitor', 'preco': 800.00, 'quantidade': 1, 'desconto': 0.05, 'categoria': 'Eletrônicos'},
    # ... mais vendas
]
```

**Requisitos técnicos:**
- Usar apenas programação funcional (sem loops explícitos onde possível)
- Criar funções puras (sem efeitos colaterais)
- Implementar composição de funções
- Usar `functools.partial` para criar funções especializadas
- Criar decoradores personalizados
- Usar `operator` module para operações funcionais

**Entregáveis:**
1. Função `pipeline_transformacao(dados)` - pipeline completo usando map/filter/reduce
2. Função `analisar_por_categoria(dados)` - análise usando dict comprehension
3. Função `compor_funcoes(*funcoes)` - compositor de funções genérico
4. Decorador `@validar_dados(tipo_esperado)` - validação automática
5. Decorador `@log_execucao` - logging automático
6. Função `processar_em_lote(datasets, funcao)` - processamento em lote funcional
7. Função `gerar_relatorio_funcional(dados)` - relatório usando apenas compreensões

**Casos de teste:**
- Pipeline com dados vazios
- Pipeline com dados inválidos (deve filtrar)
- Compor múltiplas transformações
- Performance comparativa (compreensões vs loops)

**Exemplo de uso esperado:**
```python
# Pipeline funcional
resultado = pipeline_transformacao(
    vendas_brutas,
    transformacoes=[
        lambda x: calcular_total(x),
        lambda x: aplicar_desconto(x),
        lambda x: categorizar(x)
    ],
    filtros=[
        lambda x: x['total'] > 100
    ]
)
```

**Dicas:**
- Use `functools.partial` para criar funções especializadas
- Explore `operator` module para operações funcionais
- Considere criar uma classe `Pipeline` usando métodos funcionais
- Use `itertools` para operações avançadas

---

### Exercício 5: Sistema de Biblioteca Digital com Persistência de Dados

**Objetivo:** Criar um sistema completo de biblioteca digital com persistência de dados em múltiplos formatos.

**Complexidade:** ⭐⭐⭐⭐⭐  
**Tempo estimado:** 120-150 minutos

#### Desafio:

Desenvolva um sistema completo de biblioteca digital que gerencie livros, usuários, empréstimos e relatórios com persistência completa em arquivos.

1. **Gerenciamento de Livros:**
   - CRUD completo (Create, Read, Update, Delete)
   - Busca avançada (por título, autor, ISBN, gênero, ano)
   - Validação de ISBN (formato e dígito verificador)
   - Controle de estoque e disponibilidade

2. **Sistema de Usuários:**
   - Cadastro com validações (CPF, email, telefone)
   - Histórico completo de empréstimos
   - Sistema de multas (atraso na devolução)
   - Limite de livros por usuário

3. **Sistema de Empréstimos:**
   - Realizar empréstimo com validações
   - Calcular data de devolução automática
   - Renovação de empréstimos
   - Devolução com cálculo de multa
   - Histórico completo de transações

4. **Persistência Multi-Formato:**
   - Salvar em JSON (dados completos)
   - Exportar relatórios em CSV
   - Gerar logs em arquivo de texto
   - Backup automático dos dados

5. **Relatórios e Estatísticas:**
   - Livros mais emprestados
   - Usuários mais frequentes
   - Livros atrasados
   - Estatísticas por gênero
   - Relatório financeiro (multas)

**Estrutura de dados:**
```python
biblioteca = {
    'livros': {
        'ISBN1234567890': {
            'titulo': 'Python para Ciência de Dados',
            'autor': 'João Silva',
            'ano': 2023,
            'genero': 'Técnico',
            'estoque': 5,
            'disponivel': 3
        }
    },
    'usuarios': {
        'USER001': {
            'nome': 'Maria Santos',
            'cpf': '123.456.789-00',
            'email': 'maria@email.com',
            'telefone': '(85) 99999-9999',
            'emprestimos_ativos': [],
            'historico': []
        }
    },
    'emprestimos': {
        'EMP001': {
            'isbn': 'ISBN1234567890',
            'usuario': 'USER001',
            'data_emprestimo': '2024-01-15',
            'data_devolucao_prevista': '2024-01-29',
            'data_devolucao_real': None,
            'status': 'ativo',
            'multa': 0.0
        }
    }
}
```

**Requisitos técnicos:**
- Funções com documentação completa (docstrings)
- Tratamento de erros robusto (try/except)
- Validação de todos os inputs
- Funções de backup e restore
- Context managers para manipulação de arquivos
- Uso de `json`, `csv`, e manipulação de arquivos texto
- Funções auxiliares bem organizadas

**Entregáveis:**
1. Função `cadastrar_livro(dados_livro)` - com validação de ISBN
2. Função `cadastrar_usuario(dados_usuario)` - com validações completas
3. Função `realizar_emprestimo(isbn, usuario_id)` - com todas as validações
4. Função `devolver_livro(emprestimo_id)` - com cálculo de multa
5. Função `buscar_livros(**criterios)` - busca flexível
6. Função `salvar_dados(arquivo_json)` - persistência completa
7. Função `carregar_dados(arquivo_json)` - carregamento seguro
8. Função `gerar_relatorio_csv(tipo_relatorio, arquivo_saida)`
9. Função `backup_dados()` - backup automático
10. Script principal com menu completo e tratamento de erros

**Casos de teste:**
- Empréstimo com livro indisponível
- Usuário com limite de livros atingido
- Devolução com atraso (cálculo de multa)
- Validação de ISBN inválido
- Recuperação de backup após erro

**Dicas:**
- Use `contextlib` para criar context managers customizados
- Implemente validação de ISBN-13 (algoritmo de validação)
- Use `datetime` para cálculos de datas
- Considere usar `pathlib` para manipulação de arquivos
- Implemente logging em arquivo separado

---

## Desafio Final Integrado

### 🎯 Sistema Integrado de Gestão Empresarial

**Objetivo:** Integrar todos os conceitos aprendidos em um sistema completo e funcional.

**Complexidade:** ⭐⭐⭐⭐⭐  
**Tempo estimado:** 4-6 horas (trabalho em duplas)  
**Entrega:** Código completo + Documentação + Apresentação

#### Desafio Completo:

Você e seu parceiro foram contratados para desenvolver um **Sistema Integrado de Gestão Empresarial** que combine funcionalidades de:
- Gestão financeira
- Gestão de recursos humanos
- Gestão de estoque
- Sistema de relatórios e análises

O sistema deve integrar **TODOS** os conceitos do Módulo 1:

#### Módulos Obrigatórios:

1. **Módulo Financeiro** (conceitos do Exercício 1)
   - Registro de receitas e despesas
   - Cálculo de indicadores financeiros
   - Análise de fluxo de caixa
   - Exportação para CSV

2. **Módulo de RH** (conceitos do Exercício 2)
   - Cadastro de funcionários
   - Cálculo de folha de pagamento
   - Gestão de férias e benefícios
   - Relatórios de desempenho

3. **Módulo de Estoque** (conceitos do Exercício 3)
   - Controle de produtos
   - Entrada e saída de mercadorias
   - Alertas de estoque mínimo
   - Análise de rotatividade

4. **Módulo de Análises** (conceitos do Exercício 4)
   - Pipeline de processamento de dados
   - Análises estatísticas
   - Visualizações de dados
   - Relatórios executivos

5. **Módulo de Persistência** (conceitos do Exercício 5)
   - Salvar/carregar dados em JSON
   - Exportação para CSV
   - Sistema de logs
   - Backup automático

#### Requisitos Técnicos Obrigatórios:

- ✅ Mínimo de 20 funções bem documentadas
- ✅ Uso de todos os tipos de dados (listas, dicts, tuplas, sets)
- ✅ Estruturas de controle complexas (loops aninhados, condicionais)
- ✅ Compreensões (list, dict, set comprehensions)
- ✅ Programação funcional (map, filter, reduce)
- ✅ Funções avançadas (argumentos variáveis, decoradores)
- ✅ Manipulação de arquivos (JSON, CSV, TXT)
- ✅ Tratamento de erros robusto
- ✅ Validação de dados completa
- ✅ Menu interativo completo

#### Entregáveis:

1. **Código Python completo** (organizado em módulos)
2. **Documentação técnica** (README.md explicando o sistema)
3. **Manual do usuário** (como usar o sistema)
4. **Apresentação** (10-15 minutos demonstrando o sistema)
5. **Testes** (casos de teste para validação)

#### Critérios de Avaliação:

- **Funcionalidade (40%)**: Sistema funciona completamente
- **Qualidade do Código (30%)**: Código limpo, documentado, organizado
- **Integração (20%)**: Módulos integrados corretamente
- **Apresentação (10%)**: Demonstração clara e profissional

#### Sugestões de Estrutura:

```
sistema_gestao/
├── modulos/
│   ├── financeiro.py
│   ├── rh.py
│   ├── estoque.py
│   ├── analises.py
│   └── persistencia.py
├── utils/
│   ├── validacoes.py
│   ├── formatadores.py
│   └── helpers.py
├── dados/
│   ├── financeiro.json
│   ├── rh.json
│   ├── estoque.json
│   └── logs/
├── relatorios/
├── main.py
├── README.md
└── requirements.txt
```

#### Dicas para Trabalho em Duplas:

1. **Dividam responsabilidades** por módulos
2. **Comuniquem-se constantemente** sobre interfaces entre módulos
3. **Testem integrações** desde o início
4. **Documentem** enquanto desenvolvem
5. **Versionem** o código (Git)

**Boa sorte! Este desafio vai consolidar todo o conhecimento do Módulo 1! 🚀**

---

## Como Contribuir

Sinta-se à vontade para:

1. **Fork** este repositório
2. Criar uma **branch** para sua melhoria (`git checkout -b feature/minha-melhoria`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/minha-melhoria`)
5. Abrir um **Pull Request**

### Sugestões de Melhorias

- Adicionar mais exercícios práticos
- Incluir testes unitários
- Criar exemplos de soluções
- Adicionar diagramas explicativos
- Traduzir para outros idiomas

---

## 📝 Licença

Este material é fornecido para fins educacionais. Sinta-se livre para usar, modificar e compartilhar.

---

## 👤 Autor

**Cássio Pinheiro**

- GitHub: [@cassiopo7](https://github.com/cassiopo7)
- Instituição: Universidade de Fortaleza
- Curso: MBA Ciência de Dados

---

## 🙏 Agradecimentos

Agradecimentos à Universidade de Fortaleza e ao programa de MBA em Ciência de Dados pela oportunidade de compartilhar conhecimento.

---

**Última atualização:** Janeiro 2024  
**Versão:** 1.0.0

