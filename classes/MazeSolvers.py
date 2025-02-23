from classes.Maze import Maze
from classes.Tile import Wall
from classes.Direction import (
    rotate_anticlockwise, rotate_clockwise
)

class PolicyIteration:
    def __init__(self, maze:Maze, discount):
        self.maze = maze
        self.discount = discount
        self.m = len(self.maze.layout)
        self.n = len(self.maze.layout[0])

    def _is_valid_move(self, i, j, di, dj):
        return 0 <= i + di < self.m and 0 <= j + dj < self.n and not isinstance(self.maze.layout[i+di][j+dj], Wall)

    def _get_state_value(self, i, j, action):
        # Add the reward of the current tile to value
        tile = self.maze.layout[i][j]
        value = tile.reward

        # Add the discounted rewards of current policies to value
        # Intended outcome happens
        di, dj = action.vector
        # Action results in movement
        if self._is_valid_move(i, j, di, dj):
            value += self.discount * 0.8 * self.maze.layout[i+di][j+dj].prev_value
        # Action results in staying
        else:
            value += self.discount * 0.8 * tile.prev_value

        # 1st unintended outcome happens
        di, dj = rotate_anticlockwise(action).vector
        # Action results in movement
        if self._is_valid_move(i, j, di, dj):
            value += self.discount * 0.1 * self.maze.layout[i+di][j+dj].prev_value
        # Action results in staying
        else:
            value += self.discount * 0.1 * tile.prev_value

        # 2nd unintended outcome happens
        di, dj = rotate_clockwise(action).vector
        # Action results in movement
        if self._is_valid_move(i, j, di, dj):
            value += self.discount * 0.1 * self.maze.layout[i+di][j+dj].prev_value
        # Action results in staying
        else:
            value += self.discount * 0.1 * tile.prev_value
        
        return value

    def policy_evaluation(self, theta=0.001):
        m = len(self.maze.layout)
        n = len(self.maze.layout[0])

        while True:
            delta = 0.0
            old_values = [tile.value for row in self.maze.layout for tile in row]
            for i in range(m):
                for j in range(n):
                    if type(self.maze.layout[i][j]) is Wall:
                        continue
                    self.maze.layout[i][j].value = self._get_state_value(i, j, self.maze.layout[i][j].action)
            new_values = [tile.value for row in self.maze.layout for tile in row]
            diffs = [abs(o - n) for o, n in zip(old_values, new_values)]
            delta = max(diffs)
            if delta < theta:
                break

        for i in range(m):
            for j in range(n):
                self.maze.layout[i][j].prev_value = self.maze.layout[i][j].value

    def policy_improvement(self):
        m = len(self.maze.layout)
        n = len(self.maze.layout[0])
        policy_changed = False

        for i in range(m):
            for j in range(n):
                tile = self.maze.layout[i][j]
                if type(tile) is Wall:
                    continue
                
                best_action_value = float('-inf')
                best_action = tile.action
                action = tile.action
                for _ in range(4):
                    value = self._get_state_value(i, j, action)
                    if value > best_action_value:
                        best_action_value = value
                        best_action = action
                    action = rotate_clockwise(action)
                if type(best_action) != type(tile.action):
                    policy_changed = True
                    self.maze.layout[i][j].action = best_action
        
        return policy_changed
                        
    def solve(self, theta=0.001, max_iterations=100):
        print("==== Iteration 0 ====")
        self.maze.display()
        for iteration in range(max_iterations):
            self.policy_evaluation(theta)
            policy_changed = self.policy_improvement()
            print(f"==== Iteration {iteration + 1} ====")
            self.maze.display()
            if not policy_changed:
                break
