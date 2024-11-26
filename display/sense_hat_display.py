from sense_emu import SenseHat
import copy
from display import IDisplay
class SenseHatDisplay(IDisplay):
    def __init__(self, width=8, height=8):
        self.sense = SenseHat()
        self.sense.clear()
        self.width = width
        self.height = height
        self.lastMap = list()
        
    def draw(self, map, textDisplay):
        if map == self.lastMap:
            return
        self.lastMap = copy.deepcopy(map)
        self.sense.clear()
        print(textDisplay)
        for x in range(self.height):
            for y in range(self.width):
                self.sense.set_pixel(x, y, map[y][x])
