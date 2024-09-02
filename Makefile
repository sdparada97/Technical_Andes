.PHONY: build up down migrate make-migrations

# Variables
DOCKER_COMPOSE = sudo docker compose

build-local:
	$(DOCKER_COMPOSE) --env-file .env.dev build --no-cache

up-local:
	$(DOCKER_COMPOSE) --env-file .env.dev up -d

down-local:
	$(DOCKER_COMPOSE) --env-file .env.dev down

clear:
	docker system prune -a
