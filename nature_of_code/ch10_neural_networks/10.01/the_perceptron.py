from perceptron import Perceptron

INPUTS = [50, -12, 1]


def setup():
    # Create the perceptron.
    perceptron = new Perceptron(3)
    # The input is three values: x, y, and the bias.


def draw():
    # The answer!
    guess = perceptron.feed_forward(INPUTS)