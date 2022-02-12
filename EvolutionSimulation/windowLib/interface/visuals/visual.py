import pygame

class Visual:
    def __init__(self, x, y, surf=None):
        self.x = x
        self.y = y
        self.surf = surf
    
    def render(self, screen):
        if self.surf:
            screen.blit(self.surf, (self.x, self.y))
    
    def get_width(self):
        return self.surf.get_width()
    
    def get_height(self):
        return self.surf.get_height()
    
    @staticmethod
    def create_circle(x, y, radius, color):
        surf = pygame.Surface((radius*2, radius*2))
        pygame.draw.circle(surf, color, (x, y), radius)
        return Visual(x, y, surf)
    
    @staticmethod
    def create_rect(x, y, width, height, color):
        surf = pygame.Surface((width, height))
        surf.fill(color)
        return Visual(x, y, surf)
    