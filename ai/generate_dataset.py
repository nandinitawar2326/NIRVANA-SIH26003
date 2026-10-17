import pandas as pd
import random


# Make results reproducible
random.seed(42)

game_types = [
    "memory",
    "attention",
    "pattern",
    "recall"
]

rows = []


# Generate 100 synthetic users
for user_number in range(1, 101):

    user_id = f"U{user_number:03d}"

    # Generate 10 sessions per user
    for session in range(1, 11):

        game_type = random.choice(game_types)

        level = random.randint(1, 3)

        # Generate performance
        accuracy = random.randint(40, 98)

        response_time = round(
            random.uniform(8, 35), 2
        )

        mistakes = random.randint(0, 8)

        # Calculate a synthetic game score
        score = (
            accuracy * 0.7
            + max(0, 100 - response_time * 1.5) * 0.2
            + max(0, 100 - mistakes * 10) * 0.1
        )

        score = round(
            max(0, min(100, score)),
            2
        )

        # Create difficulty label
        if score >= 80:
            recommended_difficulty = "hard"

        elif score >= 60:
            recommended_difficulty = "medium"

        else:
            recommended_difficulty = "easy"

        rows.append([
            user_id,
            game_type,
            level,
            accuracy,
            response_time,
            mistakes,
            score,
            recommended_difficulty
        ])


# Create DataFrame
data = pd.DataFrame(
    rows,
    columns=[
        "user_id",
        "game_type",
        "level",
        "accuracy",
        "response_time",
        "mistakes",
        "score",
        "recommended_difficulty"
    ]
)


# Save dataset
data.to_csv(
    "datasets/game_sessions_ml.csv",
    index=False
)


print("================================")
print("NIRVANA SYNTHETIC DATASET")
print("================================")

print("Total sessions:", len(data))
print("Total users:", data["user_id"].nunique())

print("\nGame types:")
print(data["game_type"].value_counts())

print("\nDifficulty distribution:")
print(data["recommended_difficulty"].value_counts())

print("\nFirst 10 records:")
print(data.head(10))

print("\nDataset saved to:")
print("datasets/game_sessions_ml.csv")