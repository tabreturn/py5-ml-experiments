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
    def __init__(self, length: int):
        '''The genetic sequence is an array of vectors.'''
        self.max_force = .1  # How strong can the thrusters be?
        # Notice that the length of genes is equal to a global lifeSpan variable.
        self.genes = [
          # Scale the vectors randomly, but not stronger than the maximum force.
          Py5Vector2D().random() * random(0, self.max_force)
          for _ in range(length)
        ]

    



def setup():
    size(500, 500)
    a = DNA(5)
    print(a.genes)
    


def draw():
    print(frame_count)









    no_loop()

def key_pressed():
    '''Handle keyboard controls for stepping, looping, pausing, and quitting.'''
    if key == 'c': no_loop()
    if key == 'z': redraw()
    if key == 'x': loop()
    if key == 'q': exit_sketch()
