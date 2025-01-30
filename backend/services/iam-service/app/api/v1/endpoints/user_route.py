from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from loguru import logger

from domain.models.user_model import User
from domain.schemas.user_schema import (
    UserCreateSchema,
    UserResponseSchema,
    VerifyOTPSchema,
    VerifyOTPResponseSchema
)
from services.auth_services.auth_service import AuthService
from services.register_service import RegisterService
from services.user_service import UserService

user_router = APIRouter()


@user_router.post(
    "/Register",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user: UserCreateSchema, register_service: Annotated[RegisterService, Depends()]
) -> UserResponseSchema:
    logger.info(f"Registering user with email:{user.email}")
    return await register_service.register_user(user)


@user_router.post(
    "/VerifyOTP", response_model=VerifyOTPResponseSchema, status_code=status.HTTP_200_OK
)
async def verify_otp(
    verify_user_schema: VerifyOTPSchema,
    register_service: Annotated[RegisterService, Depends()],
) -> VerifyOTPResponseSchema:
    logger.info(f"Verifying OTP for user with email {verify_user_schema.email}")
    return await register_service.verify_user(verify_user_schema)