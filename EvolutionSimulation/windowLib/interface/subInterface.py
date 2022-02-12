import pygame
from .interface import Interface

class SubInterface(Interface):
    def __init__(self, interface, interacts, visuals, label=None):
        super().__init__(interface.window, interacts, visuals, False)
        self.label = label
