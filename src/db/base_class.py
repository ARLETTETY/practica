from sqlalchemy.ext.declarative import as_declarative, declared_attr
from src.db.declarative_base import Base as Base_declarative

class Base(Base_declarative):
        @declared_attr
        def __tablename__(cls)->str:
            return cls.__name__.lower()

