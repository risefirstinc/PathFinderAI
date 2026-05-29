from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Overview(Base):
    __tablename__ = "overview"
    
    id = Column(Integer, primary_key=True, index=True)
    career_name = Column(String(255), nullable=False)
    avg_salary_range = Column(String(255), nullable=False)
    avg_min_degree = Column(String(255), nullable=False)
    avg_time_to_complete = Column(String(255), nullable=False)
    education_cost = Column(String(255), nullable=False)
    alternate_career_names = Column(String(500), nullable=True)
