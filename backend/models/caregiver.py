from pydantic import BaseModel
from typing import Optional


class Caregiver(BaseModel):
    patient_id: int
    name: str
    relationship: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None