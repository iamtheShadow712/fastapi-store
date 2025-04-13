from passlib.context import CryptContext

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password):
    return pass_context.hash(password)

def verify(password, hashed_password):
    return pass_context.verify(password, hashed_password)