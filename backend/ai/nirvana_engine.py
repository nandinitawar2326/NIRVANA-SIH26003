from ai.patient_analysis import analyze_patient
from ai.progress_analysis import analyze_progress
from ai.daily_journey import create_daily_journey
from ai.caregiver_summary import generate_caregiver_summary


def analyze_patient_complete(user_id: str):
    """
    Unified NIRVANA AI Engine.

    Combines:
    1. Patient cognitive profile
    2. Performance progress
    3. Adaptive daily journey
    4. Caregiver summary

    This is a prototype cognitive engagement system
    and NOT a medical diagnostic tool.
    """

    # =========================================
    # PATIENT PROFILE
    # =========================================

    profile = analyze_patient(user_id)

    if "error" in profile:
        return profile

    # =========================================
    # PROGRESS ANALYSIS
    # =========================================

    progress = analyze_progress(user_id)

    if "error" in progress:
        return progress

    # =========================================
    # DAILY JOURNEY
    # =========================================

    journey = create_daily_journey(user_id)

    if "error" in journey:
        return journey

    # =========================================
    # CAREGIVER SUMMARY
    # =========================================

    caregiver = generate_caregiver_summary(user_id)

    if "error" in caregiver:
        return caregiver

    # =========================================
    # FINAL UNIFIED RESULT
    # =========================================

    return {

        "patient": {
            "user_id": str(user_id),
            "total_sessions": int(profile["total_sessions"]),
            "cognitive_score": float(profile["cognitive_score"]),
            "performance_level": str(profile["performance_level"]),
            "weakest_area": str(profile["weakest_area"]),
            "recommended_activity": str(
                profile["recommended_activity"]
            ),
            "domain_scores": profile["domain_scores"]
        },

        "progress": {
            "overall_trend": str(
                progress["overall_trend"]
            ),
            "score_change": float(
                progress["score_change"]
            ),
            "accuracy_change": float(
                progress["accuracy_change"]
            ),
            "total_sessions": int(
                progress["total_sessions"]
            ),
            "game_progress": progress["game_progress"]
        },

        "daily_journey": journey["journey"],

        "caregiver_summary": caregiver["summary"]
    }


# =========================================
# BACKWARD COMPATIBILITY
# =========================================

def analyze_patient_data(user_id: str):
    """
    Alternative function name for compatibility
    with API routes.
    """
    return analyze_patient_complete(user_id)


# =========================================
# TEST
# =========================================

if __name__ == "__main__":

    result = analyze_patient_complete("U001")

    print("\n========================================")
    print("          NIRVANA AI ENGINE")
    print("========================================")

    if "error" in result:

        print("\nERROR:")
        print(result["error"])

    else:

        patient = result["patient"]
        progress = result["progress"]

        print("\nPATIENT PROFILE")
        print("----------------------------------------")

        print("Patient ID:", patient["user_id"])

        print("Total Sessions:", patient["total_sessions"])

        print(
            "Cognitive Score:",
            patient["cognitive_score"]
        )

        print(
            "Performance Level:",
            patient["performance_level"]
        )

        print(
            "Weakest Area:",
            patient["weakest_area"]
        )

        print(
            "Recommended Activity:",
            patient["recommended_activity"]
        )

        print("\nDOMAIN SCORES")
        print("----------------------------------------")

        for domain, score in patient[
            "domain_scores"
        ].items():

            print(
                f"{domain.capitalize()}: {score}"
            )

        print("\nPROGRESS")
        print("----------------------------------------")

        print(
            "Overall Trend:",
            progress["overall_trend"]
        )

        print(
            "Score Change:",
            progress["score_change"]
        )

        print(
            "Accuracy Change:",
            progress["accuracy_change"]
        )

        print("\nDAILY JOURNEY")
        print("----------------------------------------")

        for index, activity in enumerate(
            result["daily_journey"],
            start=1
        ):

            print(
                f"{index}. "
                f"{activity.get('game')} → "
                f"{activity.get('difficulty')} "
                f"({activity.get('priority')})"
            )

        print("\nCAREGIVER SUMMARY")
        print("----------------------------------------")

        print(
            result["caregiver_summary"]
        )

        print("\n========================================")