from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

MYSQL_URL = f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(MYSQL_URL, echo=True)

# existing_databases = engine.execute("SHOW DATABASES;")
# existing_databases = [d[0] for d in existing_databases]
# print(existing_databases)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
