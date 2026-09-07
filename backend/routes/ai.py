from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from services.database import get_db
from ai.nirvana_ai import analyze_patient_complete


router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)


class AIAnalysisRequest(BaseModel):

    user_id: str


@router.post("/analyze")
def analyze_game(
    data: AIAnalysisRequest,
    db: Session = Depends(get_db)
):

    result = analyze_patient_complete(
        data.user_id,
        db
    )

    return {
        "status": "success",
        "analysis": result
    }