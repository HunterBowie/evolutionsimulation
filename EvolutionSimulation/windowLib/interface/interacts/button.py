import pygame
from .interact import Interact
from .entity import Entity
class Button(Interact):
    RELEASE_DELAY = 50
    def __init__(self, x, y, image, clicked_image, text, triggers, label=None, scale=None, positioner=None):
        super().__init__(label, triggers, True)
        self.entity = Entity(x, y, image.get_width(), image.get_height())
        self.current_image = image
        self.image = image
        self.clicked_image = clicked_image
        if clicked_image == None:
            self.clicked_image = image
    
        if scale:
            image_scale = (int(self.image.get_width()*scale[0]), int(self.image.get_height()*scale[1]))
            clicked_image_scale = (int(self.clicked_image.get_width()*scale[0]), int(self.clicked_image.get_height()*scale[1]))

            self.image = pygame.transform.scale(self.image, image_scale)
            self.clicked_image = pygame.transform.scale(self.clicked_image, clicked_image_scale)

            self.entity = Entity(x, y, self.image.get_width(), self.image.get_height())
        
        if positioner:
            positioner.position_interact(self)
        
        self.text = text
        if self.text:
            self.text.center(self.image.get_rect())

        self.clicked_timer = pygame.time.get_ticks()-Button.RELEASE_DELAY


    def update(self):
        pos = pygame.mouse.get_pos()
        if self.entity.rect.collidepoint(pos):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.clicked_timer = pygame.time.get_ticks()

        now = pygame.time.get_ticks()
        if now - self.clicked_timer < Button.RELEASE_DELAY:
            self.current_image = self.clicked_image
        else:
            self.current_image = self.image

    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.entity.rect.collidepoint(pos):
                self.trigger()
                self.clicked_timer = pygame.time.get_ticks()
            
    
    def render(self, screen):
        image = self.current_image.copy()
        if self.text:
            self.text.render(image)
        screen.blit(image, self.entity.get_pos())
