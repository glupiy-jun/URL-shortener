import random
import string
from sqlalchemy.orm import Session
from .models import URL

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def create_url(db: Session, original_url: str):

    short_id = generate_short_id()

    url = URL(
        short_id=short_id,
        original_url=original_url
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url

def get_url(db: Session, short_id: str):
    return db.query(URL).filter(URL.short_id == short_id).first()

def add_click(db: Session, url: URL):
    url.clicks += 1
    db.commit()
