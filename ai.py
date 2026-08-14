import random

class Neuron:
    def __init__(self, inputs, first=False):
        starting_bias = random.uniform(-1, 1)
        self.bias = starting_bias
        self.sum = 0
        self.weights = [random.uniform(-1, 1) for _ in range(len(inputs))] if first == False else []
        self.inputs = inputs

    def input(self):
        sum = 0
        weighted_inputs = []
        try:
            for x in range(len(self.inputs)):
                weighted_inputs.append(self.inputs[x]*self.weights[x])
        except:
            for x in self.inputs:
                weighted_inputs.append(x)
        for x in weighted_inputs:
            sum += x
        sum += self.bias
        self.sum = sum

    def send(self):
        return self.sum if self.sum > 0 else 0


class Network:
    def __init__(self, input, output, num_hidden_layers, *num_per_hidden_layer):
        self.inputs = [Neuron(None, True) for _ in range(input)]
        self.hidden_layers = [[Neuron() for _ in range(num_per_hidden_layer[x])] for x in range(num_hidden_layers)]
        self.outputs = [Neuron() for _ in range(output)]
        
