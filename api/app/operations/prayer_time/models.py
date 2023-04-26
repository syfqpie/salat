# from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Time
from sqlalchemy.orm import relationship

from app.core.database import Base


class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    text = Column(String, index=True)
    state = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True, default=None)


class PrayerTime(Base):
    __tablename__ = "prayer_times"

    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(Integer, ForeignKey("zones.id"))
    zone = relationship("Zone")
    hijri_date = Column(Date, nullable=False)
    date = Column(Date, nullable=False)
    imsak = Column(Time, nullable=False)
    fajr = Column(Time, nullable=False)
    syuruk = Column(Time, nullable=False)
    dhuhr = Column(Time, nullable=False)
    asr = Column(Time, nullable=False)
    maghrib = Column(Time, nullable=False)
    isha = Column(Time, nullable=False)
