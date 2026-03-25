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
    def get_all(db: Session, skip: int = 0, limit: int = 10) -> list:
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

    @staticmethod
    def create(db: Session, roadmap: RoadMapSchema) -> RoadMap:
        try:
            db_roadmap = RoadMap(**roadmap.dict(exclude_unset=True))
            db.add(db_roadmap)
            db.commit()
            db.refresh(db_roadmap)
            return db_roadmap
        except SQLAlchemyError as e:
            logger.error(f"Error creating roadmap: {str(e)}")
            db.rollback()
            raise

    @staticmethod
    def update(db: Session, roadmap_id: int, roadmap: RoadMapSchema) -> RoadMap:
        try:
            db_roadmap = db.query(RoadMap).filter(RoadMap.id == roadmap_id).first()
            if not db_roadmap:
                return None
            for key, value in roadmap.dict(exclude_unset=True).items():
                setattr(db_roadmap, key, value)
            db.commit()
            db.refresh(db_roadmap)
            return db_roadmap
        except SQLAlchemyError as e:
            logger.error(f"Error updating roadmap: {str(e)}")
            db.rollback()
            raise

    @staticmethod
    def delete(db: Session, roadmap_id: int) -> bool:
        try:
            db_roadmap = db.query(RoadMap).filter(RoadMap.id == roadmap_id).first()
            if not db_roadmap:
                return False
            db.delete(db_roadmap)
            db.commit()
            return True
        except SQLAlchemyError as e:
            logger.error(f"Error deleting roadmap: {str(e)}")
            db.rollback()
            raise


class OverviewService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10) -> list:
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

    @staticmethod
    def create(db: Session, overview: OverviewSchema) -> Overview:
        try:
            db_overview = Overview(**overview.dict(exclude_unset=True))
            db.add(db_overview)
            db.commit()
            db.refresh(db_overview)
            return db_overview
        except SQLAlchemyError as e:
            logger.error(f"Error creating overview: {str(e)}")
            db.rollback()
            raise

    @staticmethod
    def update(db: Session, overview_id: int, overview: OverviewSchema) -> Overview:
        try:
            db_overview = db.query(Overview).filter(Overview.id == overview_id).first()
            if not db_overview:
                return None
            for key, value in overview.dict(exclude_unset=True).items():
                setattr(db_overview, key, value)
            db.commit()
            db.refresh(db_overview)
            return db_overview
        except SQLAlchemyError as e:
            logger.error(f"Error updating overview: {str(e)}")
            db.rollback()
            raise

    @staticmethod
    def delete(db: Session, overview_id: int) -> bool:
        try:
            db_overview = db.query(Overview).filter(Overview.id == overview_id).first()
            if not db_overview:
                return False
            db.delete(db_overview)
            db.commit()
            return True
        except SQLAlchemyError as e:
            logger.error(f"Error deleting overview: {str(e)}")
            db.rollback()
            raise


class LocationService:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10) -> list:
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

    @staticmethod
    def create(db: Session, location: LocationSchema) -> Location:
        try:
            db_location = Location(**location.dict(exclude_unset=True))
            db.add(db_location)
            db.commit()
            db.refresh(db_location)
            return db_location
        except SQLAlchemyError as e:
            logger.error(f"Error creating location: {str(e)}")
            db.rollback()
            raise

    @staticmethod
    def update(db: Session, location_id: int, location: LocationSchema) -> Location:
        try:
            db_location = db.query(Location).filter(Location.id == location_id).first()
            if not db_location:
                return None
            for key, value in location.dict(exclude_unset=True).items():
                setattr(db_location, key, value)
            db.commit()
            db.refresh(db_location)
            return db_location
        except SQLAlchemyError as e:
            logger.error(f"Error updating location: {str(e)}")
            db.rollback()
            raise

    @staticmethod
    def delete(db: Session, location_id: int) -> bool:
        try:
            db_location = db.query(Location).filter(Location.id == location_id).first()
            if not db_location:
                return False
            db.delete(db_location)
            db.commit()
            return True
        except SQLAlchemyError as e:
            logger.error(f"Error deleting location: {str(e)}")
            db.rollback()
            raise

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
