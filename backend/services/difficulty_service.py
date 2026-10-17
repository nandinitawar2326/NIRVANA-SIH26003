from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ai" / "nirvana_difficulty_model.pkl"


pipeline = joblib.load(MODEL_PATH)


def predict_difficulty(game_session):

    new_game = pd.DataFrame([
        {
            "game_type": game_session.game_type,
            "level": game_session.level,
            "accuracy": game_session.accuracy,
            "response_time": game_session.response_time,
            "mistakes": game_session.mistakes,
            "score": game_session.score
        }
    ])

    prediction = pipeline.predict(new_game)[0]

    probabilities = pipeline.predict_proba(new_game)

    confidence = float(max(probabilities[0]))

    return {
        "recommended_difficulty": str(prediction),
        "confidence": round(confidence * 100, 2)
    }