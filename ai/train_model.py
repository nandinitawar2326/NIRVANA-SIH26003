import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = pd.read_csv("datasets/game_sessions_ml.csv")

print("========================================")
print("NIRVANA ML TRAINING")
print("========================================")

print("Total records:", len(data))


# ==========================================
# 2. FEATURES AND TARGET
# ==========================================

features = [
    "game_type",
    "level",
    "accuracy",
    "response_time",
    "mistakes",
    "score"
]

X = data[features]

y = data["recommended_difficulty"]


# ==========================================
# 3. FEATURE TYPES
# ==========================================

categorical_features = [
    "game_type"
]

numeric_features = [
    "level",
    "accuracy",
    "response_time",
    "mistakes",
    "score"
]


# ==========================================
# 4. PREPROCESSING
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)


# ==========================================
# 5. RANDOM FOREST
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)


# ==========================================
# 6. PIPELINE
# ==========================================

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# ==========================================
# 7. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 8. TRAIN
# ==========================================

print("\nTraining Random Forest...")

pipeline.fit(
    X_train,
    y_train
)

print("Training completed!")


# ==========================================
# 9. PREDICTION
# ==========================================

y_pred = pipeline.predict(X_test)


# ==========================================
# 10. ACCURACY
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n========================================")
print("MODEL PERFORMANCE")
print("========================================")

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# ==========================================
# 11. CLASSIFICATION REPORT
# ==========================================

print("\n========================================")
print("CLASSIFICATION REPORT")
print("========================================")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# 12. CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=["easy", "medium", "hard"]
)

print("\n========================================")
print("CONFUSION MATRIX")
print("========================================")

print(cm)


display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Easy", "Medium", "Hard"]
)

display.plot()

plt.title("NIRVANA Difficulty Prediction")
plt.tight_layout()

plt.savefig(
    "docs/confusion_matrix.png"
)

plt.show()


# ==========================================
# 13. FEATURE IMPORTANCE
# ==========================================

print("\n========================================")
print("FEATURE IMPORTANCE")
print("========================================")

trained_model = pipeline.named_steps["model"]

feature_names = (
    pipeline
    .named_steps["preprocessor"]
    .get_feature_names_out()
)

importance = trained_model.feature_importances_

feature_importance = pd.DataFrame({
    "feature": feature_names,
    "importance": importance
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print(
    feature_importance.to_string(index=False)
)


# ==========================================
# 14. SAVE MODEL
# ==========================================

joblib.dump(
    pipeline,
    "ai/nirvana_difficulty_model.pkl"
)

print("\n========================================")
print("MODEL SAVED")
print("========================================")

print(
    "Saved to: ai/nirvana_difficulty_model.pkl"
)


# ==========================================
# 15. TEST NEW GAME
# ==========================================

new_game = pd.DataFrame([
    {
        "game_type": "memory",
        "level": 2,
        "accuracy": 85,
        "response_time": 15,
        "mistakes": 2,
        "score": 82
    }
])

prediction = pipeline.predict(
    new_game
)

probabilities = pipeline.predict_proba(
    new_game
)

print("\n========================================")
print("NEW GAME PREDICTION")
print("========================================")

print(
    "Predicted difficulty:",
    prediction[0]
)

print(
    "Prediction confidence:",
    round(
        max(probabilities[0]) * 100,
        2
    ),
    "%"
)