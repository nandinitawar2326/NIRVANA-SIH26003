def recommend_activity(memory, attention, recall, pattern):
    """
    Recommend the next cognitive activity based on
    the user's current performance.

    This is a prototype recommendation system,
    NOT a medical diagnosis.
    """

    scores = {
        "Memory": memory,
        "Attention": attention,
        "Recall": recall,
        "Pattern": pattern
    }

    # Find the weakest cognitive area
    weakest_area = min(scores, key=scores.get)

    recommendations = {
        "Memory": "Memory Match",
        "Attention": "Attention Game",
        "Recall": "Daily Routine Recall",
        "Pattern": "Pattern Completion"
    }

    recommended_game = recommendations[weakest_area]

    return weakest_area, recommended_game


# Test the recommendation system
weakest_area, game = recommend_activity(
    memory=78,
    attention=82,
    recall=55,
    pattern=70
)

print("Area needing more practice:", weakest_area)
print("Recommended Next Activity:", game)