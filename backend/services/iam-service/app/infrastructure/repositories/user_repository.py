from typing import Annotated, Dict
from loguru import logger
from fastapi import Depends
from sqlalchemy.orm import Session
from  core.db.database import get_db
from  domain.models.user_model import User


class UserRepository:
  def __init__(self, db: Annotated[Session, Depends(get_db)]):
    self.db = db

  def create_user(self, user: User) -> User:
    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)
    logger.info(f"✅User {user.user_id} created")
    return user

  def get_user_by_email(self, email: str) -> User:
    logger.info(f"📥Fetching user with email: {email}")
    return self.db.query(User).filter(User.email == email).first()

  def get_user_by_username(self, username: str) -> User:
    logger.info(f"📥Fetching user with username: {username}")
    return self.db.query(User).filter(User.username == username).first()


  def update_user(self, user_id: int, updated_user: Dict) -> User:
    user_query = self.db.query(User).filter(User.user_id == user_id)
    db_user = user_query.first()
    user_query.filter(User.user_id == user_id).update(
        updated_user, synchronize_session=False
    )
    self.db.commit()
    self.db.refresh(db_user)
    logger.info(f"User {user_id} updated✅")
    return db_user
