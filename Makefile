ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(ARGS):;@:)
EXEC = docker-compose exec deloitte-api
RUN = docker-compose exec deloitte-api sh
$(eval TEST_TYPE := $(shell [[ -z "$(ARGS)" ]] && echo "null" || echo "$(ARGS)"))

# HELP COMMANDS
help: ## show this help
	@echo 'usage: make [target] [option]'
	@echo ''
	@echo 'Common sequence of commands:'
	@echo '- make build'
	@echo '- make init'
	@echo '- make test'
	@echo '- make run'
	@echo '- make stop'
	@echo '- make lint'
	@echo '- make audit'
	@echo '- make migrate'
	@echo '- make migrations'
	@echo '- make collectstatic'
	@echo '- make sh'
	@echo '- make db_initialize'
	@echo '- make load_initial_data'
	@echo '- make logs'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

.PHONY : build
build: ## build application containers
ifeq ($(ARGS), nocache)
	@ docker-compose build --no-cache deloitte-api
else
	@ docker-compose build deloitte-api
endif

.PHONY: init
init: run ## Initialize application's DB and fixtures
	@ make db_initialize
	@ make migrations
	@ make migrate
	@ make collectstatic
	@ make load_initial_data

.PHONY : test
test: ## run the application tests
	@ $(EXEC) coverage run --rcfile=.coveragerc_behave manage.py behave --no-capture

.PHONY : run
run: ## start the application
	@ docker-compose up -d

.PHONY : run
stop: ## stop the application
	@ docker-compose down

.PHONY: lint
lint: ## runs linters over the code
	@ $(EXEC) /bin/sh -c "isort . && black . && flake8 . && bandit -r . -c .bandit-config.yml"

.PHONY: audit
audit: run ## run package auditor
	@ $(EXEC) safety check --full-report

.PHONY: migrate
migrate: run ## run pending migrations
	@ $(EXEC) python manage.py migrate

.PHONY: migrations
migrations: run ## create new migrations
	@ $(EXEC) python manage.py makemigrations

.PHONY: collectstatic
collectstatic: run ## create admin static files
	@ $(EXEC) python manage.py collectstatic --no-input

.PHONY: sh
sh: run ## runs pure shell on application container
	@ $(EXEC) sh

.PHONY: db_initialize
db_initialize: ## initialize the database
	@ docker ps | grep percona || docker restart deloitte-database
	@ sleep 20
	## create db deloitte_api
	@ docker exec deloitte-database mysql -u root -e "CREATE DATABASE IF NOT EXISTS deloitte_api;"
	## create root user db
	@ docker exec deloitte-database mysql -u root -e "CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'root';"
	## grant all privileges root user
	@ docker exec deloitte-database mysql -u root -e "GRANT ALL PRIVILEGES ON deloitte_api.* TO 'root'@'%';"

.PHONY: load_initial_data
load_initial_data: ## load initial data
	@ $(RUN) -c "source scripts/create_initial_data.sh"

.PHONY: logs
logs: ## show the logs on terminal
	@ docker logs -f deloitte-api
