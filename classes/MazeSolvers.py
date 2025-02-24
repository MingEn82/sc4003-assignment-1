from classes.Maze import Maze
from classes.Tile import Wall
from classes.Direction import (
    rotate_anticlockwise, rotate_clockwise, Left
)
from classes.Plotter import Plotter

class Solver:
    def __init__(self, maze:Maze, discount):
        self.maze = maze
        self.discount = discount
        self.plotter = Plotter()
    
    def _agent_will_move(self, i, j, di, dj):
        '''
        Returns true if the action will move agent to a square
        Returns false if the action will move agent out of bounds or into a wall
        ''' 
        return 0 <= i + di < self.maze.height and 0 <= j + dj < self.maze.width and not isinstance(self.maze.layout[i+di][j+dj], Wall)
    
    def _get_valid_actions(self, i, j):
        actions = []
        action = Left()
        for _ in range(4):
            di, dj = action.vector
            if 0 <= i + di < self.maze.height and 0 <= j + dj < self.maze.width:
                actions.append(action)
            action = rotate_anticlockwise(action)
        return actions
    
    def _get_q_value(self, i, j, action):
        '''
        Calculates the value of a state given an action
        '''
        # Add the reward of the current tile to value
        tile = self.maze.layout[i][j]
        value = tile.reward

        # Add the discounted rewards of current policies to value
        # Intended outcome happens
        di, dj = action.vector
        # Action results in movement
        if self._agent_will_move(i, j, di, dj):
            value += self.discount * 0.8 * self.maze.layout[i+di][j+dj].prev_value
        # Action results in staying
        else:
            value += self.discount * 0.8 * tile.prev_value

        # 1st unintended outcome happens
        di, dj = rotate_anticlockwise(action).vector
        # Action results in movement
        if self._agent_will_move(i, j, di, dj):
            value += self.discount * 0.1 * self.maze.layout[i+di][j+dj].prev_value
        # Action results in staying
        else:
            value += self.discount * 0.1 * tile.prev_value

        # 2nd unintended outcome happens
        di, dj = rotate_clockwise(action).vector
        # Action results in movement
        if self._agent_will_move(i, j, di, dj):
            value += self.discount * 0.1 * self.maze.layout[i+di][j+dj].prev_value
        # Action results in staying
        else:
            value += self.discount * 0.1 * tile.prev_value
        
        return value

class ValueIteration(Solver):
    def solve(self, max_iterations=100, theta=0.001, log_every_step=True, plot_values=True):
        print("Running Value Iteration")
        if log_every_step:
            print("==== Iteration 0 ====")
            self.maze.display()
        if plot_values:
            self.plotter.add_score(sum(self.maze.get_values()))

        for iteration in range(max_iterations):
            delta = 0.0
            # Saves the old value of each state
            old_values = self.maze.get_values()

            # Iterate through each state in the maze
            for i in range(self.maze.height):
                for j in range(self.maze.width):
                    tile = self.maze.layout[i][j]
                    # Ignore state if state is a Wall
                    if isinstance(tile, Wall):
                        continue

                    # Only consider actions with intended outcome that moves agent to in-bound state
                    valid_actions = self._get_valid_actions(i, j)

                    # Find best action by calculating Q(s,a) for each action
                    max_q = float('-inf')
                    best_action = valid_actions[0]
                    for action in valid_actions:
                        value = self._get_q_value(i, j, action)
                        if value > max_q:
                            max_q = value
                            best_action = action
                            
                    # Updates best action and V(s) for the state
                    self.maze.layout[i][j].action = best_action
                    self.maze.layout[i][j].value = max_q

            # Updates the value of each state synchronously
            self.maze.update_prev_values()
            
            if log_every_step:
                print(f"==== Iteration {iteration + 1} ====")
                self.maze.display()
            
            if plot_values:
                self.plotter.add_score(sum(self.maze.get_values()))

            # Compares the old values of the states with the new value
            # If the maximum difference is below theta, the policy has converged and
            # we terminate the evaluation
            new_values = self.maze.get_values()
            diffs = [abs(o - n) for o, n in zip(old_values, new_values)]
            delta = max(diffs)
            if delta <= theta:
                break
        
        if not log_every_step:
            print(f"==== Iteration {iteration + 1} ====")
            self.maze.display()
        
        if plot_values:
            self.plotter.show_plot()

class PolicyIteration(Solver):
    def policy_evaluation(self, theta):
        '''
        Evaluates the value of each state V(s) using synchronous update
        ''' 
        while True:
            delta = 0.0
            # Saves the old value of each state
            old_values = self.maze.get_values()
            for i in range(self.maze.height):
                for j in range(self.maze.width):
                    if isinstance(self.maze.layout[i][j], Wall):
                        continue
                    self.maze.layout[i][j].value = self._get_q_value(i, j, self.maze.layout[i][j].action)
            # Compares the old values of the states with the new value
            # If the maximum difference is below theta, the policy has converged and
            # we terminate the evaluation
            new_values = [tile.value for row in self.maze.layout for tile in row]
            diffs = [abs(o - n) for o, n in zip(old_values, new_values)]
            delta = max(diffs)
            if delta <= theta:
                break

        # Updates the value of each state synchronously
        self.maze.update_prev_values()

    def policy_improvement(self):
        '''
        Updates the policy of each Square to maximize value
        '''
        policy_changed = False

        for i in range(self.maze.height):
            for j in range(self.maze.width):
                tile = self.maze.layout[i][j]
                if isinstance(tile, Wall):
                    continue
                
                # Calculate the value given each action and choose the best action
                max_q = float('-inf')
                valid_actions = self._get_valid_actions(i, j)
                best_action = valid_actions[0]
                for action in valid_actions:
                    value = self._get_q_value(i, j, action)
                    if value > max_q:
                        max_q = value
                        best_action = action
                if not isinstance(best_action, type(tile.action)):
                    policy_changed = True
                    self.maze.layout[i][j].action = best_action
        
        return policy_changed
                        
    def solve(self, theta=0.001, max_iterations=100, log_every_step=True, plot_values=True):
        print("Running Policy Iteration")
        if log_every_step:
            print("==== Iteration 0 ====")
            self.maze.display()
        if plot_values:
            self.plotter.add_score(sum(self.maze.get_values()))

        for iteration in range(max_iterations):
            self.policy_evaluation(theta)
            policy_changed = self.policy_improvement()

            if log_every_step:
                print(f"==== Iteration {iteration + 1} ====")
                self.maze.display()
            
            if plot_values:
                self.plotter.add_score(sum(self.maze.get_values()))

            if not policy_changed:
                break
            
        if not log_every_step:
            print(f"==== Iteration {iteration + 1} ====")
            self.maze.display()

        if plot_values:
            self.plotter.show_plot()
