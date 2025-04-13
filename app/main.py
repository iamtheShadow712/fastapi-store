from fastapi import FastAPI 
from app.routes import auth

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Server is up and running"}


app.include_router(auth.router)