from py5 import get_current_sketch, random
from bloop import Bloop
from dna import DNA


class World:
    """A list of bloops."""
    def __init__(self, population_size: int):
        # An array of bloops.
        self.bloops = [
          # Create each bloop with a starting position.
          Bloop(
            random(get_current_sketch().width),
            random(get_current_sketch().height),
            DNA()
          )
          for _ in range(population_size)
        ]