from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.user import User
from app.schemas import UserCreate, UserUpdate
import logging

logger = logging.getLogger(__name__)

class UserService:
    """Service layer for user operations"""
    
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        """Create a new user"""
        try:
            db_user = User(
                email=user.email,
                username=user.username,
                full_name=user.full_name,
                hashed_password=user.password,  # In production, hash this password
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            logger.info(f"User created: {db_user.id}")
            return db_user
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error creating user: {str(e)}")
            raise
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        """Get user by ID"""
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                logger.warning(f"User not found: {user_id}")
            return user
        except SQLAlchemyError as e:
            logger.error(f"Error fetching user: {str(e)}")
            raise
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        """Get user by email"""
        try:
            user = db.query(User).filter(User.email == email).first()
            return user
        except SQLAlchemyError as e:
            logger.error(f"Error fetching user by email: {str(e)}")
            raise
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
        """Get all users with pagination"""
        try:
            users = db.query(User).offset(skip).limit(limit).all()
            return users
        except SQLAlchemyError as e:
            logger.error(f"Error fetching users: {str(e)}")
            raise
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User:
        """Update user information"""
        try:
            db_user = db.query(User).filter(User.id == user_id).first()
            if not db_user:
                return None
            
            update_data = user_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_user, field, value)
            
            db.commit()
            db.refresh(db_user)
            logger.info(f"User updated: {user_id}")
            return db_user
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error updating user: {str(e)}")
            raise
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Delete a user"""
        try:
            db_user = db.query(User).filter(User.id == user_id).first()
            if not db_user:
                return False
            
            db.delete(db_user)
            db.commit()
            logger.info(f"User deleted: {user_id}")
            return True
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error deleting user: {str(e)}")
            raise
