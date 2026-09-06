from patient_analysis import analyze_patient
from predict_difficulty import predict_difficulty


def create_daily_journey(user_id):
    """
    Create a personalized cognitive game journey.

    The journey uses:
    1. Patient's historical performance
    2. Weakest cognitive domain
    3. ML-based difficulty prediction

    This is a prototype cognitive engagement system,
    NOT a medical diagnostic tool.
    """

    profile = analyze_patient(user_id)

    if "error" in profile:
        return profile

    weakest_area = profile["weakest_area"].lower()

    # Map cognitive domains to games
    game_mapping = {
        "memory": "Memory Match",
        "attention": "Attention Game",
        "recall": "Daily Routine Recall",
        "pattern": "Pattern Completion"
    }

    # Map domain names to dataset game_type values
    game_type_mapping = {
        "memory": "memory",
        "attention": "attention",
        "recall": "recall",
        "pattern": "pattern"
    }

    journey = []

    # Put weakest domain first
    domains = [
        weakest_area,
        "memory",
        "attention",
        "recall",
        "pattern"
    ]

    # Remove duplicates while preserving order
    domains = list(dict.fromkeys(domains))

    for domain in domains:

        # Get historical data for this domain
        game_data = profile["game_performance"]

        game_type = game_type_mapping[domain]

        if game_type in game_data.index:

            row = game_data.loc[game_type]

            accuracy = row["average_accuracy"]
            response_time = row["average_response_time"]
            mistakes = row["total_mistakes"]

            # Use average score as the performance score
            score = row["average_score"]

        else:

            # Default values for a new/unplayed game
            accuracy = 70
            response_time = 20
            mistakes = 3
            score = 70

        # Current level starts at 1 for the prototype
        level = 1

        # Ask the trained ML model for difficulty
        difficulty, confidence = predict_difficulty(
            game_type=game_type,
            level=level,
            accuracy=accuracy,
            response_time=response_time,
            mistakes=mistakes,
            score=score
        )

        # Higher priority for weakest area
        if domain == weakest_area:
            priority = "High"
            duration = 3
        else:
            priority = "Normal"
            duration = 2

        journey.append({
            "game": game_mapping[domain],
            "domain": domain.capitalize(),
            "difficulty": difficulty,
            "confidence": confidence,
            "duration": duration,
            "priority": priority
        })

    return {
        "user_id": user_id,
        "cognitive_score": profile["cognitive_score"],
        "performance_level": profile["performance_level"],
        "weakest_area": weakest_area.capitalize(),
        "journey": journey
    }


if __name__ == "__main__":

    result = create_daily_journey("U001")

    print("\n========================================")
    print("       NIRVANA DAILY COGNITIVE JOURNEY")
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
            "Focus Area:",
            result["weakest_area"]
        )

        print("\nTODAY'S PERSONALIZED JOURNEY")
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
                f"   Duration: {activity['duration']} minutes"
            )

            print(
                f"   Priority: {activity['priority']}"
            )

            print()