from classes.Maze import Maze
from classes.Tile import Square, Wall
from classes.MazeSolvers import PolicyIteration

if __name__ == "__main__":
    maze = Maze(
        [
            [Square(1), Wall(), Square(1), Square(), Square(), Square(1)],
            [Square(), Square(-1), Square(), Square(1), Wall(), Square(-1)],
            [Square(), Square(), Square(-1), Square(), Square(1), Square()],
            [Square(), Square(), Square(), Square(-1), Square(), Square(1)],
            [Square(), Wall(), Wall(), Wall(), Square(-1), Square()],
            [Square(), Square(), Square(), Square(), Square(), Square()]
        ]
    )
    maze.display()
    solver = PolicyIteration(maze, discount=0.99)
    solver.solve()