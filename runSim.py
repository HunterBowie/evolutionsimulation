import pygame
pygame.init()

from EvolutionSimulation.simulation.simulation import Simulation
from EvolutionSimulation.config import Config

Config.init()

Simulation().start()

 