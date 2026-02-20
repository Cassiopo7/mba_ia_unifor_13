# 🚀 Guia Passo a Passo: Colaboração com Git e GitHub

Este guia demonstra como trabalhar colaborativamente em um projeto usando Git e GitHub. Vamos simular um cenário onde o professor cria um repositório e um aluno faz alterações e contribui com o projeto.

---

## 📋 Índice

1. [Parte 1: Professor - Criar e Subir o Projeto](#parte-1-professor---criar-e-subir-o-projeto)
2. [Parte 2: Aluno - Baixar e Modificar o Projeto](#parte-2-aluno---baixar-e-modificar-o-projeto)
3. [Parte 3: Professor - Buscar Atualizações](#parte-3-professor---buscar-atualizações)

---

## Parte 1: Professor - Criar e Subir o Projeto

### Passo 1.1: Verificar se o Git está instalado

Abra o terminal e verifique se o Git está instalado:

```bash
git --version
```

Se não estiver instalado, baixe em: https://git-scm.com/downloads

### Passo 1.2: Configurar o Git (apenas na primeira vez)

Configure seu nome e email (substitua pelos seus dados):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### Passo 1.3: Navegar até a pasta do projeto

```bash
cd "/Users/cassiopinheiro/Documents/UNIFOR/Programacao Ciencia de Dados/chamada"
```

### Passo 1.4: Inicializar o repositório Git

```bash
git init
```

Isso cria uma pasta `.git` oculta na pasta do projeto.

### Passo 1.5: Criar arquivo .gitignore (opcional, mas recomendado)

Crie um arquivo `.gitignore` para não subir arquivos desnecessários:

```bash
cat > .gitignore << EOF
# Arquivos do sistema
.DS_Store
__pycache__/
*.pyc
*.pyo

# Jupyter Notebook
.ipynb_checkpoints/

# Ambientes virtuais
venv/
env/
.venv/

# Arquivos de configuração local
config.py
*.key
*.pem

# Logs
*.log
EOF
```

### Passo 1.6: Adicionar arquivos ao Git

Adicione todos os arquivos do projeto:

```bash
git add .
```

Para ver quais arquivos foram adicionados:

```bash
git status
```

### Passo 1.7: Fazer o primeiro commit

```bash
git commit -m "Commit inicial: Sistema de Chamada Interativo"
```

### Passo 1.8: Criar repositório no GitHub

1. Acesse https://github.com
2. Faça login na sua conta
3. Clique no botão **"+"** no canto superior direito
4. Selecione **"New repository"**
5. Preencha:
   - **Repository name**: `sistema-chamada-interativo` (ou outro nome)
   - **Description**: "Sistema de Chamada Interativo - Disciplina C028"
   - **Visibility**: Escolha **Public** (para facilitar a demonstração) ou **Private**
   - **NÃO marque** "Initialize this repository with a README"
6. Clique em **"Create repository"**

### Passo 1.9: Conectar o repositório local ao GitHub

Após criar o repositório no GitHub, você verá instruções. Execute os comandos abaixo (substitua `SEU_USUARIO` pelo seu usuário do GitHub):

```bash
git remote add origin https://github.com/SEU_USUARIO/sistema-chamada-interativo.git
git branch -M main
git push -u origin main
```

Se solicitado, faça login com suas credenciais do GitHub.

**Pronto!** O projeto está no GitHub e pode ser acessado por qualquer pessoa com o link.

---

## Parte 2: Aluno - Baixar e Modificar o Projeto

### Passo 2.1: Obter o link do repositório

O professor deve compartilhar o link do repositório GitHub. Exemplo:
```
https://github.com/SEU_USUARIO/sistema-chamada-interativo
```

### Passo 2.2: Clonar o repositório

O aluno abre o terminal e executa (substitua pelo link real):

```bash
cd ~/Documents  # ou qualquer pasta onde quer salvar o projeto
git clone https://github.com/SEU_USUARIO/sistema-chamada-interativo.git
```

Isso cria uma pasta `sistema-chamada-interativo` com todos os arquivos do projeto.

### Passo 2.3: Entrar na pasta do projeto

```bash
cd sistema-chamada-interativo
```

### Passo 2.4: Verificar o status do repositório

```bash
git status
```

Deve mostrar "nothing to commit, working tree clean" (nada para commitar, árvore de trabalho limpa).

### Passo 2.5: Fazer uma alteração

Agora o aluno vai fazer uma alteração simples. Por exemplo, criar um arquivo de teste ou modificar um arquivo existente.

**Exemplo 1: Criar um novo arquivo**

```bash
echo "# Contribuição do Aluno" > contribuicao_aluno.md
```

**Exemplo 2: Adicionar uma linha em um arquivo existente**

```bash
echo "\n\n## Atualização feita pelo aluno em $(date)" >> README.md
```

**Exemplo 3: Adicionar um novo aluno no dicionário** (específico para o projeto de chamada)

O aluno pode abrir o arquivo `notebook_chamada.ipynb` e adicionar uma nova entrada no dicionário de alunos, ou criar um arquivo de texto com sugestões.

Ou o aluno pode abrir um arquivo no editor e fazer alterações manualmente.

### Passo 2.6: Verificar as alterações

```bash
git status
```

Deve mostrar os arquivos modificados ou criados em vermelho.

Para ver exatamente o que foi alterado:

```bash
git diff
```

### Passo 2.7: Adicionar as alterações ao Git

```bash
git add .
```

Ou para adicionar arquivos específicos:

```bash
git add contribuicao_aluno.md
```

### Passo 2.8: Fazer commit das alterações

```bash
git commit -m "Adiciona contribuição do aluno: arquivo de teste"
```

**Importante**: Use mensagens de commit descritivas e claras!

### Passo 2.9: Enviar alterações para o GitHub

```bash
git push origin main
```

Se for a primeira vez, o GitHub pode pedir autenticação. O aluno precisará:
- Ter uma conta no GitHub
- Fazer login quando solicitado

**Pronto!** As alterações do aluno estão no GitHub.

---

## Parte 3: Professor - Buscar Atualizações

### Passo 3.1: Verificar se há atualizações no GitHub

Antes de buscar, é bom verificar se há mudanças:

```bash
git fetch origin
```

Isso baixa informações sobre mudanças sem aplicar ainda.

### Passo 3.2: Ver o que mudou

Para ver commits que estão no GitHub mas não no seu repositório local:

```bash
git log HEAD..origin/main
```

### Passo 3.3: Buscar e aplicar as atualizações

```bash
git pull origin main
```

Este comando:
- Busca as alterações do GitHub (`fetch`)
- Aplica as alterações no seu repositório local (`merge`)

### Passo 3.4: Verificar as alterações recebidas

```bash
git log --oneline -5
```

Mostra os últimos 5 commits, incluindo o do aluno.

Para ver o conteúdo das alterações:

```bash
ls -la  # lista arquivos, incluindo os novos
cat contribuicao_aluno.md  # se o aluno criou este arquivo
```

**Pronto!** O professor agora tem as atualizações do aluno no seu repositório local.

---

## 🔄 Fluxo Completo Resumido

```
┌─────────────────┐
│   PROFESSOR     │
│                 │
│ 1. git init     │
│ 2. git add .    │
│ 3. git commit   │
│ 4. git push     │
└────────┬────────┘
         │
         │ (cria repositório no GitHub)
         │
         ▼
┌─────────────────┐
│     GITHUB      │
│   (nuvem)       │
└────────┬────────┘
         │
         │ (aluno clona)
         │
         ▼
┌─────────────────┐
│     ALUNO       │
│                 │
│ 1. git clone    │
│ 2. (faz alter.) │
│ 3. git add .    │
│ 4. git commit   │
│ 5. git push     │
└────────┬────────┘
         │
         │ (envia para GitHub)
         │
         ▼
┌─────────────────┐
│     GITHUB      │
│   (atualizado)  │
└────────┬────────┘
         │
         │ (professor busca)
         │
         ▼
┌─────────────────┐
│   PROFESSOR     │
│                 │
│ git pull        │
│ (recebe alter.) │
└─────────────────┘
```

---

## 📚 Comandos Git Essenciais

### Comandos Básicos

| Comando | Descrição |
|---------|-----------|
| `git init` | Inicializa um repositório Git |
| `git status` | Mostra o status dos arquivos |
| `git add .` | Adiciona todos os arquivos modificados |
| `git commit -m "mensagem"` | Salva as alterações com uma mensagem |
| `git push` | Envia alterações para o GitHub |
| `git pull` | Busca e aplica alterações do GitHub |
| `git clone URL` | Baixa um repositório do GitHub |
| `git log` | Mostra histórico de commits |
| `git diff` | Mostra diferenças entre arquivos |

### Comandos Úteis para Depuração

```bash
# Ver histórico resumido
git log --oneline --graph

# Ver alterações em um arquivo específico
git diff arquivo.txt

# Desfazer alterações não commitadas
git restore arquivo.txt

# Ver configuração atual
git config --list
```

---

## ⚠️ Dicas Importantes

1. **Sempre faça `git status` antes de commitar** para ver o que será salvo
2. **Use mensagens de commit descritivas**: "Corrige bug" é melhor que "mudanças"
3. **Faça commits frequentes**: pequenos commits são melhores que um grande
4. **Antes de fazer `push`, sempre faça `pull`** para garantir que está atualizado
5. **Se houver conflitos**, o Git avisará. Resolva manualmente e depois faça commit

---

## 🎓 Exercício Prático Sugerido

1. **Professor**: Crie um arquivo `participantes.md` com uma lista vazia
2. **Aluno**: Adicione seu nome na lista e faça commit
3. **Professor**: Faça pull e veja o nome do aluno aparecer
4. **Repita** com outros alunos para demonstrar colaboração em equipe

**Alternativa específica para o projeto de chamada:**
1. **Professor**: Crie um arquivo `sugestoes_melhoria.md` vazio
2. **Aluno**: Adicione uma sugestão de melhoria para o sistema de chamada
3. **Professor**: Faça pull e veja a sugestão do aluno

---

## 📖 Recursos Adicionais

- Documentação oficial do Git: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

## ✅ Checklist para Demonstração

### Professor
- [ ] Git instalado e configurado
- [ ] Repositório inicializado na pasta `chamada/`
- [ ] Projeto commitado
- [ ] Repositório criado no GitHub
- [ ] Projeto enviado para GitHub (`push`)
- [ ] Link do repositório compartilhado com aluno

### Aluno
- [ ] Git instalado
- [ ] Repositório clonado
- [ ] Alteração feita
- [ ] Alteração commitada
- [ ] Alteração enviada para GitHub (`push`)

### Professor (buscar atualizações)
- [ ] `git pull` executado
- [ ] Alterações do aluno recebidas
- [ ] Alterações verificadas

---

**Boa demonstração! 🎉**

