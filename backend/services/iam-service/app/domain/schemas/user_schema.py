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

class VerifyOTPSchema(BaseModel):
    email: str
    otp: str
    model_config = ConfigDict(from_attributes=True)

class VerifyOTPResponseSchema(BaseModel):
    verified: bool
    message: str


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserInfoSchema(BaseModel):
    user_id: int
    library_id: int
    first_name: str
    last_name: str
    email: str
    username: str
    class Config:
        from_attributes = True

class ResendOTPSchema(BaseModel):
    email: str

class ResendOTPResponseSchema(BaseModel):
    email: str
    OTP: str
    message: str        