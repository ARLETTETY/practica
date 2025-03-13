from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import engine
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
# el autocommit y autoflush se dejan en false, 
#ya que por defecto va a estar en true, para manejar la grabación de los datos, es decir el db.commit() o flush.commit() 
#por lo que no se sincronizaran de inmediato con la bd