# Projeto Me Poupe

## Descrição do Projeto

O **Me Poupe** é um sistema web desenvolvido para auxiliar no **controle de despesas pessoais**, permitindo que os usuários registrem, visualizem e analisem seus gastos mensais.

O sistema permite cadastrar despesas, organizá-las por categorias e visualizar relatórios que ajudam o usuário a entender melhor para onde seu dinheiro está indo.

O projeto foi desenvolvido utilizando **Python** com o framework **Django**, além de tecnologias web como HTML, CSS e JavaScript.

---

# Objetivo do Projeto

O objetivo do projeto é oferecer uma ferramenta simples para ajudar pessoas a:

* Registrar suas despesas diárias
* Organizar gastos por categoria
* Visualizar relatórios de gastos
* Melhorar o controle financeiro pessoal

Com isso, o sistema ajuda o usuário a ter **maior consciência sobre seus hábitos financeiros**.

---

# Problema que o Projeto Resolve

Muitas pessoas têm dificuldade em controlar suas finanças pessoais porque:

* Não registram seus gastos
* Não sabem para onde o dinheiro está indo
* Não possuem organização financeira
* Não conseguem visualizar seus gastos de forma clara

O **Me Poupe** resolve esse problema oferecendo um sistema simples que permite:

* cadastrar despesas
* organizar gastos
* visualizar relatórios e gráficos
* acompanhar os gastos mensais

---

# Tecnologias Utilizadas

* Python
* **Django**
* HTML
* CSS
* JavaScript
* **python-dotenv**
* SQLite (banco de dados padrão do Django)
* **Git**
* **GitHub**

---

# Arquivos Ignorados pelo Git

Alguns arquivos **não são enviados para o repositório** por motivos de segurança ou porque são específicos de cada computador.

Esses arquivos são definidos no `.gitignore`.

Arquivos ignorados importantes:

* `venv/` → ambiente virtual
* `.env` → variáveis de ambiente
* `db.sqlite3` → banco de dados local
* `__pycache__/` → cache do Python

Por esse motivo, algumas configurações precisam ser recriadas quando o projeto for executado em outro computador.

---

# Configuração das Variáveis de Ambiente

O projeto utiliza **variáveis de ambiente** através da biblioteca **python-dotenv**.

Crie um arquivo chamado `.env` na raiz do projeto.

Exemplo:

```env
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

Essas variáveis são carregadas automaticamente pelo Django.

---

# Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto em qualquer computador.

---

# 1 Clonar o repositório

```bash
git clone https://github.com/seu-usuario/bora-poupar.git
```

Depois entre na pasta do projeto:

```bash
cd bora-poupar/django
```

---

# Criar o ambiente virtual

Crie um ambiente virtual para instalar as dependências do projeto:

```bash
python3 -m venv venv
```

---

# Ativar o ambiente virtual

### Linux ou Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Se ativado corretamente aparecerá:

```
(venv)
```

no início do terminal.

---

# Instalar as dependências

Instale todas as bibliotecas necessárias para rodar o projeto:

```bash
pip install -r requirements.txt
```

Caso não exista o arquivo `requirements.txt`, instale manualmente:

```bash
pip install django
pip install python-dotenv
```

---

# Criar o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

---

# Executar as migrações do banco de dados

O banco de dados **não está no repositório**, portanto precisa ser criado automaticamente.

Execute:

```bash
python manage.py migrate
```

Isso criará o arquivo `db.sqlite3` com todas as tabelas do sistema.

---

# Rodar o servidor do projeto

Execute o comando abaixo:

```bash
python manage.py runserver
```

Se tudo estiver correto aparecerá:

```
Starting development server at
http://127.0.0.1:8000/
```

---

# Acessar o sistema

Abra o navegador e acesse:

```
http://127.0.0.1:8000
```

---

# Glossário

**Despesa**
Registro de um gasto realizado pelo usuário.

**Categoria**
Classificação usada para organizar despesas (ex: Fixa, Variavel, Essencial...).

**Relatório**
Visualização resumida dos gastos cadastrados por categoria.

**Ambiente Virtual**
Ambiente isolado utilizado para instalar as dependências do projeto sem afetar o Python do sistema.

---

# Autor

Projeto desenvolvido por **Eliseu dos Santos Cosme**.

---
