import random
import breeding
import csv
import os
import time

class Game:
    def __init__(self):
        self.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.wall = 1
        self.score = 0

    def change(self):
        options = [0, 1, 1, 1, 1, 1, 1, 1, 1]
        for x in range(9):
            choice = random.choice(options)
            options.remove(choice)
            self.grid[x] = choice

    def output(self):
        grid = []
        for x in self.grid:
            if x == 1:
                grid.append(0.5)
            else:
                grid.append(0.1)
        return grid

    def get_player_input(self, input):
        if self.grid[input] == 0:
            self.score += 1


def convert_input(input):
    highest = -1
    num = 0
    for x in range(len(input)):
        if input[x] > highest:
            highest = input[x]
            num = x
    return num

def get_scores(parents):
    highest = 0
    for parent in parents:
        if parent.network.score > highest:
            highest = parent.network.score
    average = 0
    for parent in parents:
        average += parent.network.score
    average = average/len(parents)
    lowest = 100
    for parent in parents:
            if parent.network.score < lowest:
                lowest = parent.network.score

    return highest, lowest, average

enviroment = breeding.Enviroment(16, 2, 9, 9, 11)
file_exists = os.path.exists("training.csv")
with open("training.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Generation", "Best", "Worst", "Average"])
    while True:
        parents = enviroment.return_parents()
        for parent in parents:
            game = Game()
            for _ in range(100):
                game.change()
                game.get_player_input(convert_input(parent.network.run(game.output())))
            parent.network.score = game.score
        best, worst, average = get_scores(parents)
        print(f"Generation: {enviroment.generation}, Best: {best}, Worst: {worst}, Average: {average}")
        writer.writerow([
            enviroment.generation,
            best,
            worst,
            average
        ])
        enviroment.evolve()

