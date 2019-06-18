import numpy as np
import math
import random
import fish


class Brain:
    def __init__(self, weights=None, biases=None):
        if weights is None:
            weights=[]
        if biases is None:
            biases=[]
        self.weights=weights
        self.biases=biases


def initialize(layers):
    brain = Brain()

    for i in range (len(layers)-1):
        brain.weights.append( np.random.randn(layers[i], layers[i+1]) )
        brain.biases.append( np.random.randn(layers[i+1]))

    return layers, brain


def calculate(input, brain):
    output = np.copy(input)

    for i in range(len(brain.weights)):
        output = output.dot(brain.weights[i])
        output = output + brain.biases[i]
        output = sigmoid(output)

    return output


def sigmoid (x):
    return np.vectorize(lambda y : 1./(1+np.exp(-y)))(x)


def crossover (brain1, brain2):
    res = Brain()
    res.weights = np.copy(brain1.weights)
    res.biases = np.copy(brain1.biases)

    for i in range(len(res.weights)):
        for j in range(len(res.weights[i])):
            for k in range(len(res.weights[i][j])):
                if np.random.randint(2):    # random binary number
                    res.weights[i][j][k]=brain2.weights[i][j][k]

    for i in range(len(res.biases)):
        for j in range(len(res.biases[i])):
            if np.random.randint(2):    # random binary number
                res.biases[i][j]=brain2.biases[i][j]

    return res


def mutation (brain, prob):

    for neurons in brain.weights:
        for i in range(len(neurons)):
            for j in range(len(neurons[i])):
                if np.random.random()<prob:
                    neurons[i][j]=np.random.randn()

    for neurons in brain.biases:
        for i in range(len(neurons)):
            if np.random.random()<prob:
                neurons[i]=np.random.randn()


def fitness (fish):
    return fish.age * (1 + 0.5*fish.health - 0.5*fish.hunger)
