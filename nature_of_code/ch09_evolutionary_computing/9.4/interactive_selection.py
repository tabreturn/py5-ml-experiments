# https://natureofcode.com/genetic-algorithms/#interactive-selection

from population import Population

POPULATION_SIZE = 8  # This is a very small population!
# Pretty high mutation. Our population is small; we need to enforce variety.
MUTATION_RATE = .05


def setup():
    global monospace, population
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)
    color_mode(RGB, 1)
    # Create the population.
    population = Population(MUTATION_RATE, POPULATION_SIZE)
    # A p5.js-'like' button
    text_font(monospace); text_size(11); fill(0)
    text('evolve new generation', 20, 29)
    no_fill(); rect(10, 10, 158, 30)


def mouse_pressed():
    # For the p5.js-'like' button
    if 10 <= mouse_x <= 168 and 10 <= mouse_y <= 40:
        next_generation()


def draw():
    background(1)
    population.show()  # Draw the flowers.
    # Check for increasing fitness.
    population.rollover(mouse_x, mouse_y)
    text(f'Generation {population.generations}', 12, height - 40)


def next_generation():
    """If the button is pressed, evolve the next generation."""
    population.selection()
    population.reproduction()