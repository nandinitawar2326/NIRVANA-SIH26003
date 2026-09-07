def choose_difficulty(
    accuracy: float,
    response_time: float,
    mistakes: int
):
    """
    Calculate patient performance and recommend
    the next game difficulty level.

    Parameters:
        accuracy: Accuracy percentage (0-100)
        response_time: Time taken in seconds
        mistakes: Number of mistakes made

    Returns:
        tuple: (performance_score, recommended_difficulty)
    """

    # Ensure values are within valid ranges
    accuracy = max(0, min(float(accuracy), 100))
    response_time = max(0, float(response_time))
    mistakes = max(0, int(mistakes))

    # Speed score
    # Lower response time gives a higher score
    speed_score = max(0, 100 - (response_time * 2))

    # Mistake score
    mistake_score = max(0, 100 - (mistakes * 10))

    # Overall performance calculation
    performance = (
        accuracy * 0.5
        + speed_score * 0.3
        + mistake_score * 0.2
    )

    # Recommended difficulty
    if performance >= 80:
        difficulty = "hard"

    elif performance >= 60:
        difficulty = "medium"

    else:
        difficulty = "easy"

    return {
        "performance_score": round(performance, 2),
        "recommended_difficulty": difficulty,
        "accuracy": round(accuracy, 2),
        "speed_score": round(speed_score, 2),
        "mistake_score": round(mistake_score, 2)
    }


# Test this file directly
if __name__ == "__main__":

    result = choose_difficulty(
        accuracy=90,
        response_time=12,
        mistakes=1
    )

    print(result)