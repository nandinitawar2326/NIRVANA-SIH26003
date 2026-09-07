from sqlalchemy.orm import Session

from models.database_models import GameScoreDB


def analyze_progress(user_id, db: Session):

    """
    Analyze patient performance changes
    using REAL database sessions.
    """

    patient_id = int(user_id)


    # -----------------------------------------
    # GET GAME HISTORY
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
            "error": "No game sessions found."
        }


    # -----------------------------------------
    # OVERALL SCORE
    # -----------------------------------------

    first_score = games[0].score

    latest_score = games[-1].score


    score_change = round(
        latest_score - first_score,
        2
    )


    # -----------------------------------------
    # ACCURACY
    # -----------------------------------------

    first_accuracy = games[0].accuracy or 0

    latest_accuracy = games[-1].accuracy or 0


    accuracy_change = round(

        latest_accuracy - first_accuracy,

        2
    )


    # -----------------------------------------
    # OVERALL TREND
    # -----------------------------------------

    if score_change >= 5:

        trend = "Improving"

    elif score_change <= -5:

        trend = "Declining"

    else:

        trend = "Stable"


    # -----------------------------------------
    # GAME-WISE PROGRESS
    # -----------------------------------------

    game_groups = {}


    for game in games:

        name = game.game_name


        if name not in game_groups:

            game_groups[name] = []


        game_groups[name].append(game)


    game_progress = []


    for game_name, sessions in game_groups.items():

        first_game_score = sessions[0].score

        latest_game_score = sessions[-1].score


        change = round(

            latest_game_score - first_game_score,

            2
        )


        if change >= 5:

            game_trend = "Improving"

        elif change <= -5:

            game_trend = "Declining"

        else:

            game_trend = "Stable"


        game_progress.append({

            "game_type": game_name,

            "first_score": first_game_score,

            "latest_score": latest_game_score,

            "change": change,

            "trend": game_trend
        })


    return {

        "user_id": str(user_id),

        "total_sessions": len(games),

        "first_score": first_score,

        "latest_score": latest_score,

        "score_change": score_change,

        "accuracy_change": accuracy_change,

        "overall_trend": trend,

        "game_progress": game_progress
    }