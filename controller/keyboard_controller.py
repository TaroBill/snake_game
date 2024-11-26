from controller.controller import IController, Direction
from pynput import keyboard

class KeyboardController(IController):
    def __init__(self):
        self.dir = None
        self.isSpaceClicked = False
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
            
    def on_press(self, key):
        if key == keyboard.Key.space:
            self.isSpaceClicked = True
            return 
        if not hasattr(key, 'char'):
            return
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
        
    def get_direction(self) -> Direction:
        return self.dir
    
    def start_button(self) -> bool:
        if self.isSpaceClicked:
            self.isSpaceClicked = False
            return True
        return False