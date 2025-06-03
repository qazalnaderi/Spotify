from typing import Annotated, Dict
from loguru import logger
from fastapi import Depends
from  domain.models.user_model import User
from  domain.schemas.user_schema import UserCreateSchema
from  infrastructure.repositories.user_repository import UserRepository
from  services.auth_services.hash_service import HashService
from  services.base_service import BaseService


class UserService(BaseService):
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        hash_service: Annotated[HashService, Depends()],
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.hash_service = hash_service

    async def create_user(self, user_body: UserCreateSchema) -> User:
        logger.info(f"⚒️ Creating user with email: {user_body.email}")
        return self.user_repository.create_user(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                email=user_body.email,
                username= user_body.username,
                password=self.hash_service.hash_password(user_body.password),
            )
        )

    async def get_user_by_email(self, email: str) -> User:
        logger.info(f"📥 Fetching user with email {email}")
        return self.user_repository.get_user_by_email(email)

    async def get_user_by_id(self, user_id: int) -> User:
        logger.info(f"📥 Fetching user with id {user_id}")
        return self.user_repository.get_user_by_id(user_id)    

    async def get_user_by_username(self, username: str) -> User:
        logger.info(f"📥 Fetching user with username {username}")
        return self.user_repository.get_user_by_username(username)    

    async def update_user(self, user_id: int, update_fields: Dict) -> User:
        logger.info(f"🔃 Updating user with id {user_id}")
        return self.user_repository.update_user(user_id, update_fields)    