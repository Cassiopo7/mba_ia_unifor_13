# 🖥️ Guia de Instalação e Configuração do Ambiente

## MBA Inteligência Artificial – Universidade de Fortaleza
### Disciplina: Programação para Ciência de Dados – Turma 13
### Instrutor: Cássio Pinheiro

---

<br>

# 📦 Repositório do Curso

<div align="center">

### Escaneie o QR Code para acessar o repositório:

![QR Code do Repositório](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://github.com/Cassiopo7/mba_ia_unifor_13.git)

### 🔗 https://github.com/Cassiopo7/mba_ia_unifor_13

</div>

---

<br>

# 🐍 Etapa 1 – Instalar o Python

<br>

## Windows

### 1.1 Acesse o site oficial

```
https://www.python.org/downloads/
```

### 1.2 Baixe a versão mais recente (3.12+)

> Clique no botão amarelo **"Download Python 3.x.x"**

### 1.3 Execute o instalador

> ⚠️ **IMPORTANTE: Marque a opção abaixo ANTES de clicar em "Install Now"**

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   ☑  Add python.exe to PATH    ← MARQUE ESTA OPÇÃO!    │
│                                                         │
│   [ Install Now ]                                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> Se esquecer de marcar esta opção, o Python não será reconhecido no terminal.

---

## macOS

### Opção A – Site oficial (mais simples)

```
https://www.python.org/downloads/
```

Baixe o instalador `.pkg` e execute.

### Opção B – Via Homebrew (recomendado para quem já usa)

```bash
brew install python
```

---

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

---

<br>

# ✅ Etapa 2 – Verificar a Instalação do Python

Abra o **Terminal** (macOS/Linux) ou **Prompt de Comando / PowerShell** (Windows):

```bash
python --version
```

> Resultado esperado:

```
Python 3.12.x
```

> ⚠️ No macOS/Linux pode ser necessário usar `python3`:

```bash
python3 --version
```

### Verificar o pip (gerenciador de pacotes):

```bash
pip --version
```

> Resultado esperado:

```
pip 24.x.x from ... (python 3.12)
```

> ⚠️ No macOS/Linux pode ser necessário usar `pip3`:

```bash
pip3 --version
```

---

<br>

# 📝 Etapa 3 – Instalar o Visual Studio Code (VS Code)

<br>

## 3.1 Baixar o VS Code

```
https://code.visualstudio.com/
```

> Clique no botão grande **"Download"** – o site detecta automaticamente seu sistema operacional.

```
┌──────────────────────────────────────────┐
│                                          │
│        Visual Studio Code                │
│                                          │
│    [ ⬇ Download for Windows/Mac ]        │
│                                          │
└──────────────────────────────────────────┘
```

## 3.2 Instalar

| Sistema | Instrução |
|---------|-----------|
| **Windows** | Execute o `.exe` baixado → Aceite os termos → Marque **"Add to PATH"** → Install |
| **macOS** | Arraste o app para a pasta **Applications** |
| **Linux** | Use o `.deb` ou `.rpm` baixado, ou instale via snap: `sudo snap install code --classic` |

---

<br>

# 🧩 Etapa 4 – Instalar Extensões Essenciais no VS Code

Abra o VS Code e acesse as extensões:

```
Atalho:  Ctrl + Shift + X   (Windows/Linux)
         Cmd + Shift + X    (macOS)
```

```
┌──────────────────────────────────────────────────────────┐
│  🔍 Buscar extensões...                                  │
│                                                          │
│  Pesquise e instale cada uma das extensões abaixo:       │
└──────────────────────────────────────────────────────────┘
```

<br>

## 🔴 Obrigatórias

| # | Extensão | Buscar por | Para que serve |
|---|----------|------------|----------------|
| 1 | **Python** | `ms-python.python` | Suporte completo à linguagem Python |
| 2 | **Jupyter** | `ms-toolsai.jupyter` | Executar notebooks `.ipynb` no VS Code |
| 3 | **Pylance** | `ms-python.vscode-pylance` | Autocompletar e verificação de tipos |

<br>

## 🟡 Recomendadas

| # | Extensão | Buscar por | Para que serve |
|---|----------|------------|----------------|
| 4 | **Python Indent** | `KevinRose.vsc-python-indent` | Indentação automática correta |
| 5 | **indent-rainbow** | `oderwat.indent-rainbow` | Colorir níveis de indentação |
| 6 | **Portuguese (Brazil) Language Pack** | `MS-CEINTL.vscode-language-pack-pt-BR` | Interface em português |

<br>

## 🟢 Opcionais (melhoram a experiência)

| # | Extensão | Buscar por | Para que serve |
|---|----------|------------|----------------|
| 7 | **GitHub Copilot** | `GitHub.copilot` | Assistente de IA para código |
| 8 | **Material Icon Theme** | `PKief.material-icon-theme` | Ícones bonitos para arquivos |
| 9 | **GitLens** | `eamodio.gitlens` | Visualização avançada do Git |
| 10 | **Excel Viewer** | `GrapeCity.gc-excelviewer` | Visualizar CSV/Excel no VS Code |

<br>

### Como instalar cada extensão:

```
1. Clique no ícone de extensões (ou Ctrl+Shift+X)
2. Digite o nome da extensão na barra de busca
3. Clique em "Install" na extensão correta
4. Repita para cada extensão da lista
```

```
┌───────────────────────────────────────────┐
│  🔍  Python                               │
│                                           │
│  ┌─────────────────────────────────────┐  │
│  │ 🐍 Python          Microsoft       │  │
│  │ ⭐⭐⭐⭐⭐  IntelliSense, Linting... │  │
│  │                    [ Install ]      │  │
│  └─────────────────────────────────────┘  │
│                                           │
│  ┌─────────────────────────────────────┐  │
│  │ 📓 Jupyter         Microsoft       │  │
│  │ ⭐⭐⭐⭐⭐  Jupyter notebook support │  │
│  │                    [ Install ]      │  │
│  └─────────────────────────────────────┘  │
└───────────────────────────────────────────┘
```

---

<br>

# 🔧 Etapa 5 – Instalar o Git

<br>

## Windows

```
https://git-scm.com/downloads/win
```

> Baixe e execute o instalador. Pode manter todas as opções padrão.

## macOS

```bash
# Já vem instalado, ou instale via Xcode Command Line Tools:
xcode-select --install

# Ou via Homebrew:
brew install git
```

## Linux

```bash
sudo apt install git
```

### Verificar instalação:

```bash
git --version
```

> Resultado esperado:

```
git version 2.x.x
```

---

<br>

# 📂 Etapa 6 – Clonar o Repositório do Curso

<br>

## 6.1 Escolha uma pasta para o projeto

> Sugestão: crie uma pasta `UNIFOR` na área de trabalho ou em Documentos.

### Windows (PowerShell):

```powershell
cd ~\Documents
mkdir UNIFOR
cd UNIFOR
```

### macOS / Linux (Terminal):

```bash
cd ~/Documents
mkdir UNIFOR
cd UNIFOR
```

<br>

## 6.2 Clone o repositório

```bash
git clone https://github.com/Cassiopo7/mba_ia_unifor_13.git
```

> Resultado esperado:

```
Cloning into 'mba_ia_unifor_13'...
remote: Enumerating objects: ...
remote: Counting objects: 100% ...
Receiving objects: 100% ...
Resolving deltas: 100% ...
done.
```

<br>

## 6.3 Entre na pasta do projeto

```bash
cd mba_ia_unifor_13
```

<br>

## 6.4 Abra o projeto no VS Code

```bash
code .
```

> O VS Code abrirá com todos os arquivos do curso!

```
┌──────────────────────────────────────────────────────┐
│  VS Code                                             │
│  ┌──────────┐  ┌──────────────────────────────────┐  │
│  │ EXPLORER │  │                                  │  │
│  │          │  │  Bem-vindo ao projeto!            │  │
│  │ 📁 datasets    │                                  │  │
│  │ 📁 modulo_1    │  Abra o arquivo:                 │  │
│  │ 📄 Progr...    │  Programacao_Intensiva_...ipynb   │  │
│  │ 📄 docum...    │                                  │  │
│  │ 📄 GUIA_...    │                                  │  │
│  │          │  │                                  │  │
│  └──────────┘  └──────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

---

<br>

# 📚 Etapa 7 – Instalar Bibliotecas Python

Abra o **Terminal integrado** do VS Code:

```
Atalho:  Ctrl + `  (crase)   (Windows/Linux)
         Cmd + `   (crase)   (macOS)
```

Execute os comandos abaixo:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy
```

> ⚠️ No macOS/Linux, pode ser necessário usar `pip3`:

```bash
pip3 install numpy pandas matplotlib seaborn scikit-learn scipy
```

### Verificar se tudo foi instalado:

```bash
python -c "import numpy; import pandas; import matplotlib; import seaborn; import sklearn; print('Tudo instalado com sucesso!')"
```

> Resultado esperado:

```
Tudo instalado com sucesso!
```

---

<br>

# 🧪 Etapa 8 – Testar o Ambiente

<br>

## 8.1 Abra o notebook do curso

No VS Code, abra o arquivo:

```
Programacao_Intensiva_Ciencia_de_Dados.ipynb
```

## 8.2 Selecione o kernel Python

> Ao abrir o notebook, o VS Code pedirá para selecionar um kernel.

```
┌─────────────────────────────────────────────────┐
│  Select Kernel                                  │
│                                                 │
│  ▸ Python 3.12.x    ← Selecione este!          │
│                                                 │
└─────────────────────────────────────────────────┘
```

## 8.3 Execute a primeira célula

> Clique no botão ▶️ ao lado da primeira célula de código, ou use:

```
Atalho:  Shift + Enter   (executa e avança)
         Ctrl + Enter    (executa e permanece)
```

> Se aparecer o resultado `MOstre alguma coisa`, o ambiente está funcionando!

---

<br>

# ⚠️ Problemas Comuns e Soluções

<br>

| Problema | Solução |
|----------|---------|
| `python não é reconhecido como comando` | Reinstale o Python marcando **"Add to PATH"** |
| `pip não é reconhecido` | Use `python -m pip install ...` em vez de `pip install ...` |
| `No module named 'numpy'` | Execute `pip install numpy` no terminal |
| `Kernel not found` no notebook | Instale a extensão **Jupyter** e reinicie o VS Code |
| `git não é reconhecido` | Reinstale o Git e reinicie o terminal |
| `Permission denied` no macOS/Linux | Use `pip3 install --user ...` ou `sudo pip3 install ...` |
| VS Code não abre com `code .` | Abra o VS Code → `Cmd+Shift+P` → "Shell Command: Install 'code' in PATH" |

---

<br>

# 🔄 Como Atualizar o Repositório

Quando houver atualizações no material do curso, execute no terminal:

```bash
cd ~/Documents/UNIFOR/mba_ia_unifor_13
git pull
```

> Isso baixará todas as atualizações feitas pelo instrutor.

---

<br>

# ✅ Checklist Final

Verifique se tudo está funcionando:

```
☐  Python instalado e acessível no terminal
☐  pip funcionando
☐  VS Code instalado
☐  Extensão Python instalada
☐  Extensão Jupyter instalada
☐  Extensão Pylance instalada
☐  Git instalado
☐  Repositório clonado
☐  Bibliotecas instaladas (numpy, pandas, matplotlib, seaborn, scikit-learn, scipy)
☐  Notebook abre e executa no VS Code
```

---

<br>

<div align="center">

### 🎓 Bom curso e boas análises!

**Em caso de dúvidas, procure o instrutor antes ou durante a aula.**

</div>
