from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost:5432/timekeeper"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

metadata = MetaData()
