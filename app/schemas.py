from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class RoadMap(BaseModel):
    """Base roadmap schema"""
    id: int
    career_name: str
    milestone: str
    milestone_description: str
    priority: int

    model_config = ConfigDict(from_attributes=True)

class Overview(BaseModel):
    """Base overview schema"""
    id: int
    career_name: str
    avg_salary_range: str
    avg_min_degree: str
    avg_time_to_complete: str
    education_cost: str
    alternate_career_names: Optional[str] = None

class Location(BaseModel):
    """Base location schema"""
    id: int
    career_name: str
    location: str