import pygame

class Connection:
    ID_COUNT = 0
    def __init__(self, source, sink, weight):
        self.id = Connection.ID_COUNT
        Connection.ID_COUNT += 1
        self.source = source
        self.sink = sink
        self.weight = weight
    
    def update(self):
        self.sink.give((self.source.get()*self.weight), self.id)
        