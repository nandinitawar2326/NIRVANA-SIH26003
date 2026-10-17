from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.memory import Memory
from models.database_models import MemoryDB
from services.database import get_db


# Create router
router = APIRouter(
    prefix="/memories",
    tags=["Memory Assistance"]
)


# ==========================================
# ADD A MEMORY
# ==========================================

@router.post("/")
def create_memory(
    memory: Memory,
    db: Session = Depends(get_db)
):

    new_memory = MemoryDB(
        patient_id=memory.patient_id,
        title=memory.title,
        description=memory.description,
        memory_date=memory.memory_date
    )

    db.add(new_memory)
    db.commit()
    db.refresh(new_memory)

    return {
        "message": "Memory added successfully",
        "memory": {
            "id": new_memory.id,
            "patient_id": new_memory.patient_id,
            "title": new_memory.title,
            "description": new_memory.description,
            "memory_date": new_memory.memory_date,
            "created_at": new_memory.created_at
        }
    }


# ==========================================
# GET ALL MEMORIES OF A PATIENT
# ==========================================

@router.get("/patient/{patient_id}")
def get_patient_memories(
    patient_id: int,
    db: Session = Depends(get_db)
):

    memories = (
        db.query(MemoryDB)
        .filter(MemoryDB.patient_id == patient_id)
        .order_by(MemoryDB.created_at.desc())
        .all()
    )

    return {
        "patient_id": patient_id,
        "total_memories": len(memories),
        "memories": memories
    }


# ==========================================
# GET ONE MEMORY
# ==========================================

@router.get("/{memory_id}")
def get_memory(
    memory_id: int,
    db: Session = Depends(get_db)
):

    memory = (
        db.query(MemoryDB)
        .filter(MemoryDB.id == memory_id)
        .first()
    )

    if not memory:
        raise HTTPException(
            status_code=404,
            detail="Memory not found"
        )

    return memory


# ==========================================
# DELETE MEMORY
# ==========================================

@router.delete("/{memory_id}")
def delete_memory(
    memory_id: int,
    db: Session = Depends(get_db)
):

    memory = (
        db.query(MemoryDB)
        .filter(MemoryDB.id == memory_id)
        .first()
    )

    if not memory:
        raise HTTPException(
            status_code=404,
            detail="Memory not found"
        )

    db.delete(memory)
    db.commit()

    return {
        "message": "Memory deleted successfully"
    }