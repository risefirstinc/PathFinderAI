from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Location(Base):
    __tablename__ = "locations"
    
    id = Column(Integer, primary_key=True, index=True)
    career_name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
