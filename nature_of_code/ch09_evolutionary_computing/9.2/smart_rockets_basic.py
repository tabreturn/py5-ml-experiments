# https://natureofcode.com/genetic-algorithms/#evolving-forces-smart-rockets

from dna import DNA
from population import Population
from rocket import Rocket

LIFE_SPAN = 500
life_counter = 0


def setup():
    global population, target
    size(500, 500)
    # Step 1: Create the population.
    # Try different values for the mutation rate and population size.
    population = Population(.01, 50)


def draw():
    global life_counter
    background(255)
    # The revised GA
    if life_counter < LIFE_SPAN:
        # Step 2: The rockets live until life_counter reaches LIFE_SPAN.
        population.live()
        life_counter += 1
    else:
        # When lifeSpan is reached, reset lifeCounter and evolve the next gen.
        # (steps 3 and 4, selection and reproduction).
        life_counter = 0
        population.fitness()
        population.selection()
        population.reproduction()
    




    print(frame_count)


def mouse_pressed():
    '''Move the target if the mouse is clicked.
    The rockets will adapt to the new target.'''
    target.x = mouse_x
    target.y = mouse_y


def key_pressed():
    '''Handle keyboard controls for stepping, looping, pausing, and quitting.'''
    if key == 'c': no_loop()
    if key == 'z': redraw()
    if key == 'x': loop()
    if key == 'q': exit_sketch()
