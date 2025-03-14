# valida los datos de entrada y salida de la api

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeriadoBase(BaseModel):
    name: str
    public_name: str
    year: int
    country: str
    is_renounceable: bool
    is_local: bool
    start: datetime
    end: datetime
    enable: Optional[bool] = True

class FeriadoCreate(FeriadoBase):
    pass

class FeriadoUpdate(FeriadoBase):
    pass

class FeriadoResponse(FeriadoBase):
    holiday_id: int

    class Config:
        orm_mode = True
