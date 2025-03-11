from sqlite3.dbapi2 import version
from fastapi import FastAPI   
from scr.core.config import settings
from src.DB import Base 

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get("/")
def root():
    return {'message:hola hola'}