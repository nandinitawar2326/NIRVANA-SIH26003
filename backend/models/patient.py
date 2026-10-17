from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ==========================================
# PATIENT CREATE MODEL
# ==========================================

class Patient(BaseModel):

    name: str

    age: Optional[int] = None

    gender: Optional[str] = None

    phone: Optional[str] = None

    address: Optional[str] = None


# ==========================================
# PATIENT RESPONSE MODEL
# ==========================================

class PatientResponse(Patient):

    id: int

    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True