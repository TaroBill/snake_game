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
        self.map = [[(0,0,0)]*self.mapWidth for _ in range(8)]
        self.timeSurvie = 0
        self.displayText = ""
        self.wait()
        self.game_loop()
    
    def wait(self):
        self.state = GameState.Waiting
        self.displayText = "Press 「Space」 to Start"
            
    def wait_scene(self):
        self.draw_wait()
        if self.controller.start_button():
            self.start()
            return
    
    def start(self):
        self.state = GameState.Start
        self.snake = Snake()
        self.displayText = "" 
        self.snakeMoveTimer = 0
        self.add_fruit()
        self.timeSurvie = 0
        
    def start_scene(self):
        self.timeSurvie += self.refreshTime
        self.snakeMoveTimer += self.snake.get_speed()
        if self.snakeMoveTimer >= 1:
            self.snakeMoveTimer = 0
            controller_dir = self.controller.get_direction()
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
            if self.is_in_wall(x, y) or self.snake.is_in_body(x, y):
                self.gameover()
                return
            if self.fruitLoc == (x, y):
                self.snake.add_body()
                self.add_fruit() 
            self.snake.move(x, y)
            
        self.draw_snake()
        self.draw_fruit()

        
    def gameover(self):
        self.displayText = f"Game Over! Score: {self.snake.length * int(self.timeSurvie)}"
        self.state = GameState.GameOver
        self.gameover_timer = 30
        
    def gameover_scene(self):
        self.draw_gameover()
        if self.gameover_timer >= 0:
            self.gameover_timer -= 1
        else:
            self.wait()
            return
        
    def game_loop(self):
        while True:
            # 繪製地圖
            self.clear_map() 
            if self.state == GameState.Start:
                self.start_scene()
            elif self.state == GameState.GameOver:
                self.gameover_scene()
            elif self.state == GameState.Waiting:
                self.wait_scene()
            self.display.draw(self.map, self.displayText) 
            sleep(self.refreshTime)
            
    def add_fruit(self):
        availableLoc = []
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                if not self.snake.is_in_body(x, y):
                    availableLoc.append((x,y))
        randomLoc = random.choice(availableLoc)
        self.fruitLoc = randomLoc
    
    def draw_fruit(self):
        self.map[self.fruitLoc[1]][self.fruitLoc[0]] = (255,0,0)
        
    def is_in_wall(self, x, y):
        if x < 0 or x >= self.mapWidth or y < 0 or y >= self.mapHeight:
            return True
        return False
    
    def draw_snake(self):
        body = self.snake.get_body()
        for loc in body:
            self.map[loc[1]][loc[0]] = self.snake.snakeColor
            
    def clear_map(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (0,0,0)
                
    def draw_gameover(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (255,0,0)
    
    def draw_wait(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (0,0,255)


from controller.keyboard_controller import KeyboardController
from display.cli_display import CliDisplay
SnakeGame(KeyboardController(), CliDisplay(8, 8))