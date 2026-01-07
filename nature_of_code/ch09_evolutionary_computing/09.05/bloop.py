from py5 import circle, fill, noise, Py5Vector2D, stroke, random


class Bloop:
    
    def __init__(self, x: float, y: float):
        self.position = Py5Vector2D(x, y)
        # Each bloop will use a different part of the 1D noise space.
        self.xoff = random(1000)
        self.yoff = random(1000)
        self.max_speed = 5
        self.r = 8

    def update(self):
        """Assign simple movement and velocity with Perlin noise."""
        vx = remap(noise(self.xoff), 0, 1, -self.max_speed, self.max_speed)
        vy = remap(noise(self.yoff), 0, 1, -self.max_speed, self.max_speed)
        self.xoff += 0.01
        self.yoff += 0.01
        velocity = Py5Vector2D(vx, vy)
        self.position.add(velocity)

    def show(self):
        """A bloop is a circle."""
        stroke(0)
        fill(127)
        circle(self.position.x, self.position.y, self.r * 2)