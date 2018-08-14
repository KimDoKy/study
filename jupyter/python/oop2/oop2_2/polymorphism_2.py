from abc import *

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def eat(self):
        pass
