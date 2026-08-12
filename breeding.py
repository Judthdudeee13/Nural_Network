import random
import time

string = "Hello, World!"
options = "q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M , . ? !".split()
options.append(" ")

class Parent:
    def __init__(self, lenght):
        string = [random.choice(options) for _ in range(lenght)]
        self.string = ""
        for x in string:
            self.string += x
        self.fitness = 0

class Specimin:
    def __init__(self, parent1, parent2):
        self.parent1 = parent1
        self.parent2 = parent2
        self.generate_self()
        self.mutate()
        self.fitness = 0
        print(f"Child: {self.string}")

    def generate_self(self):
        child_string = ""
        parents = [self.parent1, self.parent2]
        for i in range(len(self.parent1.string)):
            parent = random.choice(parents)
            child_string += parent.string[i]

        self.string = child_string
        
    def mutate(self):
        mutated_string = ""
        for i in range(len(self.string)):
            if random.randint(0, 100) == 0:
                mutated_string += random.choice(options)
            else:
                mutated_string += self.string[i]
        self.string = mutated_string

class Enviroment:
    def __init__(self, childern_per_parent, str_length, string, *parents):
        self.childern_per_parent = childern_per_parent
        self.parents = parents
        self.generation = 0
        self.str_length = str_length
        self.string = string

    def judge_fitness(self):
        for parent in self.parents:
            for i in range(self.str_length):
                if parent.string[i] == self.string[i]:
                    parent.fitness += 1

    def kill(self):
        parents = []
        temp_parents = self.parents
        self.parents = sorted(temp_parents, key=lambda x: x.fitness, reverse=True)
        for i in range(int(len(self.parents)/self.childern_per_parent)):
                parents.append(self.parents[i])
        self.parents = parents


    def next_generation(self):
        new_children = []
        while self.parents:
            parent1 = random.choice(self.parents)
            self.parents.remove(parent1)
            parent2 = random.choice(self.parents)
            self.parents.remove(parent2)
            for _ in range(self.childern_per_parent*2):
                new_children.append(Specimin(parent1, parent2))
        self.parents = new_children

    def evolve(self):
        print(f"Generation: {self.generation}")
        self.judge_fitness()
        self.kill()
        self.next_generation()
        self.generation += 1

parents = [Parent(13) for _ in range(32)]
enviroment = Enviroment(2, 13, string, *parents)
while True:
    print()
    print()
    print()
    enviroment.evolve()
    print(len(enviroment.parents))
    time.sleep(0.1)