import pygame
from ..worldEntity import WorldEntity
from .brain.brain import Brain
from ....constants import Constants
from .brain.genome import Genome

class Creature(WorldEntity):
    ID = 0
    COLORS = [Constants.YELLOW, Constants.ORANGE, Constants.RED]
    def __init__(self, world, genome, group):
        super().__init__(world, Creature.COLORS[group], "creature")
        self.genome = genome
        self.brain = Brain(self)
        self.age = 0
        self.food_eaten = 0
        self.group = group
        self.id = Creature.ID
        Creature.ID += 1

    def update(self):
        self.age += 1
        self.brain.update()
    
    def __repr__(self):
        return str(self.id)
    
