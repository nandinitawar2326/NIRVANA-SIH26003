from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ==========================================
# CREATE REMINDER
# ==========================================

class ReminderCreate(BaseModel):

    patient_id: int
    title: str
    description: Optional[str] = None
    reminder_time: datetime


# ==========================================
# UPDATE REMINDER
# ==========================================

class ReminderUpdate(BaseModel):

    completed: bool


# ==========================================
# REMINDER RESPONSE
# ==========================================

class ReminderResponse(ReminderCreate):

    id: int
    completed: bool
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True