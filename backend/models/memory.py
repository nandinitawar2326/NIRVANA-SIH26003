from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Memory(BaseModel):
    patient_id: int
    title: str
    description: Optional[str] = None
    memory_date: Optional[datetime] = None