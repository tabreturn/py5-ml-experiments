# https://natureofcode.com/genetic-algorithms/#coding-the-genetic-algorithm

from dna import DNA
#from population import Population

mutationrate = 0.1            # Mutation rate
populationsize = 5           # Population size
population = []                # Population list
target = 'cat'  # Target phrase


def setup():
    global monospace, population
    size(640, 360)
    monospace = create_font('DejaVu Sans Mono', 32)

    # Step 1: Initialization
    for _ in range(populationsize):
        population.append(DNA(len(target)))


def draw():  # Step 2: Selection

    for phrase in population:  # Step 2a: Calculate fitness.
        phrase.calculate_fitness(target)
    
    print('population:')
    print(*(dna.genes for dna in population), sep="\n")

    matingpool = []  # Step 2b: Build the mating pool.

    for phrase in population:
        # Add each member n times according to its fitness score.
        n = floor(phrase.fitness * 100)
        for _ in range(n):
            matingpool.append(phrase)
        # Add one of each, even if score is zero (so always enough to mate).
        matingpool.append(phrase)
    
    print(f'total mating pool: {len(matingpool)}')
    
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
    
    print(f'parents: \n{parenta.genes}\n{parentb.genes}')

    background(255)
    fill(0)
    text_font(monospace)
    text_size(12)
    text('Best phrase:', 10, 32)
    text_size(24)
    text('answer', 10, 64)
    
    statstext = (
      f'total generations:     {frame_count}\n'
      f'average fitness:       nf(population.getAverageFitness(), 0, 2)\n'
      f'total population:      {populationsize}\n'
      f'mutation rate:         {floor(mutationrate * 100)}%'
    )

# 
    text_size(12)
    text(statstext, 10, 96)
#    textSize(8)
#    text(population.allPhrases(), width / 2, 24)

    print(f'frame count: {frame_count}')
    no_loop()



def key_pressed():
    if key == 'x':
        exit_sketch()
    if key == 'z':
        loop()
        
