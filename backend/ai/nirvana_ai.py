from ai.patient_analysis import analyze_patient
from ai.progress_analysis import analyze_progress
from ai.daily_journey import create_daily_journey
from ai.caregiver_summary import generate_caregiver_summary


def analyze_patient_complete(user_id, db):

    """
    Unified NIRVANA AI engine.

    Prototype cognitive engagement system.
    NOT a medical diagnostic tool.
    """

    # -----------------------------------------
    # PATIENT PROFILE
    # -----------------------------------------

    profile = analyze_patient(
        user_id,
        db
    )

    if "error" in profile:
        return profile


    # -----------------------------------------
    # PROGRESS ANALYSIS
    # -----------------------------------------

    progress = analyze_progress(
        user_id,
        db
    )

    if "error" in progress:
        return progress


    # -----------------------------------------
    # DAILY JOURNEY
    # -----------------------------------------

    journey = create_daily_journey(
        user_id,
        db
    )

    if "error" in journey:
        return journey


    # -----------------------------------------
    # CAREGIVER SUMMARY
    # -----------------------------------------

    caregiver = generate_caregiver_summary(
        user_id,
        db
    )

    if "error" in caregiver:
        return caregiver


    # -----------------------------------------
    # UNIFIED RESPONSE
    # -----------------------------------------

    return {

        "patient": {

            "user_id": str(user_id),

            "total_sessions": profile["total_sessions"],

            "domain_scores": profile["domain_scores"],

            "cognitive_score": profile["cognitive_score"],

            "performance_level": profile["performance_level"],

            "weakest_area": profile["weakest_area"],

            "recommended_activity":
                profile["recommended_activity"]
        },


        "progress": {

            "overall_trend":
                progress["overall_trend"],

            "score_change":
                progress["score_change"],

            "accuracy_change":
                progress["accuracy_change"],

            "game_progress":
                progress["game_progress"]
        },


        "daily_journey":
            journey["journey"],


        "caregiver_summary":
            caregiver["summary"]
    }