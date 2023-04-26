from sqlalchemy.orm import Session

from app.operations.prayer_time import models


def get_zones(db: Session):
    return db.query(models.Zone).all()


def get_zones_by_state(db: Session, state: str):
    return db.query(models.Zone).filter(models.Zone.state == state)
