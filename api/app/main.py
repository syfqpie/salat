from functools import lru_cache

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.v1.api import api_router
from app.core.settings import settings
from app.core.database import Base, engine
from app.v1.tags import tags_metadata


@lru_cache()
def get_settings():
    # https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
    return settings


app = FastAPI(
    title=get_settings().PROJECT_NAME,
    openapi_url=f"{ get_settings().API_V1_STR }/openapi.json",
    version=get_settings().VERSION,
    description=get_settings().DESCRIPTION,
    openapi_tags=tags_metadata,
)

# Database
Base.metadata.create_all(bind=engine)

# CORS config
# https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
if get_settings().BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in get_settings().BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Router
app.include_router(api_router, prefix=get_settings().API_V1_STR)
