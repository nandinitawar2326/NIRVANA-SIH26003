import pandas as pd


# Location of our dataset
file_path = "datasets/game_sessions.csv"


# Load CSV
data = pd.read_csv(file_path)


print("\n===== NIRVANA DATASET =====")

print(data)


print("\n===== DATASET INFORMATION =====")

print("Number of game sessions:", len(data))
print("Number of users:", data["user_id"].nunique())
print("Game types:", data["game_type"].unique())


print("\n===== AVERAGE PERFORMANCE =====")

print("Average accuracy:",
      round(data["accuracy"].mean(), 2))

print("Average response time:",
      round(data["response_time"].mean(), 2), "seconds")

print("Average mistakes:",
      round(data["mistakes"].mean(), 2))

print("Average score:",
      round(data["score"].mean(), 2))