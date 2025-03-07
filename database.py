from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://usuario:clave@localhost:5432/mi_bd"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

metadata = MetaData()
