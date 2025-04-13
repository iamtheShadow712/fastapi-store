from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends
from .config import settings
from typing import Annotated
from .models import User
# from sqlalchemy.ext.declarative import declarative_base

# database_url = f"postgresql+psycopg2://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}/{settings.DATABASE_NAME}"
database_url = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(database_url)

# Base = declarative_base()

# create db and table automatically
# SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]


