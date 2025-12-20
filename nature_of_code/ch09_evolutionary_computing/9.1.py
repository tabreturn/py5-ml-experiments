# https://natureofcode.com/genetic-algorithms/#coding-the-genetic-algorithm

from DNA import DNA

mutationrate = 0.01            # Mutation rate
populationsize = 150           # Population size
population = []                # Population array
target = "to be or not to be"  # Target phrase

def setup():
    global population
    size(640, 360)

    # Step 1: Initialization
    for _ in range(populationsize):
        population.append(DNA(len(target)))


def draw():
    # Step 2: Selection

    for phrase in population:  # Step 2a: Calculate fitness.
        phrase.calculate_fitness(target)

    matingpool = []  # Step 2b: Build the mating pool.

    for phrase in population:
        # Add each member n times according to its fitness score.
        n = floor(phrase.fitness * 100)
        for _ in range(n):
            matingpool.append(phrase)

    for i, _ in enumerate(population):  # Step 3: Reproduction
        parenta = random_choice(matingpool)
        parentb = random_choice(matingpool)

        child = parenta.crossover(parentb)  # Step 3a: Crossover
        child.mutate(mutationrate)  # Step 3b: Mutation
        
        ''' Note that you are overwriting the population with the new children.
        When draw() loops, you will perform all the same steps with the new
        population of children.'''
        population[i] = child

        # Step 4: Repetition. Go back to the beginning of draw()!


def key_pressed():
    if key == 'x':
        exit_sketch()
