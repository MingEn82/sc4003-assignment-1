from classes.Maze import Maze
from classes.Tile import Square, Wall
from classes.MazeSolvers import PolicyIteration, ValueIteration

if __name__ == "__main__":
    # maze = Maze(
    #     [
    #         [Square(1), Wall(), Square(1), Square(), Square(), Square(1)],
    #         [Square(), Square(-1), Square(), Square(1), Wall(), Square(-1)],
    #         [Square(), Square(), Square(-1), Square(), Square(1), Square()],
    #         [Square(), Square(), Square(), Square(-1), Square(), Square(1)],
    #         [Square(), Wall(), Wall(), Wall(), Square(-1), Square()],
    #         [Square(), Square(), Square(), Square(), Square(), Square()]
    #     ]
    # )
    maze = Maze(
        [
            [Square(0), Square(0), Square(0), Square(1),],
            [Square(0), Wall(), Square(0), Square(-1),],
            [Square(0), Square(0), Square(0), Square(0),],
        ]
    )
    solver = PolicyIteration(maze, discount=0.99)
    solver.solve(log_every_step=False, plot_values=True)

    maze = Maze(
        [
            [Square(0), Square(0), Square(0), Square(1),],
            [Square(0), Wall(), Square(0), Square(-1),],
            [Square(0), Square(0), Square(0), Square(0),],
        ]
    )
    solver = ValueIteration(maze, discount=0.99)
    solver.solve(log_every_step=False, plot_values=True)
