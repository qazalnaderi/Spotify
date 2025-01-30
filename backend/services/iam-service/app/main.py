import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)
logger.info("Custom logging is configured.")
import smtplib
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.account_route import user_router
from app.api.endpoints.login_route import login_router
from app.api.endpoints.profile_management_route import profile_router
from app.api.endpoints.contacts_route import contact_router
from app.api.endpoints.email_route import email_router
from app.api.endpoints.report_route import report_router
from app.api.endpoints.admin_route import admin_router
from app.api.endpoints.auth_route import auth_router
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info("IAM Service Started")

@app.get("/")
async def root():
    return {"message": "Hello Dear! Welcome to the IAM service."}

