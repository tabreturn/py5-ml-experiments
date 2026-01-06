from dna import DNA
from py5 import color, floor, remap


class Flower():
    """Flower phenotype."""
    def __init__(self, dna: DNA, x: float, y: float):
        self.dna = dna  # Flower DNA.
        self.fitness = 1  # How fit is the flower?

    def show(self):
        # DNA values such as petal color, petal size, and number of petals.
        genes = self.dna.genes
        # Set RGB range from 0 to 1 with color_mode() and use map() as needed.
        petal_color  = color(genes[0], genes[1], genes[2], genes[3])
        petal_size   = remap(genes[4], 0, 1, 4, 24)
        petal_count  = floor(remap(genes[5], 0, 1, 2, 16))
        center_color = color(genes[6], genes[7], genes[8])
        center_size  = remap(genes[9], 0, 1, 24, 48)
        stem_color   = color(genes[10], genes[11], genes[12])
        stem_length  = remap(genes[13], 0, 1, 50, 100)

    