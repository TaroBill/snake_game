from abc import ABC, abstractmethod

class IDisplay(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @abstractmethod
    def draw(self, map, textDisplay):
        pass