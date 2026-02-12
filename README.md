# 📌 API de Integração com Pipefy

API desenvolvida em **FastAPI** para integração com o **Pipefy**, permitindo criar, mover e deletar cards via requisições HTTP.

## 🚀 Tecnologias Utilizadas

* Python 3.12+
* FastAPI
* Pydantic
* Requests
* GraphQL
* Python-dotenv

---

## 📂 Estrutura do Projeto

```
pipefyapi-main/
│
├── controllers/      # Camada de rotas (endpoints)
├── services/         # Regras de negócio
├── clients/          # Integração com API do Pipefy
├── schemas/          # Modelos de dados (Pydantic)
├── enums/            # Enumerações (Cidade e Phase)
│
├── main.py           # Inicialização da aplicação
├── requirements.txt
└── .env
```

---

## ⚙️ Configuração

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/pipefyapi-main.git
cd pipefyapi-main
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```
PIPEFY_URL=https://api.pipefy.com/graphql
PIPEFY_PIPE_ID=SEU_PIPE_ID
PIPEFY_TOKEN=SEU_TOKEN_AQUI
```

---

## ▶️ Executando a aplicação

```bash
python -m uvicorn main:app --reload
```

Acesse a documentação automática:

```
http://localhost:8000/docs
```

---

## 📌 Endpoints Disponíveis

### 🔹 Criar Card

```
POST /card
```

### 🔹 Deletar Card

```
DELETE /card/{card_id}
```

### 🔹 Mover Card de Fase

```
POST /card/{card_id}/move/{phase_id}
```

---

## 🧠 Funcionalidades Implementadas

* Criação de cards no Pipefy via GraphQL
* Movimentação de cards entre fases
* Remoção de cards
* Validação de cidade e fase
* Validação de CPF e telefone
* Uso de variáveis de ambiente para segurança

---

## 🔐 Segurança

Tokens de acesso são armazenados em variáveis de ambiente utilizando `.env` (não versionado).
