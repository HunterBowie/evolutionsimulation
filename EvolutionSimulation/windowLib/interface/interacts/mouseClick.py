import pygame
from .interact import Interact

class MouseClick(Interact):
    def __init__(self, triggers, label=None, rect=None, mode="down"):
        super().__init__(label, triggers, False)
        self.rect = rect
        self.mode = mode

    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        mouse_focused = False

        if self.rect is None:
            mouse_focused = pygame.mouse.get_focused()

        elif self.rect.collidepoint(pos):
            mouse_focused = True
        
        if mouse_focused:
            if self.mode == "down":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.trigger()
            elif self.mode == "up":
                if event.type == pygame.MOUSEBUTTONUP:
                    self.trigger()
            elif self.mode == "hold":
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    self.trigger()
            else:
                raise Exception("mouseclick gived invalid mode arg")
