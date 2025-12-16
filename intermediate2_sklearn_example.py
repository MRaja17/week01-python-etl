# Intermediate 2: Dataset Analysis using Pandas

import pandas as pd

# 1. Load CSV using pandas
df = pd.read_csv("students.csv")

# 2. Basic statistics
total_students = len(df)
average_score = df["score"].mean()
highest = df.loc[df["score"].idxmax()]
lowest = df.loc[df["score"].idxmin()]

# 3. Print results
print("Total students:", total_students)
print("Average score:", round(average_score, 2))
print("Highest scorer:", highest['name'], "-", highest['score'])
print("Lowest scorer:", lowest['name'], "-", lowest['score'])
