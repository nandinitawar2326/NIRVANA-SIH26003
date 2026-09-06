import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = pd.read_csv("datasets/game_sessions_ml.csv")

print("Dataset loaded successfully!")
print("Total records:", len(data))


# ==========================================
# 2. SELECT FEATURES AND TARGET
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
# 3. DEFINE COLUMNS
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
# 5. CREATE ML MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)


# ==========================================
# 6. CREATE PIPELINE
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


print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ==========================================
# 8. TRAIN MODEL
# ==========================================

print("\nTraining Random Forest model...")

pipeline.fit(
    X_train,
    y_train
)

print("Training completed!")


# ==========================================
# 9. MAKE PREDICTIONS
# ==========================================

y_pred = pipeline.predict(X_test)


# ==========================================
# 10. EVALUATE MODEL
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n===== MODEL PERFORMANCE =====")

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print("\n===== CLASSIFICATION REPORT =====")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# 11. TEST NEW GAME RESULT
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

print("\n===== NEW GAME PREDICTION =====")

print(
    "Predicted difficulty:",
    prediction[0]
)