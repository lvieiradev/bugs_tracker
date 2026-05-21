<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />

<br/><br/>

# 🐛 Bugs Tracker

**Sistema web para registro e acompanhamento de bugs — desenvolvido com Flask e MySQL.**

Permite que membros da empresa júnior reportem problemas encontrados no site, com suporte a categorização, upload de imagens e painel administrativo para gestão de status.

<br/>

[![MIT License](https://img.shields.io/badge/Licença-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=flat-square)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)]()

</div>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Usar](#-como-usar)
- [Licença](#-licença)

---

## 💡 Sobre o Projeto

O **Bugs Tracker** nasceu da necessidade de centralizar o reporte de problemas encontrados no site de uma empresa júnior. Antes de existir essa ferramenta, os bugs eram comunicados de forma descentralizada por mensagens, e-mails ou até verbalmente o que dificultava o rastreamento e a resolução.

Com esse sistema, qualquer membro pode registrar um bug com título, categoria, descrição, data de ocorrência e uma imagem de evidência. A equipe técnica, por sua vez, acessa o painel administrativo para visualizar e atualizar o status de cada ocorrência.

---

## ✨ Funcionalidades

- ✅ **Registro de bugs** com título, categoria, descrição e data
- 🖼️ **Upload de imagem** como evidência do problema (PNG, JPG, JPEG, GIF — máx. 5 MB)
- 🔍 **Verificação de duplicatas** — o sistema impede o reporte do mesmo bug duas vezes
- 📋 **Listagem pública** de todos os bugs reportados com seus status
- 🔧 **Painel administrativo** para visualização e atualização de status
- 🔄 **Controle de status** dos bugs (ex: aberto, em andamento, resolvido)

---

## 🛠 Tecnologias

| Camada | Tecnologia |
|---|---|
| Back-end | Python 3 + Flask 3.1 |
| Banco de Dados | MySQL + Flask-MySQLdb |
| Front-end | HTML5 + Jinja2 |
| Upload de Arquivos | Werkzeug |
| Variáveis de Ambiente | python-dotenv |

---

## 📦 Pré-requisitos

Antes de começar, você vai precisar ter instalado:

- [Python 3.10+](https://www.python.org/)
- [MySQL](https://www.mysql.com/)
- [Git](https://git-scm.com/)

---

## 🚀 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/lvieiradev/bugs_tracker.git
cd bugs_tracker
```

### 2. Crie e ative um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no exemplo abaixo:

```env
MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DB
```

### 5. Configure o banco de dados

Acesse o MySQL e crie o banco e a tabela:

```sql
CREATE DATABASE bugs_tracker;
USE bugs_tracker;

CREATE TABLE bugs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    data_problema DATE NOT NULL,
    imagem VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Aberto',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 6. Execute a aplicação

```bash
python app.py
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 📁 Estrutura do Projeto

```
bugs_tracker/
│
├── static/
│   └── uploads/          # Imagens enviadas pelos usuários
│
├── templates/
│   ├── index.html         # Página pública de reporte e listagem
│   └── admin.html         # Painel administrativo
│
├── app.py                 # Aplicação principal (rotas e lógica)
├── requirements.txt       # Dependências do projeto
├── .env                   # Variáveis de ambiente (não versionar)
├── .gitignore
└── LICENSE
```

---

## 📖 Como Usar

### Página Principal — `/`

Qualquer usuário pode acessar a página principal para:

- **Reportar um bug** preenchendo o formulário com título, categoria, descrição, data e imagem opcional
- **Visualizar a lista** de todos os bugs já registrados e seus status atuais

### Painel Administrativo — `/admin`

A equipe técnica acessa `/admin` para:

- Visualizar todos os bugs registrados em detalhe
- **Atualizar o status** de cada bug clicando nas opções disponíveis

> ⚠️ O painel admin não possui autenticação nesta versão. Recomenda-se adicionar login antes de um deploy em produção.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

<div align="center">
  Desenvolvido por <a href="https://github.com/lvieiradev">lvieiradev</a>
</div>
