from py5 import random


class Perceptron:
    def __init__(self, n: int):
        """The argument n determines number of inputs (including the bias)."""
        self.weights = [
          # The weights are picked randomly to start.
          random(-1, 1)
          for _ in range(n)
        ]

    def feed_forward(inputs: float): -> int:
        """The result is the sign of the sum, –1 or +1."""
        weighted_sum = sum(i * w for i, w in zip(inputs, weights))
        # The perceptron is guessing: Is it on one side of the line or other?
        return this.activate(sum);
        