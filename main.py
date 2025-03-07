from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, select
from pydantic import BaseModel
import os

# Configuración de la base de datos
DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/timekeeper"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Modelo de la tabla 'holiday' 
# holiday_id/serial4
# name/varchar
# public_name/varchar
# year/int2
# country/varchar
# is_renounceable/bool
# is_local/bool
# start/timestamp
# end/timestamp,
# enable/bool
class Holiday(Base):
    __tablename__ = "holiday"
    #id = Column(Integer, primary_key=True, index=True)
    #name = Column(String, nullable=False)
    #date = Column(String, nullable=False)

# Esquema Pydantic para validación de datos
class HolidayCreate(BaseModel):
    #name: str
    #date: str

class HolidayUpdate(BaseModel):
    #name: str
    #date: str

# Dependencia para obtener la sesión de la base de datos
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

app = FastAPI()

# Endpoint para obtener todos los holidays
@app.get("/holidays")
async def get_holidays(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Holiday))
    holidays = result.scalars().all()
    return holidays

# Endpoint para agregar un holiday
@app.post("/holidays")
async def create_holiday(holiday: HolidayCreate, db: AsyncSession = Depends(get_db)):
    new_holiday = Holiday(name=holiday.name, date=holiday.date)
    db.add(new_holiday)
    await db.commit()
    await db.refresh(new_holiday)
    return new_holiday

# Endpoint para actualizar un holiday
@app.put("/holidays/{holiday_id}")
async def update_holiday(holiday_id: int, holiday: HolidayUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Holiday).where(Holiday.id == holiday_id))
    existing_holiday = result.scalars().first()
    if not existing_holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")
    existing_holiday.name = holiday.name
    existing_holiday.date = holiday.date
    await db.commit()
    await db.refresh(existing_holiday)
    return existing_holiday

# Endpoint para eliminar un holiday
@app.delete("/holidays/{holiday_id}")
async def delete_holiday(holiday_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Holiday).where(Holiday.id == holiday_id))
    holiday = result.scalars().first()
    if not holiday:
        raise HTTPException(status_code=404, detail="Holiday not found")
    await db.delete(holiday)
    await db.commit()
    return {"message": "Holiday deleted successfully"}


#por revisar 