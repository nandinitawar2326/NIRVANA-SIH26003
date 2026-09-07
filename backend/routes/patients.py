from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.patient import Patient
from models.database_models import PatientDB
from services.database import get_db


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# ==========================================
# CREATE PATIENT
# ==========================================

@router.post("/")
def create_patient(
    patient: Patient,
    db: Session = Depends(get_db)
):

    new_patient = PatientDB(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient created successfully",
        "patient": new_patient
    }


# ==========================================
# GET ALL PATIENTS
# ==========================================

@router.get("/")
def get_patients(
    db: Session = Depends(get_db)
):

    patients = db.query(PatientDB).all()

    return {
        "total_patients": len(patients),
        "patients": patients
    }


# ==========================================
# GET SINGLE PATIENT
# ==========================================

@router.get("/{patient_id}")
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = (
        db.query(PatientDB)
        .filter(PatientDB.id == patient_id)
        .first()
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# ==========================================
# DELETE PATIENT
# ==========================================

@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = (
        db.query(PatientDB)
        .filter(PatientDB.id == patient_id)
        .first()
    )

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return {
        "message": "Patient deleted successfully"
    }