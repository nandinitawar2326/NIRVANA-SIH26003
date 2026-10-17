from pydantic import BaseModel
from typing import Optional


class FamilyMember(BaseModel):

    name: str

    relationship: Optional[str] = None

    phone: Optional[str] = None


class FamilyResponse(FamilyMember):

    id: int

    patient_id: int