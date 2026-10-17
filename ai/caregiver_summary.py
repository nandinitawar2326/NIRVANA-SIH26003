from patient_analysis import analyze_patient
from progress_analysis import analyze_progress


def generate_caregiver_summary(user_id):
    """
    Generate a simple caregiver-friendly summary
    from game performance and progress data.

    This is a prototype cognitive engagement summary,
    NOT a medical diagnosis.
    """

    profile = analyze_patient(user_id)
    progress = analyze_progress(user_id)

    if "error" in profile:
        return profile

    if "error" in progress:
        return progress

    # -----------------------------------------
    # FIND IMPORTANT PERFORMANCE INFORMATION
    # -----------------------------------------

    weakest_area = profile["weakest_area"]

    cognitive_score = profile["cognitive_score"]

    performance_level = profile["performance_level"]

    overall_trend = progress["overall_trend"]

    score_change = progress["score_change"]

    accuracy_change = progress["accuracy_change"]

    # -----------------------------------------
    # FIND DECLINING / STABLE / IMPROVING AREAS
    # -----------------------------------------

    declining = []
    improving = []
    stable = []

    for game in progress["game_progress"]:

        game_name = game["game_type"].capitalize()

        if game["trend"] == "Declining":
            declining.append(game_name)

        elif game["trend"] == "Improving":
            improving.append(game_name)

        else:
            stable.append(game_name)

    # -----------------------------------------
    # CREATE CAREGIVER MESSAGE
    # -----------------------------------------

    summary_parts = []

    summary_parts.append(
        f"Patient {user_id} completed "
        f"{profile['total_sessions']} cognitive game sessions."
    )

    summary_parts.append(
        f"Current cognitive engagement score is "
        f"{cognitive_score}, classified as "
        f"{performance_level}."
    )

    summary_parts.append(
        f"Overall game-performance trend is "
        f"{overall_trend.lower()} "
        f"(score change: {score_change})."
    )

    summary_parts.append(
        f"The area currently needing more practice is "
        f"{weakest_area}."
    )

    if declining:
        summary_parts.append(
            "Declining game areas: "
            + ", ".join(declining)
            + "."
        )

    if improving:
        summary_parts.append(
            "Improving game areas: "
            + ", ".join(improving)
            + "."
        )

    if stable:
        summary_parts.append(
            "Stable game areas: "
            + ", ".join(stable)
            + "."
        )

    summary_parts.append(
        "The next cognitive session should prioritize "
        f"{weakest_area} while continuing practice "
        "in other cognitive areas."
    )

    summary = " ".join(summary_parts)

    return {
        "user_id": user_id,
        "summary": summary,
        "cognitive_score": cognitive_score,
        "performance_level": performance_level,
        "overall_trend": overall_trend,
        "weakest_area": weakest_area,
        "score_change": score_change,
        "accuracy_change": accuracy_change,
        "declining_areas": declining,
        "improving_areas": improving,
        "stable_areas": stable
    }


# =========================================
# TEST
# =========================================

if __name__ == "__main__":

    result = generate_caregiver_summary("U001")

    print("\n========================================")
    print("       NIRVANA CAREGIVER AI SUMMARY")
    print("========================================")

    if "error" in result:

        print(result["error"])

    else:

        print("\nPatient ID:", result["user_id"])

        print("\nCOGNITIVE STATUS")
        print("----------------------------------------")

        print(
            "Cognitive Score:",
            result["cognitive_score"]
        )

        print(
            "Performance Level:",
            result["performance_level"]
        )

        print(
            "Overall Trend:",
            result["overall_trend"]
        )

        print(
            "Weakest Area:",
            result["weakest_area"]
        )

        print("\nPERFORMANCE CHANGES")
        print("----------------------------------------")

        print(
            "Score Change:",
            result["score_change"]
        )

        print(
            "Accuracy Change:",
            result["accuracy_change"],
            "%"
        )

        print("\nCARE GIVER SUMMARY")
        print("----------------------------------------")

        print(result["summary"])