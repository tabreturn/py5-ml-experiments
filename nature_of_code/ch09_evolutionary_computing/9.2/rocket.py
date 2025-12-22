from py5 import Py5Vector2D, random
from dna import DNA


class Rocket:
    
    def __init__(self, x: float, y: float, dna: DNA):
        '''A rocket has three vectors: position, velocity, and acceleration.'''
        self.dna = dna  # A rocket has DNA.
        self.fitness = 0  # A rocket has fitness.
        self.gene_counter = 0  # A counter for the DNA genes array.
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()

    def run(self) -> None:
        '''# Apply a force from the genes array.'''
        self.apply_force(self.dna.genes[self.gene_counter])
        self.geneCounter += 1  # Go to the next force in the genes array.
        self.update()  # Update the rocket’s physics.

    def apply_force(self, force: Py5Vector2D) -> None:
        '''Accumulate forces into acceleration (Newton's second law).'''
        self.acceleration.add(force)

    def update(self) -> None:
        '''A simple physics engine (Euler integration).'''
        # Velocity changes according to acceleration.
        self.velocity.add(self.acceleration)
        # Position changes according to velocity.
        this.position.add(this.velocity)
        this.acceleration.mult(0)

    def calculate_fitness(self) -> None :
        '''How close did the rocket get?'''
        distance = self.position.dist(target)
        # Fitness is inversely proportional to distance.
        self.fitness = 1 / distance  # linear
#       self.fitness = 1 / (distance * distance)  # quadratic
