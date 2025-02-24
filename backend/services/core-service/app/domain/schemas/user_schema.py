from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional

class UserInfoSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str

    class Config:
        from_attributes = True

class UpdateUserInfoSchema(BaseModel):
    password: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
