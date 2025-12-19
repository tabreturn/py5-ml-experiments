# https://natureofcode.com/genetic-algorithms/#coding-the-genetic-algorithm

population = []  # A list for the population of elements
target = "cat" #"to be or not to be"
mutationrate = 0.01


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
        """Return a random character (letter, number, symbol, space, and so forth)."""
        c = floor(random(32, 127))
        return chr(c)

    def crossover(self, partner: 'DNA'):
        # The child is a new instance of DNA.
        # (Note that the genes are generated randomly in the DNA constructor,
        # but the crossover method will override the array.)
        child = DNA(len(self.genes))
        
        # Pick a random midpoint in the genes array.
        midpoint = floor(random(len(self.genes)))

        # Before the midpoint, take genes from this DNA.
        child.genes[:midpoint] = self.genes[:midpoint]
        # After the midpoint, take from the partner DNA.
        child.genes[midpoint:] = partner.genes[midpoint:]

        return child

    def mutate(self):
        for i, _ in enumerate(self.genes):  # Look at each gene in the array.
            # Check a random number against the mutation rate.
            if random(1) < mutationrate:
                # Mutation means choosing a new random character.
                self.genes[i] = self.random_character()
            

def setup():
    """Initialize each element of the population;
    100 and 18 are hardcoded for now as the population size and length of the genes array."""
    global population

#     for _ in range(100):
#         population.append(DNA(18))
    population.append(DNA(3))  #------------------------------------------------
    population.append(DNA(3))  #------------------------------------------------
    population.append(DNA(3))  #------------------------------------------------
    population[0].genes = list('cat')  #----------------------------------------
    population[1].genes = list('gag')  #----------------------------------------


def draw():
    for phrase in population:
        phrase.calculate_fitness(target)

    matingpool = []  # Start with an empty mating pool.

    for phrase in population:
        """n is equal to fitness times 100. 100 is an arbitrary way to scale the
        percentage of fitness to a larger integer value."""

        n = floor(phrase.fitness * 100)
        
        print(phrase.genes); print(n)  #----------------------------------------

        for _ in range(n):
            """Add each member of the population to the mating pool n times."""
            matingpool.append(phrase)

    for m in matingpool:  #-----------------------------------------------------
        print(m.genes)    #-----------------------------------------------------

    parenta = random_choice(matingpool)
    parentb = random_choice(matingpool)

    child = parenta.crossover(parentb)  # A function for crossover
    child.mutate()  # A function for mutation




    no_loop()

def key_pressed():
    if key == 'x':
        exit_sketch()
    