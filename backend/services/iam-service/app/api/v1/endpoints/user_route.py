from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from loguru import logger

from domain.models.user_model import User
from domain.schemas.user_schema import (
    UserCreateSchema,
    UserResponseSchema,
    VerifyOTPSchema,
    VerifyOTPResponseSchema,
    UserLoginSchema,
    UserInfoSchema,
    ResendOTPResponseSchema,
    ResendOTPSchema
        )
from domain.schemas.token_schema import TokenSchema
from services.auth_services.auth_service import AuthService
from services.register_service import RegisterService
from services.user_service import UserService
from services.auth_services.auth_service import get_current_user
user_router = APIRouter()

#TODO add check username password email
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

#TODO check if it'd be better to get username instead of email
@user_router.post("/login", response_model=TokenSchema, status_code=status.HTTP_200_OK)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
) -> TokenSchema:

    logger.info(f"Logging in user with email {form_data.username}")
    return await auth_service.authenticate_user(
        UserLoginSchema(email=form_data.username, password=form_data.password)
    )    

@user_router.post(
    "/ResendOTP",
    response_model=ResendOTPResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def resend_otp(
    resend_otp_schema: ResendOTPSchema,
    register_service: Annotated[RegisterService, Depends()],
) -> ResendOTPResponseSchema:
    logger.info(f"Resending OTP for user with email {resend_otp_schema.email}")
    return await register_service.resend_otp(resend_otp_schema)

@user_router.get("/Me", response_model=UserInfoSchema, status_code=status.HTTP_200_OK)
async def read_me(current_user: User = Depends(get_current_user)) -> UserInfoSchema:
    logger.info(f"📥 Getting user with email {current_user.email}")
    return current_user