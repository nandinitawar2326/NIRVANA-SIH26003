import pandas as pd

from cognitive_score import calculate_cognitive_score
from cognitive_score import performance_level
from recommendation import recommend_activity


def analyze_patient(user_id):
    """
    Generate a cognitive performance profile
    from the patient's game sessions.

    This is a prototype cognitive engagement
    system and NOT a medical diagnosis.
    """

    data = pd.read_csv("datasets/game_sessions.csv")

    patient_data = data[data["user_id"] == user_id]

    if patient_data.empty:
        return {
            "error": "Patient not found."
        }

    # -----------------------------------------
    # GAME PERFORMANCE
    # -----------------------------------------

    game_performance = patient_data.groupby("game_type").agg(
        average_accuracy=("accuracy", "mean"),
        average_score=("score", "mean"),
        average_response_time=("response_time", "mean"),
        total_mistakes=("mistakes", "sum")
    ).round(2)

    # -----------------------------------------
    # COGNITIVE DOMAIN SCORES
    # -----------------------------------------

    domain_scores = {}

    for game in ["memory", "attention", "recall", "pattern"]:

        game_data = patient_data[
            patient_data["game_type"] == game
        ]

        if not game_data.empty:
            domain_scores[game] = round(
                game_data["score"].mean(), 2
            )
        else:
            domain_scores[game] = 0

    # -----------------------------------------
    # OVERALL COGNITIVE SCORE
    # -----------------------------------------

    cognitive_score = calculate_cognitive_score(
        memory=domain_scores["memory"],
        attention=domain_scores["attention"],
        recall=domain_scores["recall"],
        pattern=domain_scores["pattern"]
    )

    level = performance_level(cognitive_score)

    # -----------------------------------------
    # RECOMMENDATION
    # -----------------------------------------

    weakest_area, recommended_game = recommend_activity(
        memory=domain_scores["memory"],
        attention=domain_scores["attention"],
        recall=domain_scores["recall"],
        pattern=domain_scores["pattern"]
    )

    # -----------------------------------------
    # RESULT
    # -----------------------------------------

    return {
        "user_id": user_id,
        "total_sessions": len(patient_data),
        "domain_scores": domain_scores,
        "cognitive_score": cognitive_score,
        "performance_level": level,
        "weakest_area": weakest_area,
        "recommended_activity": recommended_game,
        "game_performance": game_performance
    }


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    result = analyze_patient("U001")

    print("\n========================================")
    print("       NIRVANA PATIENT ANALYSIS")
    print("========================================")

    if "error" in result:

        print(result["error"])

    else:

        print("\nPatient ID:", result["user_id"])

        print(
            "Total Game Sessions:",
            result["total_sessions"]
        )

        print("\nCOGNITIVE DOMAIN SCORES")
        print("----------------------------------------")

        for domain, score in result["domain_scores"].items():

            print(
                f"{domain.capitalize():<12}: {score}"
            )

        print("\nOVERALL COGNITIVE ENGAGEMENT")
        print("----------------------------------------")

        print(
            "Score:",
            result["cognitive_score"]
        )

        print(
            "Performance Level:",
            result["performance_level"]
        )

        print("\nPERSONALIZED RECOMMENDATION")
        print("----------------------------------------")

        print(
            "Weakest Area:",
            result["weakest_area"].capitalize()
        )

        print(
            "Recommended Activity:",
            result["recommended_activity"]
        )

        print("\nGAME PERFORMANCE")
        print("----------------------------------------")

        print(result["game_performance"])