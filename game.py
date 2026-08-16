import random
import breeding

class Game:
    def __init__(self):
        self.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.wall = 1
        self.player = 2
        self.score = 0

    def change(self):
        options = [0, 1, 1, 1, 1, 1, 1, 1, 1]
        for x in range(9):
            choice = random.choice(options)
            options.remove(choice)
            self.grid[x] = choice

    def output(self):
        return self.grid

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

while True:
    enviroment = breeding.Enviroment(16, 2, 9, 9, 11)
    parents = enviroment.return_parents()
    for parent in parents:
        for _ in range(100):
            game = Game()
            game.change()
            game.get_player_input(convert_input(parent.network.run(game.output())))
        parent.network.score = game.score
        print(parent.network.score)
    enviroment.evolve()

