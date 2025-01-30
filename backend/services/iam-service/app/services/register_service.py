from typing import Annotated
from loguru import logger
from fastapi import Depends, HTTPException, status

from domain.schemas.user_schema import (
    UserCreateSchema,
    UserResponseSchema,
    VerifyOTPSchema,
    VerifyOTPResponseSchema
)
from services.auth_services.auth_service import AuthService
from services.auth_services.otp_service import OTPService
from services.base_service import BaseService
from services.user_service import UserService

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/Token")

class RegisterService(BaseService):
    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
        auth_service: Annotated[AuthService, Depends()],
    ) -> None:
        super().__init__()

        self.user_service = user_service
        self.otp_service = otp_service
        self.auth_service = auth_service

    async def register_user(self, user: UserCreateSchema) -> UserResponseSchema:
        existing_email = await self.user_service.get_user_by_email(user.email)

        if existing_email:
            logger.error(f"User with mobile number {user.email} already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )

        existing_username = await self.user_service.get_user_by_username(user.username)
        if existing_username:
            logger.error(f"User with mobile number {user.username} already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Username taken"
            )    

        new_user = await self.user_service.create_user(user)
        otp = self.otp_service.send_otp(new_user.email)
        logger.info(f"User with email: {user.email} created successfully")
        return UserResponseSchema(
            first_name= new_user.first_name ,
            last_name= new_user.last_name ,
            email= new_user.email,
            is_verified=new_user.is_verified,
            username= new_user.username,
            message = 'user created✅'
        )
    async def verify_user(
        self, verify_user_schema: VerifyOTPSchema
    ) -> VerifyOTPResponseSchema:
        if not self.otp_service.verify_otp(
            verify_user_schema.email, verify_user_schema.otp
        ):
            logger.error(f"Invalid OTP for mobile number {verify_user_schema.email}❌")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP❌"
            )

        user = await self.user_service.get_user_by_email(
            verify_user_schema.email
        )

        await self.user_service.update_user(user.user_id, {"is_verified": True})

        logger.info(f"User with mobile number {verify_user_schema.email} verified✅")
        return VerifyOTPResponseSchema(
            verified=True, message="User Created Successfully, OTP Sent To The Email✅"
        )