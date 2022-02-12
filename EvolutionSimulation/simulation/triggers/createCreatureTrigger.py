import pygame
from ...windowLib.interface.triggers import Trigger
from ..world.creature.brain.genome import Genome

class CreateCreatureTrigger(Trigger):
    def __init__(self, simulator):
        super().__init__(simulator)

    def call(self, interact):
        row, col = self.window.world.get_row_col_from_pos(pygame.mouse.get_pos())
        self.window.world.new_creature(row, col, Genome.random())