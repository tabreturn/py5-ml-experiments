from py5 import random


class DNA:
    # Genetic sequence is a single value! But scales for sophisticated bloops.
    genes = [random(1) for _ in range(1)]