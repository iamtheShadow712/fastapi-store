from sqlmodel import SQLModel, Session, create_engine
from app.database import database_url, get_session
from app.config import settings
from app.main import app
import pytest
from fastapi.testclient import TestClient
import app.constants as CONSTANTS

database_url = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}_test"

engine = create_engine(database_url)


@pytest.fixture()
def session():
   SQLModel.metadata.drop_all(engine) 
   SQLModel.metadata.create_all(engine)
   with Session(engine) as session:
        yield session
        
@pytest.fixture()
def client(session):
    def override_get_session():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_session] = override_get_session         
    yield TestClient(app)
    
@pytest.fixture()
def first_user(client):
    user = {
        "username": "User 1",
        "email": "user1@email.com",
        "password": "user1"
    }
    res = client.post(f"/{CONSTANTS.API_VERSION}/auth/register", json=user)
    first_user = res.json()
    first_user['password'] = user['password']
    return first_user
   