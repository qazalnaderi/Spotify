import sqlalchemy
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


SQLALCHEMY_DATABASE_URL = ""


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)
Base = sqlalchemy.orm.declarative_base()

AsyncSessionLocal = sessionmaker(
    bind=engine, 
    class_=AsyncSession,  
    expire_on_commit=False, 
)

async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db  
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        finally:
            await db.close()

