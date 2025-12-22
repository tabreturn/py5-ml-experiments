from py5 import Py5Vector2D, random


class DNA:
    def __init__(self, length: int):
        '''The genetic sequence is an array of vectors.'''
        self.max_force = .1  # How strong can the thrusters be?
        # Notice that the length of genes is equal to a global lifeSpan variable.
        self.genes = [
          # Scale the vectors randomly, but not stronger than the maximum force.
          Py5Vector2D().random() * random(0, self.max_force)
          for _ in range(length)
        ]
