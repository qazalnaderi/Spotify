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
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from api.v1.endpoints.user_route import core_user_router
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info("Core Service Started")

app.include_router(core_user_router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Hello Dear! Welcome to the IAM service."}

