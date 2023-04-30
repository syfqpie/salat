import datetime
from pydantic import BaseModel


class ZoneBase(BaseModel):
    code: str
    text: str
    state: str


class ZoneCreate(ZoneBase):
    pass


class Zone(ZoneBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

    class Config:
        orm_mode = True


class PrayerTimeBase(BaseModel):
    hijri_date: datetime.date
    date: datetime.date
    imsak: str
    date: datetime.date
    imsak: datetime.time
    fajr: datetime.time
    syuruk: datetime.time
    dhuhr: datetime.time
    asr: datetime.time
    maghrib: datetime.time
    isha: datetime.time


class PrayerTimeCreate(PrayerTimeBase):
    pass


class PrayerTime(PrayerTimeBase):
    id: int
    zone_code: str

    class Config:
        orm_mode = True


class SyncBase(BaseModel):
    status: str
