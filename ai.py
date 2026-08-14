import random

class Neuron:
    def __init__(self):
        starting_bias = random.uniform(-1, 1)
        self.bias = starting_bias
        self.value = 0

    def input(self, inputs):
        value = 0
        for x in inputs:
            value += x
        value += self.bias
        self.value = value if value > 0 else 0

    def send(self):
        return self.value 

class InputNeuron:
    def __init__(self):
        self.value = 0

    def input(self, inputs):
        self.value = inputs[0]

    def send(self):
        return self.value


class Network:
    def __init__(self, input, output, *num_per_hidden_layer):
        self.inputs = [InputNeuron() for _ in range(input)]
        self.hidden_layers = [[Neuron() for _ in range(num_per_hidden_layer[x])] for x in range(len(num_per_hidden_layer))]
        self.outputs = [Neuron() for _ in range(output)]
        self.neurons = [self.inputs, *self.hidden_layers, self.outputs]

        self.weights = []
        for layer in range(len(self.neurons)-1):
            self.weights.append([])
            for x in range(len(self.neurons[layer+1])):
                self.weights[layer].append([])
                for y in range(len(self.neurons[layer])):
                    self.weights[layer][x].append(random.uniform(-1, 1))

    def input(self, inputs):
        for x in range(len(inputs)):
            self.neurons[0][x].input([inputs[x]])

    def feed_forward(self):
        for layer in range(len(self.neurons)-1):
            for neuron in range(len(self.neurons[layer+1])):
                values = []
                for weight in range(len(self.weights[layer][neuron])):
                    values.append(self.weights[layer][neuron][weight] * self.neurons[layer][weight].send())
                self.neurons[layer+1][neuron].input(values)

    def get_output(self):
        for x in self.neurons:
            for y in x:
                print(y.send())

    def get_weights_and_biases(self):
        return self.weights, [[neuron.bias for neuron in layer] for layer in self.neurons[1:]]
    

net = Network(2, 2, 3)
net.input([1, 1])
net.feed_forward()
net.get_output()
