from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.database import get_db
from models.database_models import GameProgressDB
from models.game_session import GameScore


router = APIRouter(
    prefix="/cognitive",
    tags=["Cognitive Games"]
)


# ==========================================
# SAVE GAME SCORE
# ==========================================

@router.post("/game-score")
def save_game_score(
    game: GameScore,
    db: Session = Depends(get_db)
):

    new_game_score = GameProgressDB(

        patient_id=game.patient_id,

        game_name=game.game_name,

        score=game.score,

        accuracy=str(game.accuracy),

        time_taken=str(game.time_taken),

        difficulty=game.difficulty
    )


    db.add(new_game_score)

    db.commit()

    db.refresh(new_game_score)


    return {

        "message": "Game score saved successfully",

        "data": {

            "id": new_game_score.id,

            "patient_id": new_game_score.patient_id,

            "game_name": new_game_score.game_name,

            "score": new_game_score.score,

            "accuracy": new_game_score.accuracy,

            "time_taken": new_game_score.time_taken,

            "difficulty": new_game_score.difficulty,

            "created_at": new_game_score.created_at
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

    games = db.query(GameProgressDB).filter(
        GameProgressDB.patient_id == patient_id
    ).all()


    return {

        "patient_id": patient_id,

        "total_games": len(games),

        "games": games
    }


# ==========================================
# GET ALL GAME SCORES
# ==========================================

@router.get("/scores")
def get_all_game_scores(
    db: Session = Depends(get_db)
):

    games = db.query(GameProgressDB).all()


    return {

        "total_games": len(games),

        "games": games
    }