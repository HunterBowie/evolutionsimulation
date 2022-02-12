import pygame
from ..constants import Constants
from ..windowLib.interface.interface import Interface
from ..windowLib.interface.interacts import Button
from .changeEntityTypeTrigger import ChangeEntityTypeTrigger
from ..windowLib.interface.visuals import Text
from .saveTrigger import SaveTrigger
from .printTrigger import PrintTrigger

def create_surf(size, color):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf


class SimulationController(Interface):
    def __init__(self, window):
        interacts = [
            Button(750, 150, create_surf((50, 50), Constants.YELLOW), None, None, [ChangeEntityTypeTrigger(window, ("creature", 0))]),
            Button(750, 250, create_surf((50, 50), Constants.ORANGE), None, None, [ChangeEntityTypeTrigger(window, ("creature", 1))]),

            Button(750, 350, create_surf((50, 50), Constants.GREEN), None, None, [ChangeEntityTypeTrigger(window, ("plant"))]),
            Button(750, 450, create_surf((50, 50), Constants.BLACK), None, None, [ChangeEntityTypeTrigger(window, ("wall"))]),
            Button(750, 550, create_surf((50, 50), Constants.WHITE), None, None, [ChangeEntityTypeTrigger(window, None)]),

            Button(100, 10, create_surf((100, 50), Constants.WHITE), None, Text(0, 0, "Save"), [SaveTrigger(window)]),
            Button(250, 10, create_surf((100, 50), Constants.WHITE), None, Text(0, 0, "Print"), [PrintTrigger(window)])

        ]

        super().__init__(window, interacts, [])
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if self.window.world.rect.collidepoint(mouse_pos):
                self.window.world.change_entity(mouse_pos, self.window.entity_type)
        super().update()
    
  