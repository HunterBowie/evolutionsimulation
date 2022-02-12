import pygame

class Trigger:
    def __init__(self, window):
        self.window = window
    
    def call(self, interact):
        pass

    def get_interact(self, label):
        for interact in self.window.interface.interacts:
            if interact.label == label:
                return interact
        raise ValueError("no interact with given label")
        