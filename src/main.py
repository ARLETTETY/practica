from sqlite3.dbapi2 import version
from fastapi import FastAPI   
from src.core.config import settings
from src.db.declarative_base import Base
from src.db.session import engine
from src.models.feriado import Feriado
from src.api.routes.feriado import router as feriado_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

#con esto se crea la tabla que se declararon con la base 
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {'message:hola hola'}



