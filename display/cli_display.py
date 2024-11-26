from display.display import IDisplay
import copy
import os


class CliDisplay(IDisplay):
    def __init__(self, width=8, height=8):
        super().__init__(width, height)
        self.lastMap = list()

    def rgb_background(self, r, g, b, text):
        return f"\033[48;2;{r};{g};{b}m{text}\033[0m"   
        
    def printRGB(self, r, g, b):
        print(self.rgb_background(r, g, b, "　"), end="")
    
    def printRGB(self, color):
        print(self.rgb_background(color[0], color[1], color[2], "　"), end="")
    
    def draw(self, map):
        if map == self.lastMap:
            return
        self.lastMap = copy.deepcopy(map)
        os.system('clear')
        for y in range(self.height):
            for x in range(self.width):
                self.printRGB(map[y][x])
            print()