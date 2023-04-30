from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status, Query

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.operations.prayer_time import crud, schemas, docs

router = APIRouter()


@router.get(
    "/zones/", response_model=list[schemas.Zone], openapi_extra=docs.ZONES_EXTRA
)
def read_zones(
    db: Session = Depends(get_db),
    state: Annotated[str | None, Query(**docs.ZONES_PARAMETERS["state"])] = None,
):
    if state:
        return crud.get_zones_by_state(db, state)

    return crud.get_zones(db)


@router.get(
    "/prayer-times/",
    response_model=list[schemas.PrayerTime],
    openapi_extra=docs.PRAYER_TIMES_EXTRA,
)
def read_prayer_times(
    db: Session = Depends(get_db),
    zone: Annotated[str | None, Query(**docs.PRAYER_TIMES_PARAMETERS["zone"])] = None,
    weekly: Annotated[bool, Query(**docs.PRAYER_TIMES_PARAMETERS["weekly"])] = False,
):
    if not zone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Zone is required"
        )

    return crud.get_prayer_times_by_zone(db, zone, weekly)


@router.get(
    "/sync-monthly", response_model=schemas.SyncBase, openapi_extra=docs.SYNC_EXTRA
)
def sync_monthly(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    return crud.sync_monthly(db, background_tasks)
