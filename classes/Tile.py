from enum import Enum

class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

class Square:
    def __init__(self, reward=-0.05):
        self.reward = float(reward)
        self.value = 0
        self.best_action = Direction.LEFT
    
    def display(self):
        return f"|{self.reward:5.5}|"

class Wall:
    def __init__(self):
        self.value = 0
    
    def display(self):
        return f"|xxxxx|"