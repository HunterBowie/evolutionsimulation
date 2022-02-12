
import pygame, random
from ..constants import Constants


class World:
    def __init__(self, x, y):
        self.map = self.create_empty_map()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, Constants.CELL_WIDTH*Constants.MAP_COLS, Constants.CELL_WIDTH*Constants.MAP_ROWS)

    def get_spots(self):
        walls, creatures, plants = [], {}, []
        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                entity = self.map[row][col]
                if entity:
                    if entity == ("wall"):
                        walls.append((row, col))
                    elif entity == ("creature", 0):
                        if not 0 in creatures:
                            creatures[0] = []
                        creatures[0].append((row, col))
                    elif entity == ("creature", 1):
                        if not 1 in creatures:
                            creatures[1] = []
                        creatures[1].append((row, col))
                    elif entity == ("plant"):
                        plants.append((row, col))
            

        return walls, plants, creatures

    
    def create_empty_map(self):
        map = []
        for i in range(Constants.MAP_ROWS):
            new_row = []
            for i in range(Constants.MAP_COLS):
                new_row.append(None)
            map.append(new_row)
        return map
    
    def translate_pos(self, pos):
        pos = pos[0]-self.x, pos[1]-self.y
        return pos[1]//Constants.CELL_WIDTH, pos[0]//Constants.CELL_WIDTH
    
    def change_entity(self, pos, entity):
        row, col = self.translate_pos(pos)
        self.map[row][col] = entity
    


    def render(self, screen):
        x = self.x
        y = self.y

        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                surf = pygame.Surface((Constants.CELL_WIDTH, Constants.CELL_WIDTH))
                cell = self.map[row][col]
                if cell == ("plant"):
                    surf.fill(Constants.GREEN)
                elif cell == ("creature", 0):
                    surf.fill(Constants.YELLOW)
                elif cell == ("creature", 1):
                    surf.fill(Constants.ORANGE)
                elif cell == ("wall"):
                    surf.fill(Constants.BLACK)
                else:
                    surf.fill(Constants.WHITE)
                screen.blit(surf, (x, y))
                x += Constants.CELL_WIDTH
            x = self.x
            y += Constants.CELL_WIDTH

