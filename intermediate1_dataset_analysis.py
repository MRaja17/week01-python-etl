# Intermediate 1: Dataset Analysis using Python Basics

# 1. Read the CSV file manually (without pandas)
students = []

with open("students.csv", "r") as file:
    lines = file.readlines()

# Remove header
data = lines[1:]

# Parse rows
for row in data:
    name, age, score = row.strip().split(",")
    students.append({
        "name": name,
        "age": int(age),
        "score": int(score)
    })

# 2. Compute simple analytics
total_students = len(students)
average_score = sum(s["score"] for s in students) / total_students
highest = max(students, key=lambda x: x["score"])
lowest = min(students, key=lambda x: x["score"])

# 3. Print results
print("Total students:", total_students)
print("Average score:", round(average_score, 2))
print("Highest scorer:", highest["name"], "-", highest["score"])
print("Lowest scorer:", lowest["name"], "-", lowest["score"])
