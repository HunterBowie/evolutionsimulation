import pygame, math

class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.update_rect()
    
    def unpack(self):
        return self.x, self.y, self.width, self.height
    
    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        self.update_rect()
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.update_rect()
    
    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update_pos(self):
        self.x = self.rect.x
        self.y = self.rect.y 

    def get_pos(self):
        return self.x, self.y
    
    def update(self):
        pass
    
    @staticmethod
    def make_rects_entities(rects):
        entities = []
        for rect in rects:
            entities.append(Entity(rect.x, rect.y, rect.width, rect.height))
        
        return entities

    @staticmethod
    def move_by_degrees(angle, speed):
        radians = math.radians(-angle) 
        x, y = speed * math.cos(radians), speed * math.sin(radians)
        return x, y
    
    def calc_angle(self, pos):
        rel_x, rel_y = pos[0] - self.x, pos[1] - self.y
        angle = ((180 / math.pi) * -math.atan2(rel_y, rel_x))
        return angle        
    
    def get_dist(self, entity):
        return math.dist(self.get_pos(), entity.get_pos())
    
    def collide_entity(self, entity):
        return self.collide_rect(entity.rect)

    def move_and_collide(self, move_x, move_y, entities):
        self.x += move_x
        self.update_rect()
        for entity in entities:
            if self.collide_entity(entity):
                if move_x > 0:
                    self.rect.right = entity.rect.left
                else:
                    self.rect.left = entity.rect.right
        self.update_pos()
        self.y += move_y
        self.update_rect()
        for entity in entities:
            if self.collide_entity(entity):
                if move_y > 0:
                    self.rect.bottom = entity.rect.top
                else:
                    self.rect.top = entity.rect.bottom
        self.update_pos()
    
    def collide_pos(self, pos):
        return self.rect.collidepoint(pos)
    
    def collide_rect(self, rect):
        return self.rect.colliderect(rect)
    

        
