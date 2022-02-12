import pygame
from .interact import Interact

class MouseMove(Interact):
    def __init__(self, triggers, label=None):
        super().__init__(label, triggers, False)
        self.init = True
        self.mouse_pos = (0, 0)
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.init:
            self.mouse_pos = pos
            self.init = False
        
        else:
            if pos != self.mouse_pos:
                self.mouse_pos = pos
                self.trigger()
    
    def get(self):
        return self.mouse_pos