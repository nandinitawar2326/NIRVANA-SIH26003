from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AlertCreate(BaseModel):

    patient_id: int

    message: str

    alert_type: Optional[str] = "general"


class AlertResponse(AlertCreate):

    id: int

    is_read: bool

    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True