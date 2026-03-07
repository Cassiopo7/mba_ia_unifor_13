# Instruções de Entrega — Projeto Final (Datathon Investigativo)

## MBA em Ciência de Dados | UNIFOR | Turma 13

**Professor:** Cássio Pinheiro
**Prazo de Entrega:** 14/03/2026 (sexta-feira), via GitHub
**Atraso:** -2.0 pontos por dia de atraso

---

## Regras de Entrega

### 1. Repositório no GitHub

- Cada equipe deve criar um **repositório público** no GitHub.
- O nome do repositório deve seguir o padrão: **`[nome-escolhido]-CDT13`**
  - Exemplos: `operacao-bisturi-CDT13`, `alerta-vermelho-CDT13`, `datathon-fraude-CDT13`
- **Todos os membros da equipe** devem ser adicionados como colaboradores do repositório.
- O professor **Cássio Pinheiro** (`Cassiopo7`) deve ser adicionado como colaborador do repositório.

### 2. Entregáveis Obrigatórios

O repositório deve conter:

| Entregável | Descrição |
|-----------|-----------|
| **Notebook (.ipynb)** | Toda a investigação com código, análises, visualizações e células Markdown narrativas |
| **README.md** | README bem escrito descrevendo o projeto, a equipe, o problema investigado, como executar o notebook, principais descobertas e conclusões |
| **Vídeo de Storytelling** | Vídeo contando a história da investigação (storytelling). Pode ser hospedado no YouTube (não-listado) ou Google Drive com link no README |
| **Datasets** | Os datasets utilizados na análise (pasta `data/`) |
| **Apresentação** (opcional) | Slides da apresentação, se houver (pasta `docs/`) |

### 3. Estrutura Sugerida do Repositório

```
nome-do-projeto-CDT13/
├── README.md                  <- Descrição do projeto, equipe, instruções
├── notebooks/
│   └── investigacao.ipynb     <- Notebook principal da análise
├── data/
│   ├── dataset1.csv           <- Datasets do projeto
│   ├── dataset2.csv
│   └── dataset3.csv
├── docs/
│   └── apresentacao.pdf       <- Slides (opcional)
└── scripts/
    └── utils.py               <- Scripts auxiliares (se houver)
```

### 4. README.md — O que deve conter

O README é a **porta de entrada** do projeto. Deve ser claro, organizado e conter:

1. **Título do projeto** e nome da operação
2. **Equipe** — nomes completos de todos os membros
3. **Descrição** — resumo do problema investigado
4. **Principais descobertas** — os insights mais relevantes da investigação
5. **Como executar** — instruções para rodar o notebook (dependências, ordem de execução)
6. **Link do vídeo** — link para o vídeo de storytelling
7. **Estrutura do repositório** — descrição dos arquivos e pastas
8. **Tecnologias utilizadas** — Python, Pandas, Matplotlib, Seaborn, etc.

### 5. Vídeo de Storytelling

- Conte a **história da investigação**, não apenas mostre gráficos.
- Estrutura sugerida:
  1. O cenário e o problema inicial
  2. O que os dados revelaram
  3. As evidências encontradas
  4. Conclusões e recomendações
- Duração sugerida: **5 a 10 minutos**
- Hospede no **YouTube (não-listado)** ou **Google Drive** e inclua o link no README.

---

## Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Qualidade da limpeza e transformação dos dados | 20% |
| Profundidade da investigação e cruzamento entre datasets | 25% |
| Qualidade e variedade das visualizações | 20% |
| Storytelling investigativo e clareza nas conclusões | 20% |
| Organização do código e boas práticas | 15% |

### Bonificações

| Bonificação | Valor |
|-------------|-------|
| Enriquecimento com dados reais (pelo menos 1 fonte pública) | +1.0 ponto |
| Uso criativo de feature engineering | +0.5 ponto |
| Visualização avançada (dashboard, gráficos interativos) | +0.5 ponto |
| Análise adicional não solicitada com insights valiosos | +0.5 ponto |

*Bonificação máxima: +2.5 pontos*

### Penalizações

| Penalização | Valor |
|-------------|-------|
| Notebook sem células Markdown explicativas | -1.0 ponto |
| Gráficos sem título, rótulos ou legendas | -0.5 ponto por gráfico |
| Código copiado sem adaptação (entre grupos) | **nota zero para ambos** |
| Entrega após o prazo (14/03) | -2.0 pontos por dia |

---

## Passo a Passo — Como entregar via GitHub (linha de comando)

### Pré-requisitos

- Ter o [Git](https://git-scm.com/) instalado
- Ter uma conta no [GitHub](https://github.com/)
- Ter o [GitHub CLI (`gh`)](https://cli.github.com/) instalado (opcional, mas recomendado)

### Passo 1 — Criar o repositório no GitHub

**Opção A: Usando GitHub CLI (`gh`)**

```bash
# Autenticar no GitHub (só precisa fazer uma vez)
gh auth login

# Criar o repositório público
gh repo create nome-do-projeto-CDT13 --public --description "Projeto Final - Datathon Investigativo - MBA Ciência de Dados UNIFOR Turma 13"

# Clonar o repositório para a máquina local
gh repo clone nome-do-projeto-CDT13
cd nome-do-projeto-CDT13
```

**Opção B: Usando Git puro (criar primeiro no site github.com)**

```bash
# 1. Crie o repositório em github.com (botão "New repository")
# 2. Clone para sua máquina:
git clone https://github.com/seu-usuario/nome-do-projeto-CDT13.git
cd nome-do-projeto-CDT13
```

### Passo 2 — Organizar os arquivos do projeto

```bash
# Criar a estrutura de pastas
mkdir -p notebooks data docs scripts

# Copiar seus arquivos para as pastas corretas
# (ajuste os caminhos conforme necessário)
cp caminho/do/seu/notebook.ipynb notebooks/
cp caminho/dos/datasets/*.csv data/
cp caminho/da/apresentacao.pdf docs/  # se houver
```

### Passo 3 — Criar o README.md

```bash
# Criar o README (edite com seu editor preferido)
touch README.md
# Abra e edite: code README.md  (VS Code)
#           ou: nano README.md   (terminal)
```

### Passo 4 — Adicionar, commitar e enviar ao GitHub

```bash
# Verificar o status dos arquivos
git status

# Adicionar todos os arquivos ao staging
git add .

# Fazer o commit
git commit -m "Entrega do Projeto Final - Datathon Investigativo CDT13"

# Enviar para o GitHub
git push origin main
```

### Passo 5 — Adicionar colaboradores (membros da equipe + professor)

**Usando GitHub CLI:**

```bash
# Adicionar cada membro da equipe como colaborador
gh api repos/{seu-usuario}/nome-do-projeto-CDT13/collaborators/{usuario-colega} -X PUT

# Adicionar o professor
gh api repos/{seu-usuario}/nome-do-projeto-CDT13/collaborators/Cassiopo7 -X PUT
```

**Pelo site do GitHub:**

1. Acesse o repositório no GitHub
2. Vá em **Settings** > **Collaborators** > **Add people**
3. Adicione o usuário de cada membro da equipe
4. Adicione o professor: **`Cassiopo7`**

### Passo 6 — Adicionar o link do vídeo ao README

```bash
# Editar o README para incluir o link do vídeo
# Adicione uma seção como:
# ## Video de Storytelling
# [Assista ao vídeo da investigação](https://link-do-video)

# Depois salve, commit e push
git add README.md
git commit -m "Adiciona link do vídeo de storytelling"
git push origin main
```

### Passo 7 — Verificar a entrega

```bash
# Confirmar que tudo foi enviado
git log --oneline

# Verificar o repositório online
gh repo view --web
```

---

## Checklist Final

Antes de considerar a entrega completa, verifique:

- [ ] Repositório criado com nome no formato `[nome]-CDT13`
- [ ] Todos os membros da equipe adicionados como colaboradores
- [ ] Professor (`Cassiopo7`) adicionado como colaborador
- [ ] Notebook (.ipynb) com toda a investigação
- [ ] Mínimo de 8 visualizações no notebook
- [ ] Células Markdown explicando cada etapa
- [ ] Cruzamento entre os 3 datasets (merge/join)
- [ ] README.md completo e bem escrito
- [ ] Link do vídeo de storytelling no README
- [ ] Datasets na pasta `data/`
- [ ] Tudo commitado e enviado (push) até **14/03/2026**

---

## Dúvidas Frequentes

**P: Posso usar repositório privado?**
R: Pode, desde que o professor (`Cassiopo7`) esteja adicionado como colaborador.

**P: O vídeo precisa mostrar o rosto?**
R: Não é obrigatório. Pode ser uma gravação de tela com narração.

**P: Posso fazer mais de um commit?**
R: Sim! Na verdade, é uma boa prática fazer commits incrementais. O importante é que até 14/03 o repositório contenha tudo.

**P: Qual o formato do vídeo?**
R: Hospede no YouTube (não-listado) ou Google Drive e coloque o link no README. Não suba o vídeo direto no GitHub (limite de 100MB por arquivo).

**P: O que acontece se eu não adicionar o professor ao repositório?**
R: Sem acesso ao repositório, não é possível avaliar. Será considerado como não entregue.

---

*Boa entrega e boas investigações!*

**Prof. Cássio Pinheiro**
MBA em Ciência de Dados — UNIFOR — 2026
