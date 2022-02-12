import pygame, random
from ...constants import Constants
from ...config import Config
from .creature.creature import Creature
from .creature.brain.genome import Genome
from .plant import Plant
from .wall import Wall

class World:
    def __init__(self, x, y):
        self.map = self.create_empty_map()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, Constants.CELL_WIDTH*Constants.MAP_COLS, Constants.CELL_WIDTH*Constants.MAP_ROWS)
        self.creatures = {}
        self.started = True
    
    def move_creature(self, creature, move_x, move_y):
        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                if self.map[row][col] == creature:
                    new_row, new_col = row+move_y, col+move_x
                    if self.is_valid_row_col(new_row, new_col):
                        if self.map[new_row][new_col] == None:
                            self.move_entity(row, col, new_row, new_col)
                            return True
                        elif self.map[new_row][new_col].type == "plant":
                            self.move_entity(row, col, new_row, new_col)
                            creature.food_eaten += 1
                        return False

    def get_adjacent_entities(self, entity):
        entity_row_col = 0, 0
        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                if self.map[row][col] == entity:
                    entity_row_col = row, col
        adjacents = [
        (entity_row_col[0] - 1, entity_row_col[1]),
        (entity_row_col[0] + 1, entity_row_col[1]),
        (entity_row_col[0], entity_row_col[1] - 1),
        (entity_row_col[0], entity_row_col[1] + 1)]
        adjacent_entities = []
        for row_col in adjacents:
            row, col = row_col
            if row > Constants.MAP_ROWS-1:
                continue
            if col > Constants.MAP_COLS-1:
                continue
            if row == 0 or col == 0:
                continue
            if self.map[row][col] == None:
                continue
            adjacent_entities.append(self.map[row][col])
        return adjacent_entities
        
        

        
    
    def is_valid_row_col(self, row, col):
        if row < 0 or col < 0:
            return False
        if row > Constants.MAP_ROWS-1 or col > Constants.MAP_COLS-1:
            return False
        return True

    def move_entity(self, row, col, new_row, new_col):
        world_entity = self.map[row][col]
        self.map[row][col] = None
        self.map[new_row][new_col] = world_entity
    
    def get_entity_row_col(self, world_entity):
        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                if self.map[row][col] == world_entity:
                    return row, col
    
    def get_pos_row_col(self, pos):
        x, y = self.x, self.y
        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                rect = pygame.Rect(x, y, Constants.CELL_WIDTH, Constants.CELL_WIDTH)
                if rect.collidepoint(pos):
                    return row, col
                x += Constants.CELL_WIDTH
            x = self.x
            y += Constants.CELL_WIDTH
    
    def delete_entity(self, entity):
        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                if self.map[row][col] == entity:
                    self.map[row][col] = None

    
    
    def start(self):
        for creature_group in range(len(Config.CREATURE_SPOTS.keys())):
            self.creatures[creature_group] = []
        
        self.new_generation()


    def generate_plants(self):
        plant_spots = Config.PLANT_SPOTS.copy()
        for i in range(len(plant_spots)):
            row, col = plant_spots.pop(0)
            self.map[row][col] = Plant(self)

    def generate_walls(self):
        for row,col in Config.WALL_SPOTS:
            self.map[row][col] = Wall(self)

    def new_generation(self):
        self.map = self.create_empty_map()

        for creature_group in range(len(Config.CREATURE_SPOTS.keys())):
            creature_spots = Config.CREATURE_SPOTS[creature_group].copy()
            
            random.shuffle(creature_spots)
            

            if self.creatures[creature_group]:
                creature_scores = [Config.get_selection_score(creature, self.get_entity_row_col(creature)) for creature in self.creatures[creature_group]]
                ranked_creatures = [(creature, score) for (score,creature) in sorted(zip(creature_scores,self.creatures[creature_group]), key=lambda pair: pair[0])]
                ranked_creatures.reverse()
                
                self.creatures[creature_group].clear()

                if len(set(creature_scores)) <= 1:
                    for creature, score in ranked_creatures:
                        row, col = creature_spots.pop()
                        self.new_creature(row, col, Genome.create(creature, random.choice(ranked_creatures)[0]), creature_group)
                else:
                    top_creatures = [creature for (creature, score) in ranked_creatures if score > 0]
                    
                    creature_combinations = []
                    
                    if len(top_creatures) == 1:
                        for i in range(Config.GEN_SIZE):
                            creature_combinations.append((random.choice(ranked_creatures)[0], top_creatures[0])) 
                    else:
                        while len(creature_combinations) < Config.GEN_SIZE:
                            for creature in top_creatures:
                                creature_combinations.append((creature, random.choice(ranked_creatures)[0]))
                                if len(creature_combinations) == Config.GEN_SIZE:
                                    break

                    # creature_combinations = []
                    # top_creatures = ranked_creatures[:len(ranked_creatures)//2]
                    # for creature1, score in top_creatures:
                    #     for creature2, score in top_creatures:
                    #         if len(creature_combinations) < Config.GEN_SIZE:
                    #             if not (creature1, creature2) in creature_combinations:
                    #                 if not (creature2, creature1) in creature_combinations:
                    #                     creature_combinations.append((creature1, creature2))
                            
                    
                    random.shuffle(creature_combinations)

                    for creature1, creature2 in creature_combinations:
                        row, col = creature_spots.pop()
                        self.new_creature(row, col, Genome.create(creature1, creature2), creature_group)

            else:
                try:
                    for i in range(Config.GEN_SIZE):
                        try:
                            row, col = creature_spots.pop(random.randint(0, len(creature_spots)-1))
                        except ValueError:
                            row, col = creature_spots.pop(0)
                        self.new_creature(row, col, Genome.random(), creature_group)
                except IndexError:
                    raise ValueError(f"config.txt has {len(Config.CREATURE_SPOTS[creature_group])} spots for group {creature_group} and config.py has {Config.GEN_SIZE} creatures for each group")  
        self.generate_plants()
        self.generate_walls()
                

                


    
    def new_creature(self, row, col, genome, group):
        creature = Creature(self, genome, group)
        self.map[row][col] = creature
        self.creatures[group].append(creature)
        
    
    def create_empty_map(self):
        map = []
        for i in range(Constants.MAP_ROWS):
            new_row = []
            for i in range(Constants.MAP_COLS):
                new_row.append(None)
            map.append(new_row)
        return map

    def get_area_entities(self, start_row, start_col, end_row, end_col, filter=None):
        entities = []
        for row in range(start_row, end_row+1):
            for col in range(start_col, end_col+1):
                entity = self.map[row][col]
                if entity:
                    if filter:
                        if entity.type == filter:
                            entities.append(entity)
                    else:
                        entities.append(entity)
        return entities

    def get_area_entity_locs(self, start_row, start_col, end_row, end_col, filter=None):
        entity_locs = []
        for row in range(start_row, end_row+1):
            for col in range(start_col, end_col+1):
                entity = self.map[row][col]
                if entity:
                    if filter:
                        if entity.type == filter:
                            entity_locs.append((row, col))
                    else:
                        entity_locs.append((row, col))
        return entity_locs

    def get_entities(self):
        entities = []
        for row in self.map:
            for entity in row:
                if entity:
                    entities.append(entity)
        return entities

    
    def update(self):
        for entity in self.get_entities():
            entity.update()

    def render(self, screen):
        x = self.x
        y = self.y

        for row in range(Constants.MAP_ROWS):
            for col in range(Constants.MAP_COLS):
                surf = pygame.Surface((Constants.CELL_WIDTH, Constants.CELL_WIDTH))
                cell = self.map[row][col]
                if cell:
                    surf.fill(cell.color)
                else:
                    surf.fill(Constants.WHITE)
                screen.blit(surf, (x, y))
                x += Constants.CELL_WIDTH
            x = self.x
            y += Constants.CELL_WIDTH

