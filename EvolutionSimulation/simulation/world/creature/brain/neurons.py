import pygame, random

from .....config import Config
from .....constants import Constants

class Neuron:
    def __init__(self, creature, type):
        self.creature = creature
        self.type = type
        self.connections = []
    
    def update(self):
        pass

class SensoryNeuron(Neuron):
    def __init__(self, creature):
        super().__init__(creature, "sensory")
        # recorded value of what ever its sensing 0-10
        self.sensory_value = 0
        self.i = 0
    
    def sense(self):
        pass

    def update(self):
        # print(f"updating {self.i}")
        # self.i += 1
        self.sensory_value = self.sense()
    
    def get(self):
        return self.sensory_value
        

class ActionNeuron(Neuron):
    def __init__(self, creature):
        super().__init__(creature, "action")
        # recorded value of how likely to perform action 0-10
        self.action_value = 0
        self.give_connections = {}
    
    def action(self):
        pass
    
    def update(self):
        if random.randint(1, 10) < self.action_value:
            self.action()
            
    
    def give(self, value, id):
        self.action_value = value

class InnerNeuron(Neuron):
    def __init__(self, creature):
        super().__init__(creature, "inner")
        self.give_connections = {}

    
    def get(self):
        connections = len(self.give_connections.keys())
        if not connections:
            return 0
        value = 0
        for given_value in self.give_connections.values():
            value += given_value
        connections = len(self.give_connections.keys())
        return 0 + ((10 - 0) * (value - -100*connections)) / (100*connections - -100*connections)
        
    def give(self, value, id):
        self.give_connections[id] = value
    
class InnerNeuron1(InnerNeuron):
    pass

class InnerNeuron2(InnerNeuron):
    pass


class MoveUpNeuron(ActionNeuron):
    def action(self):
        self.creature.world.move_creature(self.creature, 0, -1)
            
class MoveDownNeuron(ActionNeuron):
    def action(self):
        self.creature.world.move_creature(self.creature, 0, 1)
    
class MoveLeftNeuron(ActionNeuron):
    def action(self):
        self.creature.world.move_creature(self.creature, -1, 0)

class MoveRightNeuron(ActionNeuron):
    def action(self):
        self.creature.world.move_creature(self.creature, 1, 0)


class OcilatingNeuron(SensoryNeuron):
    def __init__(self, creature):
        super().__init__(creature)
        self.ocilator = 0

    def sense(self):
        if self.ocilator == 0:
            self.ocilator = 10
        elif self.ocilator == 10:
            self.ocilator = 0
        return self.ocilator

class ColNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        return 0 + ((10 - 0) * (col - 0)) / (Constants.MAP_COLS-1 - 0)
    
class RowNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        return 0 + ((10 - 0) * (row - 0)) / (Constants.MAP_ROWS-1 - 0)

class LeftRightBorderNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        dist = col
        if col > Constants.MAP_COLS//2:
            dist = Constants.MAP_COLS - col
        return 0 + ((10 - 0) * (dist - 0)) / (Constants.MAP_COLS//2 - 0)


class UpDownBorderNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        dist = row
        if row > Constants.MAP_ROWS//2:
            dist = Constants.MAP_ROWS - row
        return 0 + ((10 - 0) * (dist - 0)) / (Constants.MAP_ROWS//2 - 0)


class PopulationDensityNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        first_row, first_col = row-2, col-2
        if first_row < 0:
            first_row = 0
        if first_col < 0:
            first_col = 0
        second_row, second_col = row+2, col+2
        if second_row > Constants.MAP_ROWS-1:
            second_row = Constants.MAP_ROWS-1
        if second_col > Constants.MAP_COLS-1:
            second_col = Constants.MAP_COLS-1
        num = len(self.creature.world.get_area_entities(first_row, first_col, second_row, second_col, filter="creature"))
        return 0 + ((10 - 0) * (num - 1)) / (25 - 1)

        

# output_start + ((output_end - output_start) * (input - input_start)) / (input_end - input_start)



class AgeNeuron(SensoryNeuron):
    def sense(self):
        return 0 + ((10 - 0) * (self.creature.age - 0)) / (Config.GEN_MAX_UPDATES - 0)

class LookSolidDownNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        below_row = row+10
        if below_row > Constants.MAP_ROWS-1:
            below_row = Constants.MAP_ROWS-1

        below_locs = self.creature.world.get_area_entity_locs(row+1, col, below_row, col)
        if not below_locs:
            return 0
        below_dist = row-min(below_locs)[0]
        return 11 - below_dist

class LookSolidUpNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        above_row = row-10
        if above_row < 0:
            above_row = 0

        above_locs = self.creature.world.get_area_entity_locs(above_row, col, row-1, col)
        if not above_locs:
            return 0
        above_dist = max(above_locs)[0]-row
        return 11 - above_dist


class LookSolidLeftNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        left_col = col-10
        if left_col < 0:
            left_col = 0
        left_locs = self.creature.world.get_area_entity_locs(row, left_col, row, col-1)
        if not left_locs:
            return 0
        left_dist = max(left_locs)[1]-col
        return 11 - left_dist

class LookSolidRightNeuron(SensoryNeuron):
    def sense(self):
        row, col = self.creature.world.get_entity_row_col(self.creature)
        right_col = col+10
        if right_col > Constants.MAP_COLS-1:
            right_col = Constants.MAP_COLS-1

        right_locs = self.creature.world.get_area_entity_locs(row, col+1, row, right_col)
        if not right_locs:
            return 0
        right_dist = min(right_locs)[1]-col
        return 11 - right_dist


