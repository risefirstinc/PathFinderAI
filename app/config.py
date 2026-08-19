from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Database Configuration
    db_host: str = "career-database.ckffsif8jnhi.us-east-2.rds.amazonaws.com"
    db_port: int = 3306
    db_user: str = "career_admin"
    db_password: str = "careerpassword2026"
    db_name: str = "career_info_db"
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False
    
    @property
    def database_url(self) -> str:
        """Construct MySQL connection URL"""
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
