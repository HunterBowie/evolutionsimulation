import pygame
from .interact import Interact

class KeyPress(Interact):
    def __init__(self, key, triggers, label=None, on_held=False):
        super().__init__(label, triggers, False)
        self.key = key
        self.on_held = on_held

    def eventloop(self, event):
        if event.type == pygame.KEYDOWN and not self.on_held:
            if event.key == self.key:
                self.trigger()
    
    def update(self):
        if pygame.key.get_pressed()[self.key] and self.on_held:
            self.trigger()