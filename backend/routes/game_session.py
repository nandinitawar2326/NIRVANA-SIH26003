from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from services.database import get_db
from models.game_session import GameScore
from models.database_models import GameScoreDB, GameProgressDB


router = APIRouter(
    prefix="/game-session",
    tags=["Game Session"]
)


# ==========================================
# SAVE GAME SESSION
# ==========================================

@router.post("/")
def save_game_score(
    game: GameScore,
    db: Session = Depends(get_db)
):

    # ------------------------------------------
    # SAVE INDIVIDUAL GAME SESSION
    # ------------------------------------------

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


    # ------------------------------------------
    # UPDATE GAME PROGRESS
    # ------------------------------------------

    progress = (
        db.query(GameProgressDB)
        .filter(
            GameProgressDB.patient_id == game.patient_id,
            GameProgressDB.game_name == game.game_name
        )
        .first()
    )


    # Create progress if this is the first game
    if not progress:

        progress = GameProgressDB(
            patient_id=game.patient_id,
            game_name=game.game_name,
            level=1,
            highest_score=game.score,
            total_games=1
        )

        db.add(progress)


    # Update existing progress
    else:

        progress.total_games += 1

        if game.score > progress.highest_score:
            progress.highest_score = game.score


    # ------------------------------------------
    # SAVE DATABASE CHANGES
    # ------------------------------------------

    db.commit()

    db.refresh(new_game_score)


    return {
        "message": "Game session saved successfully",

        "game": {
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
# GET PATIENT GAME HISTORY
# ==========================================

@router.get("/history/{patient_id}")
def get_game_history(
    patient_id: int,
    db: Session = Depends(get_db)
):

    games = (
        db.query(GameScoreDB)
        .filter(
            GameScoreDB.patient_id == patient_id
        )
        .order_by(
            GameScoreDB.played_at.desc()
        )
        .all()
    )


    if not games:

        raise HTTPException(
            status_code=404,
            detail="No game history found for this patient"
        )


    return {
        "patient_id": patient_id,
        "total_games": len(games),
        "games": games
    }


# ==========================================
# GET GAME PROGRESS
# ==========================================

@router.get("/progress/{patient_id}")
def get_game_progress(
    patient_id: int,
    db: Session = Depends(get_db)
):

    progress = (
        db.query(GameProgressDB)
        .filter(
            GameProgressDB.patient_id == patient_id
        )
        .all()
    )


    if not progress:

        raise HTTPException(
            status_code=404,
            detail="No game progress found for this patient"
        )


    return {
        "patient_id": patient_id,
        "games": progress
    }