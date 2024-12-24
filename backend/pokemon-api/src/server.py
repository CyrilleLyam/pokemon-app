from fastapi import FastAPI
from src.routes.pokemon_route import router as pokemon_routes
from src.models.pokemon import Base
from src.exceptions.base import add_global_exception_handlers
from src.database import engine

app = FastAPI()
add_global_exception_handlers(app)

Base.metadata.create_all(bind=engine)

app.include_router(pokemon_routes)