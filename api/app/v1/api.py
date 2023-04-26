from fastapi import APIRouter

from app.v1.endpoints import prayer_time


api_router = APIRouter()
api_router.include_router(prayer_time.router)
