from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from models.game_session import GameScore
from models.database_models import GameScoreDB
from services.database import get_db


router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


# ==========================================
# SAVE GAME SCORE
# ==========================================

@router.post("/score")
def add_game_score(
    game: GameScore,
    db: Session = Depends(get_db)
):

    new_game_score = GameScoreDB(
        patient_id=game.patient_id,
        game_name=game.game_name,
        score=game.score,
        accuracy=game.accuracy,
        time_taken=game.time_taken,
        difficulty=game.difficulty,
        played_at=game.played_at or datetime.utcnow()
    )

    db.add(new_game_score)
    db.commit()
    db.refresh(new_game_score)

    return {
        "message": "Game score saved successfully 🎮",

        "game_data": {
            "id": new_game_score.id,
            "patient_id": new_game_score.patient_id,
            "game_name": new_game_score.game_name,
            "score": new_game_score.score,
            "accuracy": new_game_score.accuracy,
            "time_taken": new_game_score.time_taken,
            "difficulty": new_game_score.difficulty,
            "played_at": new_game_score.played_at
        }
    }


# ==========================================
# GET GAME HISTORY
# ==========================================

@router.get("/history/{patient_id}")
def get_game_history(
    patient_id: int,
    db: Session = Depends(get_db)
):

    history = (
        db.query(GameScoreDB)
        .filter(GameScoreDB.patient_id == patient_id)
        .order_by(GameScoreDB.played_at.desc())
        .all()
    )

    if not history:

        raise HTTPException(
            status_code=404,
            detail="No game history found for this patient"
        )

    return {
        "patient_id": patient_id,
        "total_games": len(history),
        "history": history
    }


# ==========================================
# GET ALL GAME SCORES
# ==========================================

@router.get("/")
def get_all_game_scores(
    db: Session = Depends(get_db)
):

    games = db.query(GameScoreDB).all()

    return {
        "total_games": len(games),
        "games": games
    }