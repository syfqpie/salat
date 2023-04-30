import os
from app.core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def run_sync_script():
    return os.system("pipenv shell; python ./scripts/scrapper.py")
