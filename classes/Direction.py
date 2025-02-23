class Direction:
    def __init__(self, vector, icon):
        self.vector = vector
        self.icon = icon
    
    def __str__(self):
        return self.icon
    
    
class Left(Direction):
    def __init__(self):
        super().__init__(vector=(-1, 0), icon="←")

class Right(Direction):
    def __init__(self):
        super().__init__(vector=(1, 0), icon="→")

class Up(Direction):
    def __init__(self):
        super().__init__(vector=(0, -1), icon="↑")

class Down(Direction):
    def __init__(self):
        super().__init__(vector=(0, 1), icon="↓")

def rotate_clockwise(direction:Direction):
    if type(direction) is Left:
        return Up()
    elif type(direction) is Up:
        return Right()
    elif type(direction) is Right:
        return Down()
    else:
        return Left()
    
def rotate_anticlockwise(direction:Direction):
    if type(direction) is Left:
        return Down()
    elif type(direction) is Up:
        return Left()
    elif type(direction) is Right:
        return Up()
    else:
        return Right()