.PHONY: d-run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
	COMPOSE_PROFILES=full_dev \
	docker-compose up --build

.PHONY: d-run-i-db
d-run-i-db:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build postgres

.PHONY: d-run-i-local-dev
d-run-i-local-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
	COMPOSE_PROFILES=local_dev \
	docker-compose up --build

.PHONY: d-run-i-extended
d-run-i-extended:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --timeout 0 && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
	COMPOSE_PROFILES=full_dev \
	docker-compose up --build --detach && \
	make d-logs-follow

.PHONY: d-logs-follow
d-logs-follow:
	@docker-compose logs --follow

.PHONY: d-stop
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down

.PHONY: d-purge
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: migrate
migrate:
	@python manage.py migrate

.PHONY: migrations
migrations:
	@python manage.py makemigrations

.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input

.PHONY: until-i-kill-by-port
until-i-kill-by-port:
	@sudo lsof -i:8001 -Fp | head -n 1 | sed 's/^p//' | xargs sudo kill

.PHONY: init-configs-i-dev
init-configs-i-dev:
	@cp docker-compose.override.dev.yml docker-compose.override.yml && \
	cp .env.dev .env

.PHONY: init-dev
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files


.PHONY: d-homework-i-run
d-homework-i-run:
	@make init-configs-i-dev && \
	make d-run

.PHONY: d-homework-i-purge
d-homework-i-purge:
	@make d-purge