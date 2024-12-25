POSTGRES_DIR=pod-services/postgres
BACKEND_DIR=backend/**

# Default target
.PHONY: all
all: help

# Ensure the external network exists
ensure-network:
	@echo "Ensuring external network pokemon-network exists..."
	@sudo docker network inspect pokemon-network >/dev/null 2>&1 || sudo docker network create pokemon-network

# Run Docker Compose up for all services
up: ensure-network
	@echo "Starting all Docker services..."
	@sudo docker compose -f $(POSTGRES_DIR)/docker-compose.yml up -d
	@find $(BACKEND_DIR) -name docker-compose.yml -exec sudo docker compose -f {} up -d \;

# Stop Docker Compose services for all
down:
	@echo "Stopping all Docker services..."
	@sudo docker compose -f $(POSTGRES_DIR)/docker-compose.yml down
	@find $(BACKEND_DIR) -name docker-compose.yml -exec sudo docker compose -f {} down \;

# View Docker Compose logs for all
logs:
	@echo "Showing logs for all Docker services..."
	@sudo docker compose -f $(POSTGRES_DIR)/docker-compose.yml logs
	@find $(BACKEND_DIR) -name docker-compose.yml -exec sudo docker compose -f {} logs \;

# Restart all Docker Compose services
restart: down up

# Display help message
.PHONY: help
help:
	@echo "Makefile for managing Docker Compose for all services:"
	@echo "  make up       Start all Docker containers."
	@echo "  make down     Stop all Docker containers."
	@echo "  make logs     View logs for all Docker containers."
	@echo "  make restart  Restart all Docker containers."
