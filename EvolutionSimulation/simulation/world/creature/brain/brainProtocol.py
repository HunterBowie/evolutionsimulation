from .neurons import *

class BrainProtocol:
    SENSORY = [AgeNeuron, OcilatingNeuron, RowNeuron, ColNeuron, LeftRightBorderNeuron, UpDownBorderNeuron,
    LookSolidDownNeuron, LookSolidUpNeuron, LookSolidRightNeuron, LookSolidLeftNeuron, PopulationDensityNeuron]
    ACTION = [MoveUpNeuron, MoveDownNeuron, MoveLeftNeuron, MoveRightNeuron]
    ALL = SENSORY + ACTION

    def lookup_all(id):
        return BrainProtocol.ALL[id]

    @staticmethod
    def lookup_sensory(id):
        return BrainProtocol.SENSORY[id]

    @staticmethod
    def lookup_action(id):
        return BrainProtocol.ACTION[id]