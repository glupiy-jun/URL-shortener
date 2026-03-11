from sqlalchemy import Column, Integer, String
from .database import Base

class URL(Base):
    __tablename__ = "__urls__"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String, unique=True, index=True)
    original_url = Column(String)
    clicks = Column(Integer, default=0)
