# WorkoutAPI

API para gerenciar uma competição de crossfit. Projeto desenvolvido com FastAPI, SQLAlchemy, Alembic, Pydantic, PostgreSQL e Docker.

## Descrição

Esta API permite criar, consultar, atualizar e excluir atletas, categorias e centros de treinamento. A modelagem segue uma estrutura simples para fins didáticos.

## Requisitos

* Python 3.11.4
* Docker e Docker Compose
* Pyenv (opcional)

## Instalação do ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/workoutapi.git
   cd workoutapi
   ```

2. Crie o ambiente virtual com pyenv ou venv:

   ```bash
   pyenv virtualenv 3.11.4 workoutapi
   pyenv activate workoutapi

   # ou com venv:
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração do banco de dados

1. Suba o banco de dados com Docker:

   ```bash
   docker-compose up -d
   ```

2. Crie as migrations iniciais:

   ```bash
   alembic revision --autogenerate -m "initial"
   alembic upgrade head
   ```

## Executar a API

1. Inicie o servidor FastAPI:

   ```bash
   uvicorn main:app --reload
   ```

2. Acesse a documentação interativa:

   ```
   http://127.0.0.1:8000/docs
   ```

## Funcionalidades

* Endpoints para atletas: criar, consultar, atualizar, excluir
* Endpoints para categorias: criar, consultar
* Endpoints para centros de treinamento: criar, consultar
* Integração com banco de dados PostgreSQL usando SQLAlchemy
* Migrations gerenciadas pelo Alembic
* Validação de dados com Pydantic

## Desafios extras

* Adicionar query parameters para filtrar atletas por nome ou CPF
* Personalizar as respostas para incluir categoria e centro de treinamento
* Tratar erros de integridade de dados, como CPF duplicado
* Implementar paginação com fastapi-pagination (limit e offset)
