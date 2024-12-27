from fastapi import APIRouter
from src.controller.pokemon_controller import router as pokemon_controller

router = APIRouter()
router.include_router(pokemon_controller, tags=["pokemon"])