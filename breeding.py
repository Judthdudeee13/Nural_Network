import random
from nerual_network import Network
import time

class Parent:
    def __init__(self, values, weights=None, baises=None):
        self.network = Network(*values, weights = weights, biases = baises)
        self.fitness = 0


class Specimin:
    def __init__(self, parent1, parent2):
        self.parent1 = parent1
        self.parent2 = parent2
        self.data = parent1.network.data
        self.generate_self()
        self.mutate()
        self.create_network()
        self.parent1 = None
        self.parent2 = None
        self.data = None



    def generate_self(self):
        child_biases = []
        child_weights = []
        parent1_wights, parent1_biases = self.parent1.network.get_weights_and_biases() 
        parent2_wights, parent2_biases = self.parent2.network.get_weights_and_biases()
        for layer in range(len(parent1_wights)):
                    child_weights.append([])
                    for neuron in range(len(parent1_wights[layer])):
                        child_weights[layer].append([])
                        for weight in range(len(parent1_wights[layer][neuron])):
                            child_weights[layer][neuron].append(parent1_wights[layer][neuron][weight] if random.randint(0, 1) == 0 else parent2_wights[layer][neuron][weight])
        for layer in range(len(parent1_biases)):
                    child_biases.append([])
                    for neuron in range(len(parent1_biases[layer])):
                        child_biases[layer].append(parent1_biases[layer][neuron] if random.randint(0, 1) == 0 else parent2_biases[layer][neuron])

        self.child_weights = child_weights
        self.child_biases = child_biases

    def mutate(self):
        for layer in range(len(self.child_weights)):
            for neuron in range(len(self.child_weights[layer])):
                for weight in range(len(self.child_weights[layer][neuron])):
                    if random.randint(0, 50) == 0:
                        #self.child_weights[layer][neuron][weight] += random.uniform(-0.2, 0.2)
                        if random.randint(0, 9) == 0:
                            self.child_weights[layer][neuron][weight] += random.uniform(-1, 1)
                        else:
                            self.child_weights[layer][neuron][weight] += random.uniform(-0.2, 0.2)
                        
        for layer in range(len(self.child_biases)):
            for neuron in range(len(self.child_biases[layer])):
                if random.randint(0, 50) == 0:
                    #self.child_biases[layer][neuron] += random.uniform(-0.2, 0.2)
                    if random.randint(0, 9) == 0:
                        self.child_biases[layer][neuron] += random.uniform(-1, 1)
                    else:
                        self.child_biases[layer][neuron] += random.uniform(-0.2, 0.2)
                        
                    

    def create_network(self):
        self.network = Network(self.data[0], self.data[1], self.data[2], biases=self.child_biases, weights=self.child_weights)


class Enviroment:
    def __init__(self, num_parents, num_kids, num_inputs, num_outputs, *num_hidden_layer, weights = None, biases = None, generation = 0):
        data = [num_inputs, num_outputs, *num_hidden_layer]
        self.parents = [Parent(data) for _ in range(num_parents)] if weights == None else [Parent(data, weights[x], biases[x]) for x in range(num_parents)]
        self.children_per_parent = num_kids

        self.generation = generation

    def return_parents(self):
        return self.parents

    def kill_parents(self):
        parents = []
        temp_parents = self.parents
        self.parents = sorted(temp_parents, key=lambda x: x.network.score, reverse=True)
        for i in range(int(len(self.parents)/self.children_per_parent)):
                parents.append(self.parents[i])
        self.parents = parents

    def next_generation(self):
            new_children = []
            while self.parents:
                parent1 = random.choice(self.parents)
                self.parents.remove(parent1)
                parent2 = random.choice(self.parents)
                self.parents.remove(parent2)
                for _ in range(self.children_per_parent*2):
                    new_children.append(Specimin(parent1, parent2))
            self.parents = new_children

    def evolve(self):
        self.kill_parents()
        self.next_generation()
        self.generation += 1
                
            
