import pandas as pd


def analyze_patient(user_id):
    # Load game session data
    data = pd.read_csv("datasets/game_sessions.csv")

    # Select the patient's records
    patient_data = data[data["user_id"] == user_id]

    # Check if patient exists
    if patient_data.empty:
        print("Patient not found.")
        return

    print("\n===== PATIENT ANALYSIS =====")
    print("Patient ID:", user_id)
    print("Total game sessions:", len(patient_data))

    print("\n===== GAME PERFORMANCE =====")

    # Calculate performance for each game
    game_performance = patient_data.groupby("game_type").agg(
        average_accuracy=("accuracy", "mean"),
        average_score=("score", "mean"),
        average_response_time=("response_time", "mean"),
        total_mistakes=("mistakes", "sum")
    )

    print(game_performance.round(2))

    print("\n===== COGNITIVE PROFILE =====")

    # Map game types to cognitive domains
    domain_scores = {}

    for game in ["memory", "attention", "pattern", "recall"]:

        game_data = patient_data[
            patient_data["game_type"] == game
        ]

        if not game_data.empty:
            domain_scores[game] = round(
                game_data["score"].mean(), 2
            )
        else:
            domain_scores[game] = None

    for domain, score in domain_scores.items():
        print(f"{domain.capitalize()}: {score}")

    # Find weakest domain
    available_scores = {
        domain: score
        for domain, score in domain_scores.items()
        if score is not None
    }

    weakest_domain = min(
        available_scores,
        key=available_scores.get
    )

    print("\nArea needing more practice:",
          weakest_domain.capitalize())


# Test with patient U001
analyze_patient("U001")