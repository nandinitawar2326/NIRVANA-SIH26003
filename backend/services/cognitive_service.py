def analyze_cognitive_performance(game_history):

    if not game_history:
        return {
            "cognitive_score": 0,
            "status": "No data available",
            "recommendation": "Play cognitive games to generate analysis."
        }

    total_accuracy = sum(
        game["accuracy"] for game in game_history
    )

    average_accuracy = total_accuracy / len(game_history)

    total_time = sum(
        game["time_taken"] for game in game_history
    )

    average_time = total_time / len(game_history)

    # Calculate cognitive score
    cognitive_score = round(
        (average_accuracy * 0.8) +
        (min(100, 100 - average_time) * 0.2),
        2
    )

    # Determine status and recommendations
    if cognitive_score >= 80:
        status = "Good"
        recommended_difficulty = "Hard"
        recommendation = (
            "Excellent performance. Increase cognitive game difficulty."
        )

    elif cognitive_score >= 60:
        status = "Moderate"
        recommended_difficulty = "Medium"
        recommendation = (
            "Continue regular cognitive exercises."
        )

    else:
        status = "Needs Attention"
        recommended_difficulty = "Easy"
        recommendation = (
            "Focus on simpler personalized memory exercises."
        )

    # Caregiver alert
    caregiver_alert = cognitive_score < 50

    return {
        "cognitive_score": cognitive_score,
        "average_accuracy": round(average_accuracy, 2),
        "average_response_time": round(average_time, 2),
        "status": status,
        "recommended_difficulty": recommended_difficulty,
        "recommendation": recommendation,
        "caregiver_alert": caregiver_alert
    }