class State:
    def __init__(self, reward=-0.05, is_terminal=False, is_wall=False):
        self.reward = float(reward)
        self.is_terminal = is_terminal
        self.is_wall = is_wall