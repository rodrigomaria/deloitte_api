# Deloitte API

## Used Technologies:
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [OpenAPI](https://swagger.io/specification/)
- [MySQL](https://www.mysql.com/)
- [Black code formatter](https://black.readthedocs.io/en/stable/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Isort](https://readthedocs.org/projects/isort/)
- [Bandit SAST](https://bandit.readthedocs.io/en/latest/)
- [Safety](https://pyup.io/safety/)

## Getting Started:
### Setup:

* Build this project's containers: `make build`

* Run DB and fixtures using: `make init`

* Run the application using: `make run`

* The server should be listening on `http://localhost:9999`

* For showing the application logs, run `make logs`

---

### Tests:

* Integration tests (through behave BDD): `make test integration`

You can run using: `make test`

The tests are located under `tests` path.

---

### Linters:
deloitte-api has three code linters:

* [Black code formatter](https://black.readthedocs.io/en/stable/)
* [Flake8](https://flake8.pycqa.org/en/latest/)
* [Isort](https://readthedocs.org/projects/isort/)

To run them, just use the command: `make lint`

---

### Security
deloitte-api uses two libraries in order to find potencial security breaches:

* [Bandit SAST](https://bandit.readthedocs.io/en/latest/): `make lint`
* [Safety](https://pyup.io/safety/): `make audit`

---

## Interfaces

### Admin:
- Accessed by the `/deloitte/api/admin` endpoint, using username `root` and password `root`;

### REST:
- It's self-documented in the root endpoint, accessed by the `http://localhost:9999`;

---
## Checklist
### REQUISITOS MÍNIMOS BACK-END
1. Todos os códigos deverão estar em um repositório no Github com README.md descrevendo tecnologias utilizadas no projeto. ✔️
2. API:

    a. CRUD (Criar, ler, atualizar e deletar) de Serviços ✔️

    b. CRUD (Criar, ler, atualizar e deletar) de Posts ✔️

    c. CRUD (Criar, ler, atualizar e deletar) de Integrantes da Equipe ✔️
3. Banco de dados:

    a. Utilizar banco de dados relacional ✔️

    b. Adicionar dados para teste ✔️
### OPCIONAIS BACK-END
4. Autenticação de administrador para gerenciamento do conteúdo ✔️
5. Documentação da API ✔️
6. Testes automatizados ✖️
7. Deploy da aplicação ✖️

---