from fastapi import APIRouter, HTTPException
from models.family import FamilyMember


router = APIRouter(
    prefix="/family",
    tags=["Family"]
)


# Temporary in-memory storage
family_members = []


# ==========================================
# ADD FAMILY MEMBER FOR A PATIENT
# ==========================================

@router.post("/patient/{patient_id}")
def add_family_member(
    patient_id: int,
    member: FamilyMember
):

    member_data = member.model_dump()

    member_data["id"] = len(family_members) + 1
    member_data["patient_id"] = patient_id

    family_members.append(member_data)

    return {
        "message": "Family member added successfully",
        "family_member": member_data
    }


# ==========================================
# GET ALL FAMILY MEMBERS OF A PATIENT
# ==========================================

@router.get("/patient/{patient_id}")
def get_patient_family(patient_id: int):

    patient_family = [
        member
        for member in family_members
        if member["patient_id"] == patient_id
    ]

    return {
        "patient_id": patient_id,
        "total_family_members": len(patient_family),
        "family_members": patient_family
    }


# ==========================================
# GET SPECIFIC FAMILY MEMBER
# ==========================================

@router.get("/{member_id}")
def get_family_member(member_id: int):

    for member in family_members:

        if member["id"] == member_id:
            return member

    raise HTTPException(
        status_code=404,
        detail="Family member not found"
    )


# ==========================================
# DELETE FAMILY MEMBER
# ==========================================

@router.delete("/{member_id}")
def delete_family_member(member_id: int):

    for member in family_members:

        if member["id"] == member_id:

            family_members.remove(member)

            return {
                "message": "Family member removed successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Family member not found"
    )