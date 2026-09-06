from adaptive_difficulty import choose_difficulty
from cognitive_score import calculate_cognitive_score, performance_level
from recommendation import recommend_activity
from predict_difficulty import predict_difficulty


def analyze_patient(
    game_type,
    level,
    accuracy,
    response_time,
    mistakes,
    score,
    memory,
    attention,
    recall,
    pattern
):
    """
    Main NIRVANA AI engine.

    Combines:
    1. ML-based adaptive difficulty
    2. Cognitive engagement scoring
    3. Personalized activity recommendation

    This is a prototype cognitive engagement system,
    NOT a medical diagnostic tool.
    """

    # -----------------------------------------
    # 1. ML DIFFICULTY PREDICTION
    # -----------------------------------------

    ml_difficulty, confidence = predict_difficulty(
        game_type=game_type,
        level=level,
        accuracy=accuracy,
        response_time=response_time,
        mistakes=mistakes,
        score=score
    )

    # -----------------------------------------
    # 2. RULE-BASED PERFORMANCE SCORE
    # -----------------------------------------

    performance, rule_based_difficulty = choose_difficulty(
        accuracy,
        response_time,
        mistakes
    )

    # -----------------------------------------
    # 3. COGNITIVE ENGAGEMENT SCORE
    # -----------------------------------------

    cognitive_score = calculate_cognitive_score(
        memory,
        attention,
        recall,
        pattern
    )

    level_name = performance_level(cognitive_score)

    # -----------------------------------------
    # 4. PERSONALIZED RECOMMENDATION
    # -----------------------------------------

    weakest_area, recommended_game = recommend_activity(
        memory,
        attention,
        recall,
        pattern
    )

    # -----------------------------------------
    # FINAL RESULT
    # -----------------------------------------

    return {
        "game_performance": performance,

        "rule_based_difficulty": rule_based_difficulty,

        "ml_predicted_difficulty": ml_difficulty,

        "ml_confidence": confidence,

        "cognitive_score": cognitive_score,

        "performance_level": level_name,

        "area_for_practice": weakest_area,

        "recommended_activity": recommended_game
    }


# -----------------------------------------
# TEST NIRVANA AI
# -----------------------------------------

if __name__ == "__main__":

    result = analyze_patient(
        game_type="memory",
        level=2,
        accuracy=85,
        response_time=15,
        mistakes=2,
        score=82,

        memory=78,
        attention=82,
        recall=55,
        pattern=70
    )

    print("\n========================================")
    print("        NIRVANA AI ENGINE")
    print("========================================")

    print("\nGAME PERFORMANCE")
    print("----------------------------------------")
    print(
        "Performance Score:",
        result["game_performance"]
    )

    print(
        "Rule-Based Difficulty:",
        result["rule_based_difficulty"]
    )

    print("\nML ADAPTIVE DIFFICULTY")
    print("----------------------------------------")
    print(
        "Predicted Difficulty:",
        result["ml_predicted_difficulty"]
    )

    print(
        "Prediction Confidence:",
        result["ml_confidence"],
        "%"
    )

    print("\nCOGNITIVE ENGAGEMENT")
    print("----------------------------------------")
    print(
        "Cognitive Score:",
        result["cognitive_score"]
    )

    print(
        "Performance Level:",
        result["performance_level"]
    )

    print("\nPERSONALIZED RECOMMENDATION")
    print("----------------------------------------")
    print(
        "Area for Practice:",
        result["area_for_practice"]
    )

    print(
        "Recommended Activity:",
        result["recommended_activity"]
    )