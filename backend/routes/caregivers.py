from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.caregiver import Caregiver
from models.database_models import CaregiverDB
from services.database import get_db


router = APIRouter(
    prefix="/caregivers",
    tags=["Caregivers"]
)


# Add caregiver
@router.post("/")
def create_caregiver(
    caregiver: Caregiver,
    db: Session = Depends(get_db)
):

    new_caregiver = CaregiverDB(
        name=caregiver.name,
        phone=caregiver.phone,
        relationship=caregiver.relationship,
        patient_id=caregiver.patient_id
    )

    db.add(new_caregiver)
    db.commit()
    db.refresh(new_caregiver)

    return {
        "message": "Caregiver added successfully 👨‍⚕️",
        "caregiver": {
            "id": new_caregiver.id,
            "name": new_caregiver.name,
            "phone": new_caregiver.phone,
            "relationship": new_caregiver.relationship,
            "patient_id": new_caregiver.patient_id
        }
    }


# Get all caregivers
@router.get("/")
def get_all_caregivers(
    db: Session = Depends(get_db)
):

    caregivers = db.query(CaregiverDB).all()

    return {
        "total_caregivers": len(caregivers),
        "caregivers": caregivers
    }


# Get caregivers for a patient
@router.get("/patient/{patient_id}")
def get_patient_caregivers(
    patient_id: int,
    db: Session = Depends(get_db)
):

    caregivers = (
        db.query(CaregiverDB)
        .filter(CaregiverDB.patient_id == patient_id)
        .all()
    )

    return {
        "patient_id": patient_id,
        "total_caregivers": len(caregivers),
        "caregivers": caregivers
    }


# Delete caregiver
@router.delete("/{caregiver_id}")
def delete_caregiver(
    caregiver_id: int,
    db: Session = Depends(get_db)
):

    caregiver = (
        db.query(CaregiverDB)
        .filter(CaregiverDB.id == caregiver_id)
        .first()
    )

    if not caregiver:
        raise HTTPException(
            status_code=404,
            detail="Caregiver not found"
        )

    db.delete(caregiver)
    db.commit()

    return {
        "message": "Caregiver deleted successfully"
    }