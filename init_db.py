"""
Database initialization script to create all tables
Run this script to initialize the AWS RDS database
"""
from app.database.base import Base
from app.database.connection import engine
from app.models import RoadMap, Overview, Location
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db():
    """Create all database tables"""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise


if __name__ == "__main__":
    init_db()
