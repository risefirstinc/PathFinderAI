from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Database Configuration
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", 3306))
    db_user: str = os.getenv("DB_USER", "root")
    db_password: str = os.getenv("DB_PASSWORD", "")
    db_name: str = os.getenv("DB_NAME", "pathfinder_db")
    
    # API Configuration
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", 8000))
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    @property
    def database_url(self) -> str:
        """Construct MySQL connection URL"""
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    class Config:
        env_file = ".env"

settings = Settings()
