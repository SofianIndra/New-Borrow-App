from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from dotenv import load_dotenv
import os

###
# Database Configuration
###

# Load environment variables once at the start
load_dotenv()

# Get Database URL from .env
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

# Get Limit Var from .env
# LIMIT = os.getenv('LIMIT')

engine = create_engine(
   SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
