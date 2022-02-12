import pygame

class Timer:
    def __init__(self):
        self.ticks = 0
        self.stopped = False
        self.stop_time = 0
        self.wait_timer = pygame.time.get_ticks()
    
    def start(self):
        self.stopped = False
        self.stop_time = 0
        self.ticks = pygame.time.get_ticks()
    
    def stop(self):
        self.stopped = True
        self.stop_time = pygame.time.get_ticks()
    
    def wait(self, time):
        now = pygame.time.get_ticks()
        if now - self.wait_timer >= time:
            self.wait_timer = now
            return True
        return False


            
    
    def get(self):
        if self.stopped:
            return self.stop_time-self.ticks
        return pygame.time.get_ticks()-self.ticks
