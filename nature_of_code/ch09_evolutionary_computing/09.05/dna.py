from py5 import random


class DNA:
    # Genetic sequence is a single value! But scales for sophisticated bloops.
    def __init__(self):
        self.genes = [random(1) for _ in range(1)]

    def copy(self) -> 'DNA':
        """This copy() method replaces crossover()."""
        new_dna = DNA()  # Create new DNA (with random genes).
        # Overwrite the random genes with a copy of this DNA's genes.
        new_dna.genes = self.genes[:]
        return new_dna

    def mutate(self, mutation_rate: float) -> None:
        """Mutation."""
        for i, _ in enumerate(self.genes):
            if random(1) < mutation_rate:
                self.genes[i] = random(1)