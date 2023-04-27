from fastapi import APIRouter

from app.v1.endpoints import prayer_time
from app.v1.tags import Tags

api_router = APIRouter()
api_router.include_router(prayer_time.router, tags=[Tags.PRAYER_TIMES.value])
