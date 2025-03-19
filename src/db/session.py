from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import engine
from src.core.config import settings

#esto es la configuración de SQLAlchemy con la URL de la base de datos desde .env

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
# el autocommit y autoflush se dejan en false, 
#ya que por defecto va a estar en true, para manejar la grabación de los datos, es decir el db.commit() o flush.commit() 
#por lo que no se sincronizaran de inmediato con la bd


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()