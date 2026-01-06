from py5 import random

class DNA:
    """Flower genotype."""
    def __init__(self):
        # The genetic sequence (14 properties for each flower).
        # Each gene is a random value from 0 to 1.
        self.genes = [random(0, 1) for _ in range(14)]