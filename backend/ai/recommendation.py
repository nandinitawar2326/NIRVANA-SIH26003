def recommend_activity(memory, attention, recall, pattern):
    """
    Recommend the next cognitive activity.

    Prototype recommendation system.
    NOT a medical diagnosis.
    """

    scores = {
        "memory": memory,
        "attention": attention,
        "recall": recall,
        "pattern": pattern
    }

    weakest_area = min(scores, key=scores.get)

    recommendations = {
        "memory": "Memory Match",
        "attention": "Attention Game",
        "recall": "Daily Routine Recall",
        "pattern": "Pattern Completion"
    }

    recommended_game = recommendations[weakest_area]

    return weakest_area, recommended_game