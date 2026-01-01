import numpy as np

class NeuralNetwork:
    def __init__(self, input_size=2, hidden_size=4, output_size=2, weights=None, biases=None, seed=None):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.rng = np.random.default_rng(seed)

        if weights is not None:
            self.weights1 = weights[0]
            self.weights2 = weights[1]
            self.bias1 = biases[0]
            self.bias2 = biases[1]
        else:
            # Initialize with random weights
            self.weights1 = self.rng.uniform(-1, 1, (self.input_size, self.hidden_size))
            self.weights2 = self.rng.uniform(-1, 1, (self.hidden_size, self.output_size))
            self.bias1 = self.rng.uniform(-1, 1, (1, self.hidden_size))
            self.bias2 = self.rng.uniform(-1, 1, (1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        return np.tanh(x)

    def process(self, inputs):
        # inputs shape: (1, 2)
        h1 = self.tanh(np.dot(inputs, self.weights1) + self.bias1)
        output = self.tanh(np.dot(h1, self.weights2) + self.bias2)
        return output[0] # Returns [speed, rotation]

    def mutate(self, rate=0.1, magnitude=0.2):
        self.weights1 += (self.rng.uniform(-1, 1, self.weights1.shape) < rate) * self.rng.uniform(-magnitude, magnitude, self.weights1.shape)
        self.weights2 += (self.rng.uniform(-1, 1, self.weights2.shape) < rate) * self.rng.uniform(-magnitude, magnitude, self.weights2.shape)
        self.bias1 += (self.rng.uniform(-1, 1, self.bias1.shape) < rate) * self.rng.uniform(-magnitude, magnitude, self.bias1.shape)
        self.bias2 += (self.rng.uniform(-1, 1, self.bias2.shape) < rate) * self.rng.uniform(-magnitude, magnitude, self.bias2.shape)

    def copy(self):
        return NeuralNetwork(
            self.input_size, self.hidden_size, self.output_size,
            weights=[self.weights1.copy(), self.weights2.copy()],
            biases=[self.bias1.copy(), self.bias2.copy()]
        )
