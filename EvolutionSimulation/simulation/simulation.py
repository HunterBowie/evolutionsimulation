from ..windowLib.window import Window
from ..windowLib.timer import Timer
from ..constants import Constants
from ..config import Config
from .world.world import World
from ..paths import Paths
from .simulationController import SimulationController

class Simulation(Window):
    BG_COLOR = Constants.LIGHT_BLUE
    def __init__(self):
        super().__init__(Constants.SCREEN_SIZE)
        self.set_caption("Evolution Simulation")
        self.world = World(100, 100)
        self.set_interface(SimulationController)
        self.world.start()
        self.world_timer = Timer()
        self.settings = {
            "cycle_time": 0,
            "generation_size": Config.GEN_SIZE,
            "mutation_chance": Config.GENOME_MUTATION_CHANCE,
            "brain_size": Config.GENOME_SIZE,
            "generation": 0
        }
        self.pause = False

    
    def update(self):
        if self.world_timer.wait(Config.UPDATE_DELAY) and not self.pause:
            self.world.update()
            self.settings["cycle_time"] += 1
            if self.settings["cycle_time"] == Config.GEN_MAX_UPDATES:
                self.settings["cycle_time"] = 0
                self.settings["generation"] += 1
                # if self.settings["generation"] == 4:
                #     Config.CREATURE_SPOTS[1] = []
                #     Config.append_template(wall_spots=[(0, 14), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14), (15, 14), (16, 14), (17, 14), (18, 14), (19, 14), (20, 14), (21, 14), (22, 14), (23, 14), (24, 14), (25, 14), (26, 14), (27, 14), (28, 14), (29, 14)])
                #     Config.GEN_SIZE = Config.GEN_SIZE//2
                #     self.settings["generation_size"] = Config.GEN_SIZE
                #     i = 0
                #     group1_row_cols = []
                #     for row, col in Config.CREATURE_SPOTS[0]:
                #         i += 1
                #         if col > 14:
                #             group1_row_cols.append((row, col))

                #     for row, col in group1_row_cols:
                #         Config.CREATURE_SPOTS[0].remove([row, col])
                #         Config.CREATURE_SPOTS[1].append([row, col])
                #     self.world.creatures[1] = []
                self.world.new_generation()
        
            
            
        
        super().update() 
        self.world.render(self.screen)