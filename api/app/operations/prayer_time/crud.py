import datetime

from sqlalchemy import extract
from sqlalchemy.orm import Session

from app.operations.prayer_time import models


def get_zones(db: Session):
    """Query all zones"""
    return db.query(models.Zone).all()


def get_zones_by_state(db: Session, state: str):
    """Query zones by state"""
    return db.query(models.Zone).filter(models.Zone.state == state).all()


def get_prayer_times_by_zone(db: Session, zone_code: str, weekly: bool = False):
    """Query prayer times by zone and filter by current year and month / week"""
    current_year = datetime.datetime.now().year
    q_filters = [
        models.PrayerTime.zone.has(code=zone_code),
        extract("year", models.PrayerTime.date) == current_year,
    ]

    if weekly:
        current_week = datetime.datetime.now().isocalendar()[1]
        q_filters.append(extract("week", models.PrayerTime.date) == current_week)
    else:
        current_month = datetime.datetime.now().month
        q_filters.append(extract("month", models.PrayerTime.date) == current_month)

    return db.query(models.PrayerTime).filter(*q_filters).all()
