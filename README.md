# API de Gestão de Empresas e Obrigações Acessórias

Uma API simples desenvolvida com **FastAPI**, **SQLAlchemy** e **PostgreSQL** para cadastrar **empresas** e gerenciar suas **obrigações acessórias**. Ideal para testes de integração, manipulação de dados fiscais e obrigações tributárias de empresas.

## Funcionalidades

- **Cadastro de Empresas**: Permite o registro de empresas com informações como nome, CNPJ, endereço, e dados de contato.
- **Gestão de Obrigações Acessórias**: Permite cadastrar as obrigações que uma empresa deve declarar para o governo, com informações sobre periodicidade (mensal, trimestral, anual) e o vínculo com a empresa.

## Tecnologias

- **FastAPI**: Framework moderno e rápido para construção de APIs com Python.
- **SQLAlchemy**: ORM para interagir com o banco de dados PostgreSQL.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados.
- **Pydantic**: Para validação e criação de schemas.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/Ribashow666/fast-api.git
   cd fast-api
