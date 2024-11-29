from sense_emu import SenseHat
import copy
from display.display import IDisplay
class SenseHatDisplay(IDisplay):
    def __init__(self, width=8, height=8, sense: SenseHat = None) -> None:
        self.sense = sense
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
                
    def show_text(self, text):
        self.sense.show_message(text)
