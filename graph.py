import csv
import matplotlib.pyplot as plt
import time


plt.ion()  # Turn on interactive mode

fig, ax = plt.subplots()

while True:

    generations = []
    best_scores = []
    worst_scores = []
    average_scores = []

    try:
        with open("48_pool_20hidden_2pct_pm0.2_grid.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                generations.append(int(row["Generation"]))
                best_scores.append(float(row["Best"]))
                worst_scores.append(float(row["Worst"]))
                average_scores.append(float(row["Average"]))

    except FileNotFoundError:
        print("training.csv hasn't been created yet.")
        time.sleep(1)
        continue

    # Clear the old graph
    ax.clear()

    # Draw the new data
    ax.plot(generations, best_scores, label="Best")
    ax.plot(generations, worst_scores, label="Worst")
    ax.plot(generations, average_scores, label="Average")

    ax.set_xlabel("Generation")
    ax.set_ylabel("Score")
    ax.set_title("Neural Network Training")
    ax.set_ylim(0, 100)

    ax.legend()
    ax.grid()

    # Refresh the graph
    fig.canvas.draw()
    fig.canvas.flush_events()

    # Check for new data every second
    time.sleep(0.1)