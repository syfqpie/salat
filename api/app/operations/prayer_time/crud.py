import os
import datetime

from fastapi import BackgroundTasks, responses, status
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


def sync_monthly(db: Session, background_tasks: BackgroundTasks):
    """Query first entry of this month data, if no data found, sync latest monthly"""
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    month_entry = (
        db.query(models.PrayerTime)
        .filter(
            extract("year", models.PrayerTime.date) == current_year,
            extract("month", models.PrayerTime.date) == current_month,
        )
        .first()
    )

    if not month_entry:
        background_tasks.add_task(run_sync_script)

        return responses.JSONResponse(
            content={"status": "Syncing"}, status_code=status.HTTP_202_ACCEPTED
        )

    return responses.JSONResponse(
        content={"status": "Already synced"}, status_code=status.HTTP_200_OK
    )


def run_sync_script():
    return os.system("pipenv run python ./scripts/scrapper.py ")
