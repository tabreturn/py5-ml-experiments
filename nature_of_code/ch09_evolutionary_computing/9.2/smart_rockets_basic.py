class Rocket:
    
    def __init__(self, x: float, y: float):
        '''A rocket has three vectors: position, velocity, and acceleration.'''
        self.fitness = 0  # A rocket has fitness.
        self.position = Py5Vector(x, y)
        self.velocity = Py5Vector()
        self.acceleration = Py5Vector()

    def apply_force(force) -> None:
        '''Accumulate forces into acceleration (Newton's second law).'''
        self.acceleration.add(force)

    def update() -> None:
        '''A simple physics engine (Euler integration).'''
        # Velocity changes according to acceleration.
        self.velocity.add(self.acceleration)
        # Position changes according to velocity.
        this.position.add(this.velocity)
        this.acceleration.mult(0)

    def calculate_fitness() -> None :
        '''How close did the rocket get?'''
        distance = self.position.dist(target)
        # Fitness is inversely proportional to distance.
        self.fitness = 1 / distance  # linear
#       self.fitness = 1 / (distance * distance)  # quadratic


class DNA:
    def __init__(length: int):
        self.genes = []
        self.genes = [Py5Vector() for _ in range(length)]
    



def setup():
    size(500, 500)
    a = Rocket(1, 2.5)


def draw():
    print(frame_count)
