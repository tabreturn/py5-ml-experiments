from py5 import circle, fill, noise, Py5Vector2D, stroke, remap, random
from dna import DNA
from food import Food


class Bloop:
    
    def __init__(self, x: float, y: float, dna: DNA):
        self.dna = dna
        self.max_speed = remap(self.dna.genes[0], 0, 1, 15, 0)
        self.r = remap(self.dna.genes[0], 0, 1, 0, 25)
        # DNA will determine size and max speed. Bigger bloop = slower it is.
        self.health = 100.  # A variable to track the bloop's health
        self.position = Py5Vector2D(x, y)
        # Each bloop will use a different part of the 1D noise space.
        self.xoff = random(1000)
        self.yoff = random(1000)

    def update(self) -> None:
        self.health -= 0.2  # Death is always looming
        # Assign simple movement and velocity with Perlin noise.
        vx = remap(noise(self.xoff), 0, 1, -self.max_speed, self.max_speed)
        vy = remap(noise(self.yoff), 0, 1, -self.max_speed, self.max_speed)
        self.xoff += 0.01
        self.yoff += 0.01
        velocity = Py5Vector2D(vx, vy)
        self.position.add(velocity)

    def dead(self) -> float:
        """A method to test whether the bloop is alive or dead."""
        return self.health < 0.0

    def eat(self, food: list[Food]):
        # Check all the food vectors.
        for i in food:
            # How far away is the bloop?
            distance = Py5Vector2D.dist(self.position, i)
            # If it is within its radius ...
            if distance < self.r:
                self.health += 100
                food.pop(i)  # ... increase health and remove the food!

    def show(self) -> None:
        """A bloop is a circle."""
        stroke(0)
        fill(127)
        circle(self.position.x, self.position.y, self.r * 2)