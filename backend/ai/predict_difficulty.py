import os
import joblib
import pandas as pd


# ==========================================
# PATH CONFIGURATION
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ai",
    "nirvana_difficulty_model.pkl"
)


# ==========================================
# LOAD MODEL SAFELY
# ==========================================

model = None


def load_model():
    """
    Load the trained difficulty prediction model.
    Returns None if the model file is not available.
    """

    global model

    if model is not None:
        return model

    if not os.path.exists(MODEL_PATH):
        return None

    try:
        model = joblib.load(MODEL_PATH)
        return model

    except Exception as error:
        print(f"Error loading AI model: {error}")
        return None


# ==========================================
# PREDICT DIFFICULTY
# ==========================================

def predict_difficulty(
    game_type: str,
    level: int,
    accuracy: float,
    response_time: float,
    mistakes: int,
    score: float
):
    """
    Predict the recommended game difficulty.

    Returns:
        Dictionary containing difficulty recommendation
        and prediction confidence.
    """

    trained_model = load_model()

    # --------------------------------------
    # FALLBACK AI LOGIC
    # --------------------------------------

    if trained_model is None:

        performance = (
            accuracy * 0.5
            + max(0, 100 - response_time * 2) * 0.3
            + max(0, 100 - mistakes * 10) * 0.2
        )

        if performance >= 80:
            difficulty = "hard"

        elif performance >= 60:
            difficulty = "medium"

        else:
            difficulty = "easy"

        return {
            "recommended_difficulty": difficulty,
            "confidence": None,
            "model_used": False,
            "message": "Rule-based difficulty prediction used"
        }

    # --------------------------------------
    # MACHINE LEARNING PREDICTION
    # --------------------------------------

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

    try:

        prediction = trained_model.predict(game_data)[0]

        confidence = None

        # Check if model supports probabilities
        if hasattr(trained_model, "predict_proba"):

            probabilities = trained_model.predict_proba(
                game_data
            )[0]

            confidence = round(
                float(max(probabilities)) * 100,
                2
            )

        return {
            "recommended_difficulty": str(prediction),
            "confidence": confidence,
            "model_used": True,
            "message": "Machine learning prediction used"
        }

    except Exception as error:

        return {
            "recommended_difficulty": "medium",
            "confidence": None,
            "model_used": False,
            "message": f"Prediction error: {str(error)}"
        }


# ==========================================
# TEST FILE
# ==========================================

if __name__ == "__main__":

    result = predict_difficulty(
        game_type="memory",
        level=1,
        accuracy=85,
        response_time=10,
        mistakes=2,
        score=80
    )

    print(result)