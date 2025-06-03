from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean, TIMESTAMP
from datetime import datetime, timezone
from sqlalchemy.orm import relationship, Mapped
from core.db.database import Base
from sqlalchemy.sql import func 

class Follow(Base):
    __tablename__ = "follows"

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    following_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    followed_at = Column(TIMESTAMP, server_default=func.now())

    follower = relationship("User", foreign_keys=[user_id], backref="followings")
    following = relationship("User", foreign_keys=[following_id], backref="followers")
