import pygame
from ..windowLib.interface.interface import Interface
from ..windowLib.interface.visuals import Text
from ..windowLib.interface.interacts import MouseClick
from .triggers import CreateCreatureTrigger

class SimulationController(Interface):
    def __init__(self, simulation):

        interacts = [
        ]
        visuals = [
            Text(720, 50, "cycle_time 0", size=20),
            Text(720, 100, "generation_size 0", size=20),
            Text(720, 150, "mutation_chance 0", size=20),
            Text(720, 200, "brain_size 0", size=20),

            Text(300, 25, "Generation 0"),

        ]
        
        super().__init__(simulation, interacts, visuals)
    
    def update(self):
        # BAD CODE
        for visual in self.visuals:
            if visual.get()[:10] == "Generation":
                visual.set("Generation " + str(self.window.settings["generation"]))
            else:
                string = visual.get()
                string = string.split(" ")
                for setting_name in self.window.settings.keys():
                    if setting_name == string[0]:
                        value = self.window.settings[setting_name]
                        visual.set(f"{setting_name} {value}")
        super().update()



