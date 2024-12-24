from src.repository.pokemon_repository import get_all_pokemon
from sqlalchemy.orm import Session

def get_all(db: Session, base_experience=None, height=None, sort_by="name", order="asc", page=1, page_size=10):
    return get_all_pokemon(db, base_experience, height, sort_by, order, page, page_size)