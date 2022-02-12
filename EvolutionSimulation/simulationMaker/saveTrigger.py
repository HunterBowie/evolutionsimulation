import json
from ..windowLib.interface.triggers import Trigger
from ..paths import Paths

class SaveTrigger(Trigger):
    def call(self, interact):
        spots = self.window.world.get_spots()
        spots = json.dumps(spots)
        Paths.write_text(Paths.TEXT+"/config.txt", spots)
        

