import random
import breeding
import csv
import os
import time
import json
from multiprocessing import Pool

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

def train(parent1):
    game = Game()
    for _ in range(100):
        game.change()
        game.get_player_input(convert_input(parent1.network.run(game.output())))
    parent1.network.score = game.score

    return parent1

def get_wieghts_biases(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)

        all_weights = []
        all_biases = []

        for parent in data["parents"]:
            all_weights.append(parent["weights"])
            all_biases.append(parent["biases"])

    return all_weights, all_biases

def convert_input(input):
    highest = -1
    num = 0
    for x in range(len(input)):
        if input[x] > highest:
            highest = input[x]
            num = x
    return num

def save():
    save_data = True if input('Do you want to save(y/n)? ') == 'y' else False
    if save_data:
        file_name = input("File Name(json): ")
        data = {
            "generation": enviroment.generation,
            "parents": []
        }
        parents = enviroment.return_parents()
        for parent in parents:
            weights, biases = parent.network.get_weights_and_biases()
            data["parents"].append({
                "score": parent.network.score,
                "weights": weights,
                "biases": biases
            })

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

def get_scores(parents):
    highest = 0
    data = None
    for parent in parents:
        if parent.network.score > highest:
            highest = parent.network.score
            data = parent.network.get_weights_and_biases()
    average = 0
    for parent in parents:
        average += parent.network.score
    average = average/len(parents)
    lowest = 100
    for parent in parents:
            if parent.network.score < lowest:
                lowest = parent.network.score

    return highest, lowest, average, data


#old_weights, old_biases = get_wieghts_biases("test.json")

enviroment = breeding.Enviroment(48, 2, 9, 9, 2)# #weights=old_weights, biases=old_biases, generation=2288)
file_exists = os.path.exists("test1.csv")

if __name__ == "__main__":
    for test in range(2):
        enviroment = breeding.Enviroment(48, 2, 9, 9, 2)# #weights=old_weights, biases=old_biases, generation=2288)
        file_exists = os.path.exists(f"test{test}.csv")
        with open(f"test{test}.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Generation", "Best", "Worst", "Average"])
            try:
                start_time = time.time()
                with Pool(3) as pool:
                    while enviroment.generation <= 200000:
                        parents = enviroment.return_parents()

                        if test == 0:
                            parents = pool.map(train, parents)
                        else:
                            for parent in parents:
                                train(parent)
                        best, worst, average, data = get_scores(parents)
                        print(f"Generation: {enviroment.generation}, Best: {best}, Worst: {worst}, Average: {average}")
                        writer.writerow([
                            enviroment.generation,
                            best,
                            worst,
                            average
                        ])
                        if best == 100:
                            with open("perfect.txt", "a") as file:
                                weights = data[0]
                                biases = data[1]
                                file.write("\n========== PERFECT NETWORK ==========\n")
                                file.write(f"Generation: {enviroment.generation}\n")
                                file.write(f"Network Structure: 1 layer of 2 Large Mutations\n")
                                file.write(f"Weights: {weights}\n")
                                file.write(f"Biases: {biases}\n")
                        enviroment.evolve()

                print(time.time()-start_time)
                #save()
                
            except KeyboardInterrupt:
                save()
