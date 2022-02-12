import pygame, json
from .paths import Paths

class Config:
    GEN_SIZE = 100
    GEN_MAX_UPDATES = 100
    GENOME_SIZE = 10
    GENOME_MUTATION_CHANCE = 5 
    UPDATE_DELAY = 0


    # Map
    WALL_SPOTS = []
    CREATURE_SPOTS = {}
    PLANT_SPOTS = []

    @staticmethod
    def append_template(wall_spots=None, plant_spots=None, creature_spots=None):
        if wall_spots:
            Config.WALL_SPOTS = wall_spots + Config.WALL_SPOTS

        elif plant_spots:
            Config.PLANT_SPOTS = plant_spots + Config.PLANT_SPOTS

        elif creature_spots:
            Config.CREATURE_SPOTS = creature_spots + Config.CREATURE_SPOTS
 

    

    @staticmethod
    def init():
        data = Paths.read_text(Paths.TEXT+"/config.txt")
        data = json.loads(data)
        Config.WALL_SPOTS = data[0]
        Config.CREATURE_SPOTS = {}
        for key in data[2]:
            Config.CREATURE_SPOTS[int(key)] = data[2][key]
        Config.PLANT_SPOTS = data[1]



    @staticmethod
    def get_selection_score(creature, pos):
        return creature.food_eaten
    





