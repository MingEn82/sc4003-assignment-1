from classes.Maze import Maze
from classes.Tile import Wall
from classes.Direction import (
    Left, Right, Up, Down, rotate_anticlockwise, rotate_clockwise
)

class PolicyIteration:
    def __init__(self, maze:Maze, discount):
        self.maze = maze
        self.discount = discount

    def policy_evaluation(self):
        m = len(self.maze.layout)
        n = len(self.maze.layout[0])

        for i in range(m):
            for j in range(n):
                if type(self.maze.layout[i][j]) is Wall:
                    continue
                
                # Add the reward of the current tile to value
                self.maze.layout[i][j].value = self.maze.layout[i][j].reward

                # Add the discounted rewards of current policies to value
                # Intended outcome happens
                di, dj = self.maze.layout[i][j].action.vector
                # Action results in movement
                if 0 <= i + di < m and 0 <= i + dj < n and type(self.maze.layout[i+di][j+dj]) is not Wall:
                    self.maze.layout[i][j].value += self.discount * 0.8 * self.maze.layout[i+di][j+dj]._prev_value
                # Action results in staying
                else:
                    self.maze.layout[i][j].value += self.discount * 0.8 * self.maze.layout[i][j]._prev_value
    
                # 1st unintended outcome happens
                di, dj = rotate_anticlockwise(self.maze.layout[i][j].action).vector
                # Action results in movement
                if 0 <= i + di < m and 0 <= i + dj < n and type(self.maze.layout[i+di][j+dj]) is not Wall:
                    self.maze.layout[i][j].value += self.discount * 0.1 * self.maze.layout[i+di][j+dj]._prev_value
                # Action results in staying
                else:
                    self.maze.layout[i][j].value += self.discount * 0.1 * self.maze.layout[i][j]._prev_value

                # 2nd unintended outcome happens
                di, dj = rotate_clockwise(self.maze.layout[i][j].action).vector
                # Action results in movement
                if 0 <= i + di < m and 0 <= i + dj < n and type(self.maze.layout[i+di][j+dj]) is not Wall:
                    self.maze.layout[i][j].value += self.discount * 0.1 * self.maze.layout[i+di][j+dj]._prev_value
                # Action results in staying
                else:
                    self.maze.layout[i][j].value += self.discount * 0.1 * self.maze.layout[i][j]._prev_value
        
        for i in range(m):
            for j in range(n):
                self.maze.layout[i][j]._prev_value = self.maze.layout[i][j].value
                
    def solve(self, theta=0.001):
        while True:
            delta = 0.0
            old_values = [tile.value for row in self.maze.layout for tile in row]
            self.policy_evaluation()
            new_values = [tile.value for row in self.maze.layout for tile in row]
            diffs = [abs(o - n) for o, n in zip(old_values, new_values)]
            delta = max(diffs)
            if delta < theta:
                break
        self.maze.display()