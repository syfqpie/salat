from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.operations.prayer_time import crud, schemas


router = APIRouter()


@router.get("/zones/", response_model=list[schemas.Zone])
def read_zones(db: Session = Depends(get_db), state: str | None = None):
    if state:
        return crud.get_zones_by_state(db, state)
    
    return crud.get_zones(db)
