from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean
from datetime import datetime, timezone
from sqlalchemy.orm import relationship, Mapped
from core.db.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(15), unique=True, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)