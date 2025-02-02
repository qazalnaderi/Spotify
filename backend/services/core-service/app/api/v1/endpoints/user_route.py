from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from loguru import logger

from domain.models.user_model import User
from domain.schemas.user_schema import (
    UserInfoSchema
)
from domain.schemas.token_schema import TokenDataSchema
from services.auth_services.auth_service import get_current_user
from services.user_service import UserService

core_user_router = APIRouter()

@core_user_router.get(
    "/get_user_informations", status_code=status.HTTP_200_OK
)
async def get_user_info(
        current_user: Annotated[TokenDataSchema, Depends(get_current_user)],
        user_service: Annotated[UserService, Depends()]
):
    logger.info(f'📥 fetching user info for user {current_user.user_id}')
    return await user_service.get_user_info(current_user.user_id)