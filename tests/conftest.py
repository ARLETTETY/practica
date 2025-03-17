import pytest
import sys
import os
# Añade el directorio src al path. 
#agrega el directorio src al sys.path dinámicamente, permitiendo 
# que el archivo test_main.py encuentre el módulo main dentro de src


from src.db.session import SessionLocal, engine
from src.models import Base

@pytest.fixture(scope="module")
def db():
    # Configurar base de datos de prueba
    Base.metadata.create_all(bind=engine)
    db_session = SessionLocal()
    yield db_session
    db_session.close()
    Base.metadata.drop_all(bind=engine)
