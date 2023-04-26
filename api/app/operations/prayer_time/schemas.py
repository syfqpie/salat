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
    hijri_date: str
    date: datetime.date
    imsak: str


class PrayerTimeCreate(PrayerTimeBase):
    pass


class PrayerTime(PrayerTimeBase):
    id: int

    class Config:
        orm_mode = True
