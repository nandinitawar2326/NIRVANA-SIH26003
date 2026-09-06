def calculate_cognitive_score(memory, attention, recall, pattern):
    """
    Calculate an overall cognitive engagement score.

    This is a prototype game-performance score,
    NOT a medical diagnosis.
    """

    overall = (
        memory * 0.30 +
        attention * 0.25 +
        recall * 0.25 +
        pattern * 0.20
    )

    return round(overall, 2)


def performance_level(score):

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Needs Practice"

    else:
        return "Needs Support"


# Test the system
score = calculate_cognitive_score(
    memory=40,
    attention=55,
    recall=45,
    pattern=50
)

level = performance_level(score)

print("Overall Cognitive Engagement Score:", score)
print("Performance Level:", level)