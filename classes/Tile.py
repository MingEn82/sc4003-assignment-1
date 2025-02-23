from classes.Direction import Left

class Square:
    def __init__(self, reward=-0.05, action=Left()):
        self.reward = float(reward)
        self.value = 0.0
        self.prev_value = self.value
        self.action = action

    def display_reward(self):
        return f"|{str(self.reward):^7.7}|"
    
    def display_value(self):
        return f"|{str(self.value):^7.7}|"
    
    def display_direction(self):
        return f"|  {self.action.icon}  |"

class Wall:
    def __init__(self):
        self.value = 0

    def display_reward(self):
        return "|   x   |"
    
    def display_value(self):
        return "|   x   |"

    def display_direction(self):
        return "|  x  |"