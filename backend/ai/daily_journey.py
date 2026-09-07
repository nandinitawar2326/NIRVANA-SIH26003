from ai.patient_analysis import analyze_patient
from ai.predict_difficulty import predict_difficulty
from ai.progress_analysis import analyze_progress


def create_daily_journey(user_id, db):

    """
    Create a personalized cognitive game journey.

    Prototype cognitive engagement system.
    NOT a medical diagnosis.
    """

    # -----------------------------------------
    # GET PATIENT PROFILE
    # -----------------------------------------

    profile = analyze_patient(user_id, db)

    if "error" in profile:
        return profile

    # -----------------------------------------
    # GET PROGRESS
    # -----------------------------------------

    progress = analyze_progress(user_id, db)

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

    domains = [

        "memory",

        "attention",

        "recall",

        "pattern"
    ]

    # -----------------------------------------
    # GET TRENDS
    # -----------------------------------------

    trends = {}

    for game in progress["game_progress"]:

        trends[
            game["game_type"].lower()
        ] = game["trend"]

    # -----------------------------------------
    # PRIORITY SCORES
    # -----------------------------------------

    priority_scores = {}

    for domain in domains:

        priority = 0

        # Weakest cognitive area gets priority
        if domain == weakest_area:

            priority += 3

        # Declining performance gets extra priority
        if trends.get(domain) == "Declining":

            priority += 2

        elif trends.get(domain) == "Stable":

            priority += 1

        priority_scores[domain] = priority

    # -----------------------------------------
    # SORT DOMAINS BY PRIORITY
    # -----------------------------------------

    sorted_domains = sorted(

        domains,

        key=lambda x: priority_scores[x],

        reverse=True
    )

    # -----------------------------------------
    # CONVERT PERFORMANCE LIST TO DICTIONARY
    # -----------------------------------------

    performance_lookup = {}

    for game in profile.get("game_performance", []):

        performance_lookup[
            game["game_type"].lower()
        ] = game

    # -----------------------------------------
    # BUILD DAILY JOURNEY
    # -----------------------------------------

    journey = []

    for domain in sorted_domains:

        game_info = performance_lookup.get(domain)

        # -------------------------------------
        # GET PERFORMANCE DATA
        # -------------------------------------

        if game_info:

            accuracy = float(
                game_info["average_accuracy"]
            )

            response_time = float(
                game_info["average_response_time"]
            )

            mistakes = int(
                game_info["total_mistakes"]
            )

            score = float(
                game_info["average_score"]
            )

        else:

            # Default values if no game data exists

            accuracy = 70.0

            response_time = 20.0

            mistakes = 3

            score = 70.0

        # -------------------------------------
        # AI DIFFICULTY PREDICTION
        # -------------------------------------

        prediction = predict_difficulty(

            game_type=domain,

            level=1,

            accuracy=accuracy,

            response_time=response_time,

            mistakes=mistakes,

            score=score
        )

        # Extract values from dictionary

        difficulty = prediction[
            "recommended_difficulty"
        ]

        confidence = prediction[
            "confidence"
        ]

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
        # GAME DURATION
        # -------------------------------------

        if priority == "High":

            duration = 3

        else:

            duration = 2

        # -------------------------------------
        # ADD GAME TO JOURNEY
        # -------------------------------------

        journey.append({

            "game": game_mapping[domain],

            "domain": domain.capitalize(),

            "difficulty": difficulty,

            "confidence": confidence,

            "duration": duration,

            "priority": priority,

            "trend": trends.get(
                domain,
                "Stable"
            )
        })

    # -----------------------------------------
    # FINAL RESPONSE
    # -----------------------------------------

    return {

        "user_id": str(user_id),

        "cognitive_score": profile[
            "cognitive_score"
        ],

        "performance_level": profile[
            "performance_level"
        ],

        "weakest_area": weakest_area.capitalize(),

        "overall_trend": progress[
            "overall_trend"
        ],

        "journey": journey
    }