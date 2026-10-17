from patient_analysis import analyze_patient
from predict_difficulty import predict_difficulty
from progress_analysis import analyze_progress


def create_daily_journey(user_id):
    """
    Create a personalized cognitive game journey.

    Uses:
    1. Cognitive domain performance
    2. Weakest cognitive domain
    3. Performance trends
    4. ML-based difficulty prediction

    This is a prototype cognitive engagement system,
    NOT a medical diagnostic tool.
    """

    profile = analyze_patient(user_id)
    progress = analyze_progress(user_id)

    if "error" in profile:
        return profile

    if "error" in progress:
        return progress

    weakest_area = profile["weakest_area"].lower()

    # -----------------------------------------
    # GAME MAPPING
    # -----------------------------------------

    game_mapping = {
        "memory": "Memory Match",
        "attention": "Attention Game",
        "recall": "Daily Routine Recall",
        "pattern": "Pattern Completion"
    }

    game_type_mapping = {
        "memory": "memory",
        "attention": "attention",
        "recall": "recall",
        "pattern": "pattern"
    }

    # -----------------------------------------
    # GET GAME TRENDS
    # -----------------------------------------

    trends = {}

    for game in progress["game_progress"]:
        trends[game["game_type"]] = game["trend"]

    # -----------------------------------------
    # CREATE PRIORITY ORDER
    # -----------------------------------------

    domains = [
        "memory",
        "attention",
        "recall",
        "pattern"
    ]

    priority_scores = {}

    for domain in domains:

        priority = 0

        # Weakest domain gets highest priority
        if domain == weakest_area:
            priority += 3

        # Declining performance gets additional priority
        if trends.get(domain) == "Declining":
            priority += 2

        # Stable domains receive normal priority
        if trends.get(domain) == "Stable":
            priority += 1

        priority_scores[domain] = priority

    # Sort domains by priority
    domains = sorted(
        domains,
        key=lambda x: priority_scores[x],
        reverse=True
    )

    # -----------------------------------------
    # BUILD DAILY JOURNEY
    # -----------------------------------------

    journey = []

    game_data = profile["game_performance"]

    for domain in domains:

        game_type = game_type_mapping[domain]

        if game_type in game_data.index:

            row = game_data.loc[game_type]

            accuracy = row["average_accuracy"]
            response_time = row["average_response_time"]
            mistakes = row["total_mistakes"]
            score = row["average_score"]

        else:

            # Prototype defaults for unplayed games
            accuracy = 70
            response_time = 20
            mistakes = 3
            score = 70

        level = 1

        # -------------------------------------
        # ML DIFFICULTY PREDICTION
        # -------------------------------------

        difficulty, confidence = predict_difficulty(
            game_type=game_type,
            level=level,
            accuracy=accuracy,
            response_time=response_time,
            mistakes=mistakes,
            score=score
        )

        # -------------------------------------
        # PRIORITY
        # -------------------------------------

        if domain == weakest_area:
            priority = "High"

        elif trends.get(domain) == "Declining":
            priority = "High"

        else:
            priority = "Normal"

        # -------------------------------------
        # DURATION
        # -------------------------------------

        if priority == "High":
            duration = 3
        else:
            duration = 2

        journey.append({
            "game": game_mapping[domain],
            "domain": domain.capitalize(),
            "difficulty": difficulty,
            "confidence": confidence,
            "duration": duration,
            "priority": priority,
            "trend": trends.get(domain, "Stable")
        })

    # -----------------------------------------
    # RETURN RESULT
    # -----------------------------------------

    return {
        "user_id": user_id,
        "cognitive_score": profile["cognitive_score"],
        "performance_level": profile["performance_level"],
        "weakest_area": weakest_area.capitalize(),
        "overall_trend": progress["overall_trend"],
        "journey": journey
    }


# =========================================
# TEST
# =========================================

if __name__ == "__main__":

    result = create_daily_journey("U001")

    print("\n========================================")
    print("       NIRVANA ADAPTIVE DAILY JOURNEY")
    print("========================================")

    if "error" in result:

        print(result["error"])

    else:

        print("\nPatient ID:", result["user_id"])

        print(
            "Cognitive Score:",
            result["cognitive_score"]
        )

        print(
            "Performance Level:",
            result["performance_level"]
        )

        print(
            "Weakest Area:",
            result["weakest_area"]
        )

        print(
            "Overall Trend:",
            result["overall_trend"]
        )

        print("\nTODAY'S ADAPTIVE JOURNEY")
        print("----------------------------------------")

        for i, activity in enumerate(
            result["journey"],
            start=1
        ):

            print(
                f"{i}. {activity['game']}"
            )

            print(
                f"   Domain: {activity['domain']}"
            )

            print(
                f"   Difficulty: {activity['difficulty']}"
            )

            print(
                f"   ML Confidence: {activity['confidence']}%"
            )

            print(
                f"   Previous Trend: {activity['trend']}"
            )

            print(
                f"   Duration: {activity['duration']} minutes"
            )

            print(
                f"   Priority: {activity['priority']}"
            )

            print()