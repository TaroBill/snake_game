from controller.controller import IController, Direction
from pynput import keyboard

class KeyboardController(IController):
    def __init__(self):
        self.dir = None
        self.isSpaceClicked = False

            
    def on_press(self, key):
        if key.char == 'a':
            self.dir = Direction.LEFT
        elif key.char == 'd':
            self.dir = Direction.RIGHT
        elif key.char == 'w':
            self.dir = Direction.UP
        elif key.char == 's':
            self.dir = Direction.DOWN
        else:
            self.dir = None
            
        if key == keyboard.Key.space:
            self.isSpaceClicked = True
        
    def get_Direction(self) -> Direction:
        return self.dir
    
    def start_button(self) -> bool:
        return self.isSpaceClicked