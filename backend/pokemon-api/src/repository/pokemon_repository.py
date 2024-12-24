from sqlalchemy.orm import Session
from src.models.pokemon import Pokemon
from sqlalchemy import desc

def get_all_pokemon(db: Session, base_experience=None, height=None, sort_by="name", order="asc", page=1, page_size=10):
    query = db.query(Pokemon)

    if base_experience is not None:
        query = query.filter(Pokemon.base_experience == base_experience)
    if height is not None:
        query = query.filter(Pokemon.height == height)

    if sort_by == "name":
        sort_column = Pokemon.name
    elif sort_by == "base_experience":
        sort_column = Pokemon.base_experience
    else:
        raise ValueError("Invalid sort_by field")

    if order == "asc":
        query = query.order_by(sort_column)
    elif order == "desc":
        query = query.order_by(desc(sort_column))
    else:
        raise ValueError("Invalid order field")

    total_items = query.count()
    pokemons = query.offset((page - 1) * page_size).limit(page_size).all()

    return {
        "total_items": total_items,
        "page": page,
        "page_size": page_size,
        "data": pokemons,
    }
