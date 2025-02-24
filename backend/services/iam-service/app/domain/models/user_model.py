from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean, TIMESTAMP
from datetime import datetime, timezone
from sqlalchemy.orm import relationship, Mapped
from core.db.database import Base
from sqlalchemy.sql import func 

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    library_id = Column(Integer, unique=True, nullable=False, server_default=func.nextval("users_user_id_seq"))  
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    is_artist = Column(Boolean, default=False, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False) 
    profile_url = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
