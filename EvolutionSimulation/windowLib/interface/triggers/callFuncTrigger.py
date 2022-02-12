from .trigger import Trigger

class CallFuncTrigger(Trigger):
    def __init__(self, window, func, **args):
        super().__init__(window)
        self.func = func
        self.args = args
    
    def call(self, interact):
        if self.args:
            self.func(self.args)
        else:
            self.func()