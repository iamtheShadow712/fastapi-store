from sqlalchemy import String, DateTime, Integer, Column, func
from sqlmodel import Field, SQLModel
from datetime import datetime
from sqlalchemy.sql import expression


class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int = Field(sa_column=Column(Integer, primary_key=True, nullable=False))
    username: str = Field(sa_column=Column(String, nullable=False, index=True))
    email: str = Field(sa_column=Column(String, nullable=False, index=True, unique=True))
    password: str = Field(sa_column=Column(String, nullable=False))
    phone_number: str = Field(sa_column=Column(String, nullable=True))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=expression.func.now()))