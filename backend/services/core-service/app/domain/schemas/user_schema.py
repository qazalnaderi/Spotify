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

