import pygame
from .worldEntity import WorldEntity
from ...constants import Constants

class Wall(WorldEntity):
    def __init__(self, world):
        super().__init__(world, Constants.BLACK, "wall")
        