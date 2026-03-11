from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("database_url")

engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
