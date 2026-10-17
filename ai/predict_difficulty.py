import pandas as pd
import joblib
import os


# Find the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
MODEL_PATH = os.path.join(
    BASE_DIR,
    "ai",
    "nirvana_difficulty_model.pkl"
)


# Load trained ML model
model = joblib.load(MODEL_PATH)


def predict_difficulty(
    game_type,
    level,
    accuracy,
    response_time,
    mistakes,
    score
):
    """
    Predict the next difficulty level using
    the trained NIRVANA Random Forest model.

    This is a game-adaptation model,
    NOT a medical diagnostic tool.
    """

    game_data = pd.DataFrame([
        {
            "game_type": game_type,
            "level": level,
            "accuracy": accuracy,
            "response_time": response_time,
            "mistakes": mistakes,
            "score": score
        }
    ])

    prediction = model.predict(game_data)[0]

    probabilities = model.predict_proba(game_data)[0]

    confidence = max(probabilities) * 100

    return prediction, round(confidence, 2)


# Test the model
if __name__ == "__main__":

    difficulty, confidence = predict_difficulty(
        game_type="memory",
        level=2,
        accuracy=85,
        response_time=15,
        mistakes=2,
        score=82
    )

    print("\n========================================")
    print("NIRVANA ML DIFFICULTY PREDICTION")
    print("========================================")

    print("Game Type:", "memory")
    print("Accuracy:", "85%")
    print("Response Time:", "15 seconds")
    print("Mistakes:", 2)
    print("Score:", 82)

    print("\nPredicted Next Difficulty:", difficulty)
    print("Prediction Confidence:", confidence, "%")