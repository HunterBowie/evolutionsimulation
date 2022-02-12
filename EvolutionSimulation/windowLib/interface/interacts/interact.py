import pygame

class Interact:
    def __init__(self, label, triggers, tangable):
        self.triggers = triggers
        self.label = label
        self.tangable = tangable
            
    def update(self):
        pass

    def eventloop(self, event):
        pass

    def render(self, screen):
        pass

    def trigger(self):
        for trigger in self.triggers:
            trigger.call(self)
    
    def get(self):
        raise Exception("this interact does not have a get method")