from dna import DNA
from rocket import Rocket


class Population:
    def __init__(self, mutation: float, length: int):
        '''Population has variables to keep track of the mutation rate, current
        population array, and number of generations.'''
        self.mutation_rate = mutation  # Mutation rate
        self.generations = 0  # Number of generations
        # Array to hold the current population
        self.population = [Rocket(320, 220, DNA(length)) for _ in range(length)]


    def fitness(self) -> None:
        '''Calculate the fitness for each rocket.'''
        (rocket.calculate_fitness() for rocket in self.population)

    def selection(self) -> None:
        '''The selection method normalizes all the fitness values.'''
        # Sum all the fitness values.
        total_fitness = sum(rocket.fitness for rocket in self.population)
        # Divide by the total to normalize the fitness values.
        for rocket in self.population:
            rocket.fitness /= total_fitness

    def reproduction(self) -> None:
        new_population = []  # Separate the array for the next generation.

        for _ in range(len(self.population)):
            # Now use the weighted selection algorithm.
            parent_a = self.weighted_selection()
            parent_b = self.weighted_selection()
            child = parent_a.crossover(parent_b)
            child.mutate(this.mutation_rate)
            # Rocket goes in the new population.
            new_population.append(Rocket(320, 240, child))

        # Now the new population is the current one.
        self.population = new_population

    def live(self) -> None:
        '''The run() method takes care of the simulation, updates the rocket's
        position, and draws it to the canvas.'''
        (rocket.run() for rocket in self.population)
