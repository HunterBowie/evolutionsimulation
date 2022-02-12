from ..windowLib.window import Window
from .simulationController import SimulationController
from ..constants import Constants
from .world import World

class SimulationMaker(Window):
    BG_COLOR = Constants.LIGHT_BLUE
    def __init__(self):
        super().__init__(Constants.SCREEN_SIZE)
        self.set_interface(SimulationController)
        self.set_caption("Evolution Simulation Maker")
        self.entity_type = None
        self.world = World(100, 100)
    
    def update(self):
        self.world.render(self.screen)
        super().update()