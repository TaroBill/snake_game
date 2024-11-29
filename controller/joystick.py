from controller.controller import IController
from snake import Direction
from sense_emu import SenseHat

class JoystickController(IController):
    def __init__(self, sense: SenseHat) -> None:
        self.sense = sense
        self.dir = None

    def start_button(self) -> bool:
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    return True
        return False
            
    def get_direction(self) -> Direction:
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "left":
                    return Direction.LEFT
                if event.direction == "right":
                    return Direction.RIGHT
                if event.direction == "up":
                    return Direction.UP
                if event.direction == "down":
                    return Direction.DOWN
        return None