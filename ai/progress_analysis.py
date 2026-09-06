import pandas as pd


def analyze_progress(user_id):
    """
    Analyze how a user's performance changes over time.

    This is a prototype cognitive engagement/
    game-performance analysis system,
    NOT a medical diagnostic tool.
    """

    data = pd.read_csv("datasets/game_sessions.csv")

    patient_data = data[
        data["user_id"] == user_id
    ].copy()

    if patient_data.empty:
        return {
            "error": "Patient not found."
        }

    # Preserve the order of recorded sessions
    patient_data["session_number"] = range(
        1,
        len(patient_data) + 1
    )

    # -----------------------------------------
    # OVERALL PERFORMANCE TREND
    # -----------------------------------------

    first_score = patient_data.iloc[0]["score"]
    last_score = patient_data.iloc[-1]["score"]

    score_change = round(
        last_score - first_score,
        2
    )

    # -----------------------------------------
    # ACCURACY TREND
    # -----------------------------------------

    first_accuracy = patient_data.iloc[0]["accuracy"]
    last_accuracy = patient_data.iloc[-1]["accuracy"]

    accuracy_change = round(
        last_accuracy - first_accuracy,
        2
    )

    # -----------------------------------------
    # PERFORMANCE TREND
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

    game_progress = []

    for game_type in patient_data["game_type"].unique():

        game_data = patient_data[
            patient_data["game_type"] == game_type
        ]

        first_game_score = game_data.iloc[0]["score"]
        last_game_score = game_data.iloc[-1]["score"]

        change = round(
            last_game_score - first_game_score,
            2
        )

        if change >= 5:
            game_trend = "Improving"

        elif change <= -5:
            game_trend = "Declining"

        else:
            game_trend = "Stable"

        game_progress.append({
            "game_type": game_type,
            "first_score": first_game_score,
            "latest_score": last_game_score,
            "change": change,
            "trend": game_trend
        })

    return {
        "user_id": user_id,
        "total_sessions": len(patient_data),
        "first_score": first_score,
        "latest_score": last_score,
        "score_change": score_change,
        "accuracy_change": accuracy_change,
        "overall_trend": trend,
        "game_progress": game_progress
    }


if __name__ == "__main__":

    result = analyze_progress("U001")

    print("\n========================================")
    print("       NIRVANA PROGRESS ANALYSIS")
    print("========================================")

    if "error" in result:

        print(result["error"])

    else:

        print("\nPatient ID:", result["user_id"])

        print(
            "Total Sessions:",
            result["total_sessions"]
        )

        print("\nOVERALL PROGRESS")
        print("----------------------------------------")

        print(
            "First Score:",
            result["first_score"]
        )

        print(
            "Latest Score:",
            result["latest_score"]
        )

        print(
            "Score Change:",
            result["score_change"]
        )

        print(
            "Accuracy Change:",
            result["accuracy_change"],
            "%"
        )

        print(
            "Overall Trend:",
            result["overall_trend"]
        )

        print("\nGAME-WISE PROGRESS")
        print("----------------------------------------")

        for game in result["game_progress"]:

            print(
                f"\n{game['game_type'].capitalize()}"
            )

            print(
                "First Score:",
                game["first_score"]
            )

            print(
                "Latest Score:",
                game["latest_score"]
            )

            print(
                "Change:",
                game["change"]
            )

            print(
                "Trend:",
                game["trend"]
            )