from os import environ as env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
       
SQLALCHEMY_DATABASE_URL = env.get("DATABASE_URL")
print(SQLALCHEMY_DATABASE_URL)
db_engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()