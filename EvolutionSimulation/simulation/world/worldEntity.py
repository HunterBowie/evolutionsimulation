import pygame

class WorldEntity:
    def __init__(self, world, color, type):
        self.color = color
        self.world = world
        self.type = type
    
    def update(self):
        pass
        