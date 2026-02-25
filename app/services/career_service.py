from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.roadmap import RoadMap
from app.models.overview import Overview
from app.models.location import Location
from app.schemas import RoadMap as RoadMapSchema, Overview as OverviewSchema, Location as LocationSchema
import logging

logger = logging.getLogger(__name__)

class RoadMapService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10) -> list[RoadMap]:
        try:
            return db.query(RoadMap).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching roadmaps: {str(e)}")
            raise

    @staticmethod
    def get_by_id(db: Session, roadmap_id: int) -> RoadMap:
        try:
            return db.query(RoadMap).filter(RoadMap.id == roadmap_id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching roadmap: {str(e)}")
            raise

class OverviewService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10) -> list[Overview]:
        try:
            return db.query(Overview).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching overviews: {str(e)}")
            raise

    @staticmethod
    def get_by_id(db: Session, overview_id: int) -> Overview:
        try:
            return db.query(Overview).filter(Overview.id == overview_id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching overview: {str(e)}")
            raise

class LocationService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10) -> list[Location]:
        try:
            return db.query(Location).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching locations: {str(e)}")
            raise

    @staticmethod
    def get_by_id(db: Session, location_id: int) -> Location:
        try:
            return db.query(Location).filter(Location.id == location_id).first()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching location: {str(e)}")
            raise
