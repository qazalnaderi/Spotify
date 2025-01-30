from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from loguru import logger

from domain.models.user_model import User
from domain.schemas.user_schema import (
    UserCreateSchema,
    UserResponseSchema,
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
