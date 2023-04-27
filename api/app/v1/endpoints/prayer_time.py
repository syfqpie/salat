from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.operations.prayer_time import crud, schemas


router = APIRouter()


@router.get("/zones/", response_model=list[schemas.Zone])
def read_zones(db: Session = Depends(get_db), state: str | None = None):
    if state:
        return crud.get_zones_by_state(db, state)

    return crud.get_zones(db)


@router.get("/prayer-times/", response_model=list[schemas.PrayerTime])
def read_prayer_times(
    db: Session = Depends(get_db), zone: str = None, weekly: bool = False
):
    if not zone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Zone is required"
        )

    return crud.get_prayer_times_by_zone(db, zone, weekly)
