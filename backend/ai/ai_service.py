from ai.predict_difficulty import (
    predict_difficulty
)


def get_ai_difficulty(
    game_type,
    level,
    accuracy,
    response_time,
    mistakes,
    score
):

    difficulty, confidence = predict_difficulty(

        game_type=game_type,

        level=level,

        accuracy=accuracy,

        response_time=response_time,

        mistakes=mistakes,

        score=score
    )

    return {

        "recommended_difficulty": difficulty,

        "confidence": confidence
    }