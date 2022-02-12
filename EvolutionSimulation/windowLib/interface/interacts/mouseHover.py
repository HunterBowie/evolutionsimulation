import pygame
from .interact import Interact

class MouseHover(Interact):
    def __init__(self, rect, triggers, label=None):
        super().__init__(label, triggers, False)
        self.rect = rect
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.trigger()
