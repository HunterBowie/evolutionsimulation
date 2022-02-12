import random

from EvolutionSimulation.constants import Constants
from EvolutionSimulation.simulation.world.creature.brain.brain import Brain
from .brainProtocol import BrainProtocol
from .....config import Config

class Genome:
    @staticmethod
    def random():
        genome = []
        for i in range(Config.GENOME_SIZE):
            num_source_neurons = 0
            num_sink_neurons = 0

            num_source_neurons = len(BrainProtocol.SENSORY)
            num_sink_neurons = len(BrainProtocol.ACTION)
            
            source_id = random.randint(0, num_source_neurons-1)
            sink_id = random.randint(0, num_sink_neurons-1)
            weight = random.randint(-10, 10)
            genome.append([source_id, sink_id, weight])
        return genome
    
    @staticmethod
    def mutate(genome):
        gene_index = random.randint(0, Config.GENOME_SIZE-1)
        gene = genome[gene_index]

        gene_part = random.randint(0, 2)
       
                
        mutation_amount = random.randint(-5, 5)
        gene[gene_part] += mutation_amount
        

        if gene_part == 0:
            if gene[gene_part] < 0:
                gene[gene_part] = 0
            if gene[gene_part] > len(BrainProtocol.SENSORY)-1:
                gene[gene_part] = len(BrainProtocol.SENSORY)-1

        elif gene_part == 1:
            if gene[gene_part] < 0:
                gene[gene_part] = 0
            if gene[gene_part] > len(BrainProtocol.ACTION)-1:
                gene[gene_part] = len(BrainProtocol.ACTION)-1

        
        else:
            if gene[gene_part] > 10:
                gene[gene_part] == 10
            
            




    
    @staticmethod
    def create(parent1, parent2):
        genome1, genome2 = parent1.genome, parent2.genome
        random.shuffle(genome1)
        random.shuffle(genome2)
        if random.randint(0, 1) == 1:
            genome1, genome2 = genome2, genome1
        half_genome = int(Config.GENOME_SIZE/2)
        genome = genome1[:half_genome] + genome2[half_genome:]
        if random.randint(1, 100) <= Config.GENOME_MUTATION_CHANCE:
            Genome.mutate(genome)
        return genome
    


