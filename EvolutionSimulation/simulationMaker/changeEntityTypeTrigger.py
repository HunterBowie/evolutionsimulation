from ..windowLib.interface.triggers import Trigger

class ChangeEntityTypeTrigger(Trigger):
    def __init__(self, window, type):
        super().__init__(window)
        self.type = type

    def call(self, interact):
        self.window.entity_type = self.type