# https://natureofcode.com/genetic-algorithms/#ecosystem-simulation

from world import World


def setup():
    global world
    size(640, 240)
    # The world starts with 20 bloops and 20 pieces of food.
    world = World(20)

def draw():
    background(255)
    world.run()