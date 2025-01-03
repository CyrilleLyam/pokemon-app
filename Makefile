POD_SERVICES=pod-services
FETCHER=data-fetcher
BACKEND=backend
NETWORK=pokemon-network

.PHONY: ensure-network up-postgresql up-pokemon-sync up-backend up-nginx down

ensure-network:
	@echo "🔍 Checking if network '$(NETWORK)' exists..."
	@if ! docker network inspect $(NETWORK) >/dev/null 2>&1; then \
		echo "🌐 Creating network '$(NETWORK)'..."; \
		docker network create $(NETWORK); \
	fi

up-postgresql: ensure-network
	@echo "🚀 Starting PostgreSQL service..."
	@docker compose -f $(POD_SERVICES)/postgres/docker-compose.yml up -d
	@echo "✅ PostgreSQL is up and running!"

up-pokemon-sync: up-postgresql
	@echo "🚀 Starting fetcher services (e.g., pokemon-sync)..."
	@docker compose -f $(FETCHER)/pokemon-sync-service/docker-compose.yml up -d
	@echo "✅ Fetcher services are up and running!"

up-backend: up-pokemon-sync
	@echo "🚀 Starting backend services..."
	@find $(BACKEND) -type f -name docker-compose.yml -exec docker compose -f {} up -d \;
	@echo "✅ Backend services are up and running!"

up: up-backend
	@echo "🚀 Starting NGINX service..."
	@docker compose -f $(POD_SERVICES)/nginx/docker-compose.yml up -d
	@echo "✅ NGINX service is up and running!"

down:
	@echo "🛑 Stopping all services..."
	@docker compose -f $(POD_SERVICES)/postgres/docker-compose.yml down
	@docker compose -f $(FETCHER)/pokemon-sync-service/docker-compose.yml down
	@find $(BACKEND) -type f -name docker-compose.yml -exec docker compose -f {} down \;
	@docker compose -f $(POD_SERVICES)/nginx/docker-compose.yml down
	@echo "✅ All services have been stopped!"
