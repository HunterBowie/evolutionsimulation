import pygame

class Window:
    FPS = 60
    BG_COLOR = (255, 0, 0)
    def __init__(self, screen_size):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

        self.running = False
        self.interface = None
        
    
    def set_interface(self, interface):
        self.interface = interface(self)
    
    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
    
    def set_icon(self, icon):
        self.icon = icon
        pygame.display.set_icon(self.icon)
    
    def start(self):
        self.running = True
        while self.running:
            self.update()
        pygame.quit()
    
    def stop(self):
        self.running = False
    
    def update(self):
        if self.interface:
            self.interface.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

        pygame.display.update()
        self.screen.fill(self.BG_COLOR)
        self.clock.tick(self.FPS)

