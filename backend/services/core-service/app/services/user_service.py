from typing import Annotated, Dict
from loguru import logger
from fastapi import Depends
from  domain.models.user_model import User
from  infrastructure.repositories.user_repository import UserRepository
from  services.auth_services.hash_service import HashService
from  services.base_service import BaseService
from domain.schemas.user_schema import UserInfoSchema

class UserService(BaseService):
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        hash_service: Annotated[HashService, Depends()],
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.hash_service = hash_service

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

    async def get_user_info(self,  user_id: int) -> UserInfoSchema:   
        logger.info(f"📥 Fetching user with id: {user_id}")
        user = self.user_repository.get_user_by_id(user_id)
        return UserInfoSchema (
            user_id = user.user_id,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            username = user.username
        )     