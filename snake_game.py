from enum import Enum
from snake import Snake, Direction
from display.display import IDisplay
from controller.controller import IController
from time import sleep
import random

class GameState(Enum):
    Waiting = 0
    Start = 1
    GameOver = 2
    
class SnakeGame():
    def __init__(self, controller: IController, display: IDisplay) -> None:
        self.snake = Snake()
        self.mapWidth = display.width
        self.mapHeight = display.height
        self.refreshTime = 0.1
        self.controller = controller
        self.display = display
        self.snakeMoveTimer = 0
        self.map = [[(0,0,0)]*self.mapWidth for _ in range(8)]
        self.wait()
        self.game_loop()
    
    def wait(self):
        self.state = GameState.Waiting
        
            
    def wait_scene(self):
        self.drawWait()
        if self.controller.start_button():
            self.start()
            return
    
    def start(self):
        self.state = GameState.Start
        self.snake = Snake()
        self.addFruit()
        
    def start_scene(self):
        self.snakeMoveTimer += self.snake.get_speed()
        if self.snakeMoveTimer >= 1:
            self.snakeMoveTimer = 0
            controller_dir = self.controller.get_Direction()
            if controller_dir != None:
                self.snake.change_dir(controller_dir)
                
            snake_dir = self.snake.dir
            x = self.snake.loc[0]
            y = self.snake.loc[1]
            if snake_dir == Direction.UP:
                y -= 1
            elif snake_dir == Direction.DOWN:
                y += 1
            elif snake_dir == Direction.RIGHT:
                x += 1
            elif snake_dir == Direction.LEFT:
                x -= 1
            if self.isInWall(x, y) or self.snake.isInBody(x, y):
                self.gameover()
                return
            if self.fruitLoc == (x, y):
                self.snake.add_body()
                self.addFruit() 
            self.snake.move(x, y)
            
        self.drawSnake()
        self.drawFruit()

        
    def gameover(self):
        self.state = GameState.GameOver
        self.gameover_timer = 30
        
    def gameover_scene(self):
        self.drawGameover()
        if self.gameover_timer >= 0:
            self.gameover_timer -= 1
        else:
            self.wait()
            return
        
    def game_loop(self):
        while True:
            # 繪製地圖
            self.clearMap() 
            if self.state == GameState.Start:
                self.start_scene()
            elif self.state == GameState.GameOver:
                self.gameover_scene()
            elif self.state == GameState.Waiting:
                self.wait_scene()
            self.display.draw(self.map)
            sleep(self.refreshTime)
            
    def addFruit(self):
        availableLoc = []
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                if not self.snake.isInBody(x, y):
                    availableLoc.append((x,y))
        randomLoc = random.choice(availableLoc)
        self.fruitLoc = randomLoc
    
    def drawFruit(self):
        self.map[self.fruitLoc[1]][self.fruitLoc[0]] = (100,100,0)
        
    def isInWall(self, x, y):
        if x < 0 or x >= self.mapWidth or y < 0 or y >= self.mapHeight:
            return True
        return False
    
    def drawSnake(self):
        body = self.snake.getBody()
        for loc in body:
            self.map[loc[1]][loc[0]] = self.snake.snakeColor
            
    def clearMap(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (0,0,0)
                
    def drawGameover(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (255,0,0)
    
    def drawWait(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (0,0,255)


from controller.keyboard_controller import KeyboardController
from display.cli_display import CliDisplay
SnakeGame(KeyboardController(), CliDisplay(8, 8))