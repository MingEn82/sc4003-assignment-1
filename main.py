from helper.MazeLayouts import get_q1_maze, get_test_maze
from classes.MazeSolvers import PolicyIteration, ValueIteration

if __name__ == "__main__":
    solver = PolicyIteration(get_q1_maze(), discount=0.99)
    solver.solve(log_every_step=False, plot_values=False)

    solver = ValueIteration(get_q1_maze(), discount=0.99)
    solver.solve(log_every_step=False, plot_values=False)
