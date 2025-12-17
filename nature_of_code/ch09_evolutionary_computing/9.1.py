# https://natureofcode.com/genetic-algorithms/#coding-the-genetic-algorithm

population = []  # A list for the population of elements
target = "to be or not to be"
matingpool = []  # Start with an empty mating pool.

class DNA:
    """Represents a DNA sequence of random characters."""

    def __init__(self, length: int):
        self.genes = []  # The individual genes are stored in an array.
        self.fitness = 0  # Add a variable to track fitness.

        for _ in range(length):  # There are length genes.
            # Each gene is a random character.
            self.genes.append(self.random_character())

    def calculate_fitness(self, target: str):
        """Compute fitness as a percentage of correct characters."""
        score = 0
        
        for i, gene in enumerate(self.genes):
            if gene == target[i]:
                score += 1

        self.fitness = score / len(target)

    def random_character(self) -> str:
        """Return a random character (letter, number, symbol, space,
        and so forth).
        """
        c = floor(random(32, 127))
        return chr(c)


def setup():
    """Initialize each element of the population;
    100 and 18 are hardcoded for now as the population size and length
    of the genes array.
    """
    global population

    for _ in range(100):
        population.append(DNA(18))

    for phrase in population:
        phrase.calculate_fitness(target)

    for phrase in population:
        """n is equal to fitness times 100. 100 is an arbitrary way to
        scale the percentage of fitness to a larger integer value.
        """
        n = floor(phrase.fitness * 100)
        print(n)

#         for _ in len(n):
#             """Add each member of the population to the mating pool n
#             times.
#             """
#             matingpool.append(phrase)


#def draw():
#    for phrase in population:
#        phrase.calculate_fitness(target)
