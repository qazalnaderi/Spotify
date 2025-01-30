from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional


class UserBase(BaseModel):
    first_name: str 
    last_name: str 
    email: str
    username: str
   

class UserCreateSchema(UserBase):
    password: str
    confirm_password: str

class UserResponseSchema(UserBase):
    message: str




class RegistrationResponse(BaseModel):
    message: str
    model_config = ConfigDict(from_attributes=True)
