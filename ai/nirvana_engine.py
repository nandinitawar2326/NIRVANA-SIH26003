from patient_analysis import analyze_patient
from progress_analysis import analyze_progress
from daily_journey import create_daily_journey
from caregiver_summary import generate_caregiver_summary


def run_nirvana(user_id):
    """
    Unified NIRVANA AI engine.

    Combines:
    1. Patient cognitive profile
    2. Performance progress
    3. Adaptive daily journey
    4. Caregiver summary

    This is a prototype cognitive engagement system,
    NOT a medical diagnostic tool.
    """

    # -----------------------------------------
    # PATIENT PROFILE
    # -----------------------------------------

    profile = analyze_patient(user_id)

    if "error" in profile:
        return profile

    # -----------------------------------------
    # PROGRESS
    # -----------------------------------------

    progress = analyze_progress(user_id)

    if "error" in progress:
        return progress

    # -----------------------------------------
    # DAILY JOURNEY
    # -----------------------------------------

    journey = create_daily_journey(user_id)

    if "error" in journey:
        return journey

    # -----------------------------------------
    # CAREGIVER SUMMARY
    # -----------------------------------------

    caregiver = generate_caregiver_summary(user_id)

    if "error" in caregiver:
        return caregiver

    # -----------------------------------------
    # UNIFIED RESULT
    # -----------------------------------------

    return {
        "patient": {
            "user_id": user_id,
            "total_sessions": profile["total_sessions"],
            "cognitive_score": profile["cognitive_score"],
            "performance_level": profile["performance_level"],
            "weakest_area": profile["weakest_area"]
        },

        "progress": {
            "overall_trend": progress["overall_trend"],
            "score_change": progress["score_change"],
            "accuracy_change": progress["accuracy_change"]
        },

        "daily_journey": journey["journey"],

        "caregiver_summary": caregiver["summary"]
    }


if __name__ == "__main__":

    result = run_nirvana("U001")

    print("\n========================================")
    print("          NIRVANA AI ENGINE")
    print("========================================")

    if "error" in result:

        print(result["error"])

    else:

        patient = result["patient"]
        progress = result["progress"]

        print("\nPATIENT PROFILE")
        print("----------------------------------------")

        print(
            "Patient ID:",
            patient["user_id"]
        )

        print(
            "Sessions:",
            patient["total_sessions"]
        )

        print(
            "Cognitive Score:",
            patient["cognitive_score"]
        )

        print(
            "Performance:",
            patient["performance_level"]
        )

        print(
            "Weakest Area:",
            patient["weakest_area"]
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
            progress["accuracy_change"],
            "%"
        )

        print("\nDAILY JOURNEY")
        print("----------------------------------------")

        for i, activity in enumerate(
            result["daily_journey"],
            start=1
        ):

            print(
                f"{i}. {activity['game']} "
                f"→ {activity['difficulty']} "
                f"({activity['priority']})"
            )

        print("\nCAREGIVER SUMMARY")
        print("----------------------------------------")

        print(
            result["caregiver_summary"]
        )