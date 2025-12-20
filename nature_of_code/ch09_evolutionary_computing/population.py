from dna import DNA

class Population:
    ''' A class to describe a population of virtual organisms
    In this case, each organism is just an instance of a DNA object'''

    def __init__(self, p, m, num):
        self.matingpool = []   # ArrayList which we will use for our "mating pool"
        self.generations = 0   # Number of generations
        self.finished = False  # Are we finished evolving?
        self.target = p        # Target phrase
        self.mutationrate = m  # Mutation rate
        self.perfectscore = 1
        self.best = ''
        # List to hold the current population
        self.population = [DNA(len(self.target)) for _ in range(num)]
        self.calc_fitness()

    def calc_fitness(self):
        return
        '''Fill our fitness array with a value for every member of the population'''
        for i in self.population:
            i.calculate_fitness(self.target)

#     for (let i = 0; i < this.population.length; i++) {
#      this.population[i].calcFitness(target);

# 
#   // Generate a mating pool
#   naturalSelection() {
#     // Clear the ArrayList
#     this.matingPool = [];
# 
#     let maxFitness = 0;
#     for (let i = 0; i < this.population.length; i++) {
#       if (this.population[i].fitness > maxFitness) {
#         maxFitness = this.population[i].fitness;
#       }
#     }
# 
#     // Based on fitness, each member will get added to the mating pool a certain number of times
#     // a higher fitness = more entries to mating pool = more likely to be picked as a parent
#     // a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
#     for (let i = 0; i < this.population.length; i++) {
# 
#       let fitness = map(this.population[i].fitness, 0, maxFitness, 0, 1);
#       let n = floor(fitness * 100); // Arbitrary multiplier, we can also use monte carlo method
#       for (let j = 0; j < n; j++) { // and pick two random numbers
#         this.matingPool.push(this.population[i]);
#       }
#     }
#   }
# 
#   // Create a new generation
#   generate() {
#     // Refill the population with children from the mating pool
#     for (let i = 0; i < this.population.length; i++) {
#       let a = floor(random(this.matingPool.length));
#       let b = floor(random(this.matingPool.length));
#       let partnerA = this.matingPool[a];
#       let partnerB = this.matingPool[b];
#       let child = partnerA.crossover(partnerB);
#       child.mutate(this.mutationRate);
#       this.population[i] = child;
#     }
#     this.generations++;
#   }
# 
# 
#   getBest() {
#     return this.best;
#   }
# 
#   // Compute the current "most fit" member of the population
#   evaluate() {
#     let worldrecord = 0.0;
#     let index = 0;
#     for (let i = 0; i < this.population.length; i++) {
#       if (this.population[i].fitness > worldrecord) {
#         index = i;
#         worldrecord = this.population[i].fitness;
#       }
#     }
# 
#     this.best = this.population[index].getPhrase();
#     if (worldrecord === this.perfectScore) {
#       this.finished = true;
#     }
#   }
# 
#   isFinished() {
#     return this.finished;
#   }
# 
#   getGenerations() {
#     return this.generations;
#   }
# 
#   // Compute average fitness for the population
#   getAverageFitness() {
#     let total = 0;
#     for (let i = 0; i < this.population.length; i++) {
#       total += this.population[i].fitness;
#     }
#     return total / (this.population.length);
#   }
# 
#   allPhrases() {
#     let everything = "";
# 
#     let displayLimit = min(this.population.length, 51);
# 
#     for (let i = 0; i < displayLimit; i++) {
#       everything += this.population[i].getPhrase();
#       if (i % 3 == 2) everything += "\n";
#       else everything += " ";
#     }
#     return everything;
#   }
# }
