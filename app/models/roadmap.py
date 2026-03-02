from sqlalchemy import Column, Integer, String
from app.database.base import Base


class RoadMap(Base):
    __tablename__ = "roadmaps"
    
    id = Column(Integer, primary_key=True, index=True)
    career_name = Column(String(255), nullable=False)
    milestone = Column(String(255), nullable=False)
    milestone_description = Column(String(500), nullable=False)
    priority = Column(Integer, nullable=False)
