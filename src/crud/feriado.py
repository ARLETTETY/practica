from sqlalchemy.orm import Session
from src.models.feriado import Feriado
from src.schemas.feriado import FeriadoCreate, FeriadoUpdate

def get_feriados(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Feriado).offset(skip).limit(limit).all()

def get_feriado_by_id(db: Session, holiday_id: int):
    return db.query(Feriado).filter(Feriado.holiday_id == holiday_id).first()

def create_feriado(db: Session, feriado_data: FeriadoCreate):
    db_feriado = Feriado(**feriado_data.dict())
    db.add(db_feriado)
    db.commit()
    db.refresh(db_feriado)
    return db_feriado

def update_feriado(db: Session, holiday_id: int, feriado_data: FeriadoUpdate):
    db_feriado = db.query(Feriado).filter(Feriado.holiday_id == holiday_id).first()
    if not db_feriado:
        return None
    for key, value in feriado_data.dict(exclude_unset=True).items():
        setattr(db_feriado, key, value)
    db.commit()
    db.refresh(db_feriado)
    return db_feriado

def delete_feriado(db: Session, holiday_id: int):
    db_feriado = db.query(Feriado).filter(Feriado.holiday_id == holiday_id).first()
    if not db_feriado:
        return None
    db.delete(db_feriado)
    db.commit()
    return db_feriado
