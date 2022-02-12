import pygame
from .brainProtocol import BrainProtocol
from .connection import Connection

class Brain:
    def __init__(self, creature):
        self.neurons = []
        self.neuron_ids = []
        self.connections = []
        self.creature = creature
        self.construct_brain()
    
    def __repr__(self):
        neuron_names = [type(neuron).__name__ for neuron in self.neurons]
        string = ""
        for name in neuron_names:
            string = string + name + " "
        return string

    
    def construct_brain(self):
        for gene in self.creature.genome:

            source_neuron = sink_neuron = None

            neuron_type = None

            # source
            if gene[0] in self.neuron_ids:
                source_neuron = self.neurons[self.neuron_ids.index(gene[1])]
                
            else:
                neuron_type = BrainProtocol.lookup_sensory(gene[0])
                source_neuron = neuron_type(self.creature)

                self.neurons.append(source_neuron)
                self.neuron_ids.append(neuron_type)
            
            # sink
            if gene[1] in self.neuron_ids:
                source_neuron = self.neurons[self.neuron_ids.index(gene[1])]
            else:
                neuron_type = BrainProtocol.lookup_action(gene[1])
                sink_neuron = neuron_type(self.creature)   
                self.neurons.append(sink_neuron)
                self.neuron_ids.append(neuron_type)
            
            # connection
            connection = Connection(source_neuron, sink_neuron, gene[2])
            self.connections.append(connection)
        
    def update(self):
        for neuron in self.neurons:
            if neuron.type == "sensory":
                neuron.update()
        for neuron in self.neurons:
            if neuron.type == "inner":
                neuron.update()
        for connection in self.connections:
            connection.update()
        for neuron in self.neurons:
            if neuron.type == "action":
                neuron.update()


            


