from classes.Tile import Direction, Square, Wall

class Maze:
    def __init__(self):
        self.layout = [
            [Square(1), Wall(), Square(1), Square(), Square(), Square(1)],
            [Square(), Square(-1), Square(), Square(1), Wall(), Square(-1)],
            [Square(), Square(), Square(-1), Square(), Square(1), Square()],
            [Square(), Square(), Square(), Square(-1), Square(), Square(1)],
            [Square(), Wall(), Wall(), Wall(), Square(-1), Square()],
            [Square(), Square(), Square(), Square(), Square(), Square()]
        ]
    
    def display(self):
        for line in self.layout:
            print("+-----+"*len(line))
            for tile in line:
                print(tile.display(), end="")
            print()
            print("+-----+"*len(line))