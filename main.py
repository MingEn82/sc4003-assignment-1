import tkinter as tk

from classes.MazeSolvers import PolicyIteration, ValueIteration
from classes.Plotter import MazePlotter
from helper.MazeLayouts import get_q2_maze

if __name__ == "__main__":
    root = tk.Tk()
    maze_plotter = MazePlotter(root, cell_size=50, cols=2)
    maze_plotter.pack()

    maze = get_q2_maze()
    solver = PolicyIteration(maze, discount=0.99)
    solver.solve(verbose=False, plot_values=True)
    maze_plotter.draw_maze(maze.layout)
    # maze_plotter.draw_estimated_utilities(maze.layout, title="Policy Iteration")
    maze_plotter.draw_action(maze.layout, title="Policy Iteration")

    maze = get_q2_maze()
    solver = ValueIteration(maze, discount=0.99)
    solver.solve(verbose=False, plot_values=True)
    # maze_plotter.draw_maze(maze.layout)
    # maze_plotter.draw_estimated_utilities(maze.layout, title="Value Iteration")
    # maze_plotter.draw_action(maze.layout, title="Value Iteration")
    root.mainloop()