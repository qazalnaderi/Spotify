from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional
class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    user_id: int
    email: Optional[str] = None
    first_name: str
    last_name: str