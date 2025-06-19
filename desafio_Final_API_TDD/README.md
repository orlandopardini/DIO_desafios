# StoreAPI

Esta aplicação é uma API desenvolvida com FastAPI, usando TDD com Pytest. Utiliza MongoDB como banco de dados e demonstra testes em nível de Schema, Use Cases e Controllers.

## Resumo do projeto

API criada com foco educacional para praticar o desenvolvimento orientado a testes (TDD). Contém exemplos de testes automatizados, arquitetura modular e uso de FastAPI com Pytest.

## Objetivo

Demonstrar como criar uma API usando FastAPI e MongoDB, validando dados com Pydantic e garantindo qualidade do código através de testes automatizados com Pytest.

## O que é

* Aplicação com fins educativos
* Serve como base para estudar TDD, FastAPI e Pytest
* CRUD básico de produtos

## O que não é

* Aplicação para produção
* Integração com sistemas externos

## Arquitetura

* Usuário faz chamadas HTTP para a Store API
* Store API processa as requisições e se comunica com o MongoDB para leitura e escrita
* Diagrama de sequência disponível no repositório

## Estrutura do banco de dados (MongoDB)

Coleção **Product** com os campos:

* id
* name
* quantity
* price
* status

## Endpoints principais

* **POST /products** : cria um produto
* **GET /products** : lista produtos
* **GET /products/{id}** : consulta um produto por ID
* **DELETE /products/{id}** : exclui um produto

## Desafios propostos

* Mapear exceções de erros de inserção e tratar na controller
* Melhorar o método PATCH para retornar 404 quando o produto não existir
* Permitir alteração da data `updated_at` quando um campo for atualizado
* Adicionar filtro de faixa de preço (ex: preço > 5000 e preço < 8000)

## Preparar ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/storeapi.git
   cd storeapi
   ```

2. Crie o ambiente virtual com **pyenv** ou **Poetry**:

   ```bash
   pyenv virtualenv 3.11.4 storeapi
   pyenv activate storeapi

   # ou com poetry:
   poetry install
   ```

3. Configure o banco MongoDB local ou via Docker, conforme necessidade.

## Executar a API

```bash
uvicorn main:app --reload
```

Acesse:

```
http://127.0.0.1:8000/docs
```

## Rodar os testes

```bash
pytest
```
