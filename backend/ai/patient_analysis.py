from sqlalchemy.orm import Session

from models.database_models import GameScoreDB

from ai.cognitive_score import (
    calculate_cognitive_score,
    performance_level
)

from ai.recommendation import recommend_activity


# ==========================================
# GAME → COGNITIVE DOMAIN
# ==========================================

GAME_DOMAIN_MAPPING = {

    "memory match": "memory",

    "what do you see?": "attention",
    "what do you see": "attention",

    "complete the pattern": "pattern",

    "familiar faces": "recall"
}


# ==========================================
# ANALYZE PATIENT
# ==========================================

def analyze_patient(user_id, db: Session):

    """
    Generate cognitive performance profile
    using REAL database game sessions.

    Prototype cognitive engagement system.
    NOT a medical diagnosis.
    """

    patient_id = int(user_id)

    # -----------------------------------------
    # GET GAME SESSIONS FROM DATABASE
    # -----------------------------------------

    games = (
        db.query(GameScoreDB)
        .filter(
            GameScoreDB.patient_id == patient_id
        )
        .order_by(
            GameScoreDB.played_at.asc()
        )
        .all()
    )


    if not games:

        return {
            "error": "No game sessions found for this patient."
        }


    # -----------------------------------------
    # DOMAIN DATA
    # -----------------------------------------

    domain_data = {

        "memory": [],
        "attention": [],
        "recall": [],
        "pattern": []
    }


    # -----------------------------------------
    # READ GAME SCORES
    # -----------------------------------------

    for game in games:

        game_name = game.game_name.lower().strip()

        domain = GAME_DOMAIN_MAPPING.get(
            game_name
        )


        if domain:

            domain_data[domain].append(
                game.score
            )


    # -----------------------------------------
    # DOMAIN SCORES
    # -----------------------------------------

    domain_scores = {}


    for domain, scores in domain_data.items():

        if scores:

            domain_scores[domain] = round(
                sum(scores) / len(scores),
                2
            )

        else:

            domain_scores[domain] = 0.0


    # -----------------------------------------
    # COGNITIVE SCORE
    # -----------------------------------------

    cognitive_score = calculate_cognitive_score(

        memory=domain_scores["memory"],

        attention=domain_scores["attention"],

        recall=domain_scores["recall"],

        pattern=domain_scores["pattern"]
    )


    # -----------------------------------------
    # PERFORMANCE LEVEL
    # -----------------------------------------

    level = performance_level(
        cognitive_score
    )


    # -----------------------------------------
    # RECOMMENDATION
    # -----------------------------------------

    weakest_area, recommended_game = recommend_activity(

        memory=domain_scores["memory"],

        attention=domain_scores["attention"],

        recall=domain_scores["recall"],

        pattern=domain_scores["pattern"]
    )


    return {

        "user_id": str(user_id),

        "total_sessions": len(games),

        "domain_scores": domain_scores,

        "cognitive_score": float(
            cognitive_score
        ),

        "performance_level": level,

        "weakest_area": weakest_area,

        "recommended_activity": recommended_game
    }