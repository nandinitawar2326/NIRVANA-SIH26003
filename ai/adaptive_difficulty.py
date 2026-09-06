def choose_difficulty(accuracy, response_time, mistakes):

    # Convert response time into a speed score
    speed_score = max(0, 100 - (response_time * 2))

    # Convert mistakes into a mistake score
    mistake_score = max(0, 100 - (mistakes * 10))

    # Calculate overall performance
    performance = (
        accuracy * 0.5
        + speed_score * 0.3
        + mistake_score * 0.2
    )

    # Decide the next difficulty
    if performance >= 80:
        difficulty = "hard"

    elif performance >= 60:
        difficulty = "medium"

    else:
        difficulty = "easy"

    return round(performance, 2), difficulty


# Test the AI
score, difficulty = choose_difficulty(
    accuracy=90,
    response_time=12,
    mistakes=1
)

print("Performance Score:", score)
print("Recommended Difficulty:", difficulty)