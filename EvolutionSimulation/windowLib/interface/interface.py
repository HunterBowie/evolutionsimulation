import pygame
from ..exceptions import IterableItemMissingError

class Interface:
    def __init__(self, window, interacts, visuals, run_eventloop=True, sub_interfaces=None):
        self.window = window
        self.screen = window.screen
        self.interacts = interacts
        self.visuals = visuals
        self.run_eventloop = run_eventloop
        if sub_interfaces is None:
            self.sub_interfaces = []
        else:
            self.sub_interfaces = [sub_interface(self) for sub_interface in sub_interfaces]
    
    def get_interact(self, label):
        for interact in self.interacts:
            if interact.label == label:
                return interact
        raise IterableItemMissingError(f"no interact: {label} available interacts: {[interact.label for interact in self.interacts]}")
    
    def get_subinterface(self, label):
        for interface in self.sub_interfaces:
            if interface.label == label:
                return interface
        raise IterableItemMissingError(f"no subinterface: {label} available subinterfaces: {[interface.label for interface in self.sub_interfaces]}")

    
    def eventloop(self, event):
        for interact in self.interacts:
            interact.eventloop(event)
        
        for sub_interface in self.sub_interfaces:
            sub_interface.eventloop(event)

        if event.type == pygame.QUIT:
            self.window.stop()
    
    def update(self):
        if self.run_eventloop:
            for event in pygame.event.get():
                self.eventloop(event)

        for interact in self.interacts:
            interact.update()
    
        for visual in self.visuals:
            visual.render(self.screen)

        for interact in self.interacts:
            interact.render(self.screen)
        
        for sub_interface in self.sub_interfaces:
            sub_interface.update()
    
        
            