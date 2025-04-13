from fastapi import APIRouter, HTTPException, Response, status
import app.constants as CONSTANT
from app.database import SessionDep
from app.schemas import UserCreate
from app.models import User
from app.utils import hash_password

router = APIRouter(
    prefix=f"/{CONSTANT.API_VERSION}/auth"
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, session: SessionDep):

    try:
        user_exist = session.query(User).filter(User.email == user.email).first()
        if user_exist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists with the provided credentials")
        user_dict = user.model_dump()
        user_dict['password'] = hash_password.hash(user.password)
        new_user = User(**user_dict)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {"message": "Registration Successfull"}
    except HTTPException as http_error:
        raise http_error
