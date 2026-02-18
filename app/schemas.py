from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    """Schema for creating a user"""
    password: str

class UserUpdate(BaseModel):
    """Schema for updating a user"""
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponse(UserBase):
    """Schema for user responses"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

#========================================

class RoadMap(BaseModel):
    """Base roadmap schema"""
    id: int
    career_name: str
    milestone: str
    milestone_description: str
    priority: int

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