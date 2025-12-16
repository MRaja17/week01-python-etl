# Hard 1: Performance Optimization for Dataset Analysis

import pandas as pd
import time

# Load data
df = pd.read_csv("students.csv")

# -------------------------------
# Method 1: Normal loop (slowest)
# -------------------------------
start = time.time()
total_students_loop = len(df)
avg_score_loop = sum(df["score"]) / len(df)
highest_loop = df.loc[df["score"].idxmax()]
lowest_loop = df.loc[df["score"].idxmin()]
end = time.time()

print("\nMethod 1 (Loop-Based)")
print("Average Score:", avg_score_loop)
print("Time Taken:", round(end - start, 6), "seconds")

# -----------------------------------------
# Method 2: Pandas vectorized (much faster)
# -----------------------------------------
start = time.time()
total_students_fast = df.shape[0]
avg_score_fast = df["score"].mean()
highest_fast = df.loc[df["score"].idxmax()]
lowest_fast = df.loc[df["score"].idxmin()]
end = time.time()

print("\nMethod 2 (Vectorized Pandas)")
print("Average Score:", avg_score_fast)
print("Time Taken:", round(end - start, 6), "seconds")

print("\nOptimization Complete!")
