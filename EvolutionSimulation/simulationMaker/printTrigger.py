from ..windowLib.interface.triggers import Trigger

class PrintTrigger(Trigger):
    def call(self, interact):
        print(self.window.world.get_spots())