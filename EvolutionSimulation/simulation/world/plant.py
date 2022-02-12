import pygame
from .worldEntity import WorldEntity
from ...constants import Constants

class Plant(WorldEntity):
    def __init__(self, world):
        super().__init__(world, Constants.GREEN, "plant")