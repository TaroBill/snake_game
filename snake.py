from queue import Queue
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    

class Snake:
    def __init__(self) -> None:
        self.length = 1
        self.loc = (3,3)
        self.body = Queue(maxsize=self.length)
        self.body.put(self.loc)
        self.dir = Direction.RIGHT
        self.snakeColor = (0,255,0)
    
    def change_dir(self, dir: Direction) -> None:
        if self.dir == Direction.RIGHT or self.dir == Direction.LEFT:
            if dir == Direction.UP or dir == Direction.DOWN:
                self.dir = dir
        elif self.dir == Direction.UP or self.dir == Direction.DOWN:
            if dir == Direction.LEFT or dir == Direction.RIGHT:
                self.dir = dir
                
    def add_body(self) -> None:
        self.length += 1
        self.body.maxsize = self.length
        
    def move(self, x, y) -> None:
        if self.body.qsize() == self.length:
            self.body.get()
        self.body.put((x,y))
        self.loc = (x,y)
        
    def get_speed(self) -> int:
        return (1 + (self.length - 1) * 0.1) * 0.1

    def isInBody(self, x, y) -> bool:
        body_list = list(self.body.queue)
        for body in body_list:
            if (body[0] == x and body[1] == y):
                return True
        return False
    
    def getBody(self) -> list:
        body_list = list(self.body.queue)
        return body_list