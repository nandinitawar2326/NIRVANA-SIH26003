from adaptive_difficulty import choose_difficulty
from cognitive_score import calculate_cognitive_score, performance_level
from recommendation import recommend_activity


def analyze_patient(
    accuracy,
    response_time,
    mistakes,
    memory,
    attention,
    recall,
    pattern
):
    """
    Main NIRVANA AI engine.

    Combines:
    1. Adaptive difficulty
    2. Cognitive engagement scoring
    3. Personalized activity recommendation

    This is a prototype cognitive engagement system,
    NOT a medical diagnostic tool.
    """

    # 1. Calculate game performance
    performance, difficulty = choose_difficulty(
        accuracy,
        response_time,
        mistakes
    )

    # 2. Calculate cognitive engagement score
    cognitive_score = calculate_cognitive_score(
        memory,
        attention,
        recall,
        pattern
    )

    # 3. Determine performance level
    level = performance_level(cognitive_score)

    # 4. Recommend next activity
    weakest_area, recommended_game = recommend_activity(
        memory,
        attention,
        recall,
        pattern
    )

    # Return all AI results
    return {
        "game_performance": performance,
        "next_difficulty": difficulty,
        "cognitive_score": cognitive_score,
        "performance_level": level,
        "area_for_practice": weakest_area,
        "recommended_activity": recommended_game
    }


# -----------------------------
# TEST NIRVANA AI
# -----------------------------

result = analyze_patient(
    accuracy=90,
    response_time=12,
    mistakes=1,
    memory=78,
    attention=82,
    recall=55,
    pattern=70
)

print("\n===== NIRVANA AI ANALYSIS =====")

print("Game Performance:", result["game_performance"])
print("Next Difficulty:", result["next_difficulty"])
print("Cognitive Score:", result["cognitive_score"])
print("Performance Level:", result["performance_level"])
print("Area for Practice:", result["area_for_practice"])
print("Recommended Activity:", result["recommended_activity"])