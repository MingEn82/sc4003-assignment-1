from classes.Maze import Maze
from classes.Tile import Square, Wall

def get_test_maze():
    return Maze(
        [
            [Square(0), Square(0), Square(0), Square(1),],
            [Square(0), Wall(), Square(0), Square(-1),],
            [Square(0), Square(0), Square(0), Square(0),],
        ]
    )

def get_q1_maze():
    return Maze(
        [
            [Square(1), Wall(), Square(1), Square(), Square(), Square(1)],
            [Square(), Square(-1), Square(), Square(1), Wall(), Square(-1)],
            [Square(), Square(), Square(-1), Square(), Square(1), Square()],
            [Square(), Square(), Square(), Square(-1), Square(), Square(1)],
            [Square(), Wall(), Wall(), Wall(), Square(-1), Square()],
            [Square(), Square(), Square(), Square(), Square(), Square()]
        ]
    )