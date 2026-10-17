from ai.patient_analysis import analyze_patient

from ai.progress_analysis import analyze_progress


def generate_caregiver_summary(user_id, db):

    """
    Generate a caregiver-friendly summary.

    Prototype cognitive engagement summary.
    NOT a medical diagnosis.
    """

    profile = analyze_patient(user_id, db)

    if "error" in profile:
        return profile

    progress = analyze_progress(user_id, db)

    if "error" in progress:
        return progress

    weakest_area = profile[
        "weakest_area"
    ]

    cognitive_score = profile[
        "cognitive_score"
    ]

    performance = profile[
        "performance_level"
    ]

    overall_trend = progress[
        "overall_trend"
    ]

    declining = []
    improving = []
    stable = []

    for game in progress[
        "game_progress"
    ]:

        game_name = game[
            "game_type"
        ].capitalize()

        if game["trend"] == "Declining":

            declining.append(
                game_name
            )

        elif game["trend"] == "Improving":

            improving.append(
                game_name
            )

        else:

            stable.append(
                game_name
            )

    summary_parts = []

    summary_parts.append(

        f"Patient {user_id} completed "
        f"{profile['total_sessions']} "
        f"cognitive game sessions."
    )

    summary_parts.append(

        f"Current cognitive engagement score is "
        f"{cognitive_score}, classified as "
        f"{performance}."
    )

    summary_parts.append(

        f"Overall performance trend is "
        f"{overall_trend.lower()}."
    )

    summary_parts.append(

        f"The area currently needing more "
        f"practice is {weakest_area}."
    )

    if declining:

        summary_parts.append(

            "Areas showing decline: "

            + ", ".join(declining)

            + "."
        )

    if improving:

        summary_parts.append(

            "Areas showing improvement: "

            + ", ".join(improving)

            + "."
        )

    if stable:

        summary_parts.append(

            "Stable areas: "

            + ", ".join(stable)

            + "."
        )

    summary_parts.append(

        f"The next session should prioritize "
        f"{weakest_area} activities."
    )

    summary = " ".join(
        summary_parts
    )

    return {

        "user_id": str(user_id),

        "summary": summary,

        "cognitive_score": cognitive_score,

        "performance_level": performance,

        "overall_trend": overall_trend,

        "weakest_area": weakest_area,

        "score_change": progress[
            "score_change"
        ],

        "accuracy_change": progress[
            "accuracy_change"
        ],

        "declining_areas": declining,

        "improving_areas": improving,

        "stable_areas": stable
    }