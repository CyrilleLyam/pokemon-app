from fastapi import Depends, APIRouter, Query
from sqlalchemy.orm import Session
from src.service.pokemon_service import get_all
from src.database import get_db

router = APIRouter()

@router.get("/")
def get_all_pokemon(
    base_experience: int = Query(None),
    height: int = Query(None),
    sort_by: str = Query("name"),
    order: str = Query("asc"),
    page: int = Query(1),
    page_size: int = Query(10),
    db: Session = Depends(get_db),
):
    return get_all(
        db=db,
        base_experience=base_experience,
        height=height,
        sort_by=sort_by,
        order=order,
        page=page,
        page_size=page_size,
    )