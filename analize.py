import csv
import matplotlib.pyplot as plt
import statistics


# =========================
# CHANGE THIS FILE NAME
# =========================

filename = "10hidden_10hidden_large.csv"


# =========================
# READ CSV
# =========================

generations = []
best_scores = []
worst_scores = []
average_scores = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        generations.append(int(row["Generation"]))
        best_scores.append(float(row["Best"]))
        worst_scores.append(float(row["Worst"]))
        average_scores.append(float(row["Average"]))


# =========================
# BASIC INFORMATION
# =========================

print("\n========== EXPERIMENT ==========")

print("File:", filename)
print("Generations:", len(generations))

print("\nStarting:")
print("  Best:", best_scores[0])
print("  Worst:", worst_scores[0])
print("  Average:", average_scores[0])

print("\nEnding:")
print("  Best:", best_scores[-1])
print("  Worst:", worst_scores[-1])
print("  Average:", average_scores[-1])


# =========================
# BEST RESULTS
# =========================

highest_best = max(best_scores)
generation_best = generations[best_scores.index(highest_best)]

highest_average = max(average_scores)
generation_average = generations[average_scores.index(highest_average)]


print("\n========== RECORDS ==========")

print(
    f"Highest Best Score: {highest_best} "
    f"(Generation {generation_best})"
)

print(
    f"Highest Average Score: {highest_average} "
    f"(Generation {generation_average})"
)


# =========================
# IMPROVEMENT
# =========================

average_improvement = average_scores[-1] - average_scores[0]

print("\n========== IMPROVEMENT ==========")

print(
    f"Average improvement: "
    f"{average_improvement:.2f} points"
)


# =========================
# ANALYZE EVERY 100 GENERATIONS
# =========================

print("\n========== EVERY 100 GENERATIONS ==========")

for start in range(0, len(generations), 100):

    end = min(start + 100, len(generations))

    chunk = average_scores[start:end]

    print(
        f"{generations[start]} - {generations[end - 1]}:"
        f"  Average = {statistics.mean(chunk):.2f}"
        f"  Best = {max(best_scores[start:end])}"
        f"  Worst = {min(worst_scores[start:end])}"
    )


# =========================
# GRAPH 1 - RAW DATA
# =========================

plt.figure(figsize=(12, 6))

plt.plot(generations, best_scores, label="Best")
plt.plot(generations, average_scores, label="Average")
plt.plot(generations, worst_scores, label="Worst")

plt.xlabel("Generation")
plt.ylabel("Score")
plt.title("Neural Network Training 20 hidden")

plt.legend()
plt.grid()


# =========================
# GRAPH 2 - AVERAGE EVERY 100
# =========================

range_generations = []
range_averages = []

for start in range(0, len(generations), 100):

    end = min(start + 100, len(generations))

    range_generations.append(generations[start])

    range_averages.append(
        statistics.mean(average_scores[start:end])
    )


plt.figure(figsize=(12, 6))

plt.plot(range_generations, range_averages)

plt.xlabel("Generation")
plt.ylabel("Average Score")
plt.title("Average Score Per 100 Generations 20 hidden")

plt.grid()


# =========================
# SHOW BOTH
# =========================

plt.show()