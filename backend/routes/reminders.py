from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.reminder import ReminderCreate, ReminderUpdate
from models.database_models import ReminderDB
from services.database import get_db


router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"]
)


# ==========================================
# CREATE REMINDER
# ==========================================

@router.post("/")
def create_reminder(
    reminder: ReminderCreate,
    db: Session = Depends(get_db)
):

    new_reminder = ReminderDB(
        patient_id=reminder.patient_id,
        title=reminder.title,
        description=reminder.description,
        reminder_time=reminder.reminder_time,
        completed=False
    )

    db.add(new_reminder)
    db.commit()
    db.refresh(new_reminder)

    return {
        "message": "Reminder created successfully ⏰",
        "reminder": {
            "id": new_reminder.id,
            "patient_id": new_reminder.patient_id,
            "title": new_reminder.title,
            "description": new_reminder.description,
            "reminder_time": new_reminder.reminder_time,
            "completed": new_reminder.completed,
            "created_at": new_reminder.created_at
        }
    }


# ==========================================
# GET PATIENT REMINDERS
# ==========================================

@router.get("/patient/{patient_id}")
def get_patient_reminders(
    patient_id: int,
    db: Session = Depends(get_db)
):

    reminders = (
        db.query(ReminderDB)
        .filter(ReminderDB.patient_id == patient_id)
        .order_by(ReminderDB.reminder_time)
        .all()
    )

    return {
        "patient_id": patient_id,
        "total_reminders": len(reminders),
        "reminders": reminders
    }


# ==========================================
# MARK REMINDER AS COMPLETED
# ==========================================

@router.put("/{reminder_id}/complete")
def complete_reminder(
    reminder_id: int,
    update: ReminderUpdate,
    db: Session = Depends(get_db)
):

    reminder = (
        db.query(ReminderDB)
        .filter(ReminderDB.id == reminder_id)
        .first()
    )

    if not reminder:
        raise HTTPException(
            status_code=404,
            detail="Reminder not found"
        )

    reminder.completed = update.completed

    db.commit()
    db.refresh(reminder)

    return {
        "message": "Reminder updated successfully",
        "reminder": reminder
    }


# ==========================================
# DELETE REMINDER
# ==========================================

@router.delete("/{reminder_id}")
def delete_reminder(
    reminder_id: int,
    db: Session = Depends(get_db)
):

    reminder = (
        db.query(ReminderDB)
        .filter(ReminderDB.id == reminder_id)
        .first()
    )

    if not reminder:
        raise HTTPException(
            status_code=404,
            detail="Reminder not found"
        )

    db.delete(reminder)
    db.commit()

    return {
        "message": "Reminder deleted successfully"
    }