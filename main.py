from helper.MazeLayouts import get_q1_maze, get_test_maze
from classes.MazeSolvers import PolicyIteration, ValueIteration
from classes.Plotter import MazePlotter
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    maze_plotter = MazePlotter(root)
    maze_plotter.pack()

    maze = get_q1_maze()
    solver = PolicyIteration(maze, discount=0.99)
    solver.solve(log_every_step=False, plot_values=False)
    maze_plotter.draw_estimated_utilities(maze.layout)
    maze_plotter.draw_action(maze.layout)

    maze = get_q1_maze()
    solver = ValueIteration(maze, discount=0.99)
    solver.solve(log_every_step=False, plot_values=False)
    maze_plotter.draw_estimated_utilities(maze.layout)
    maze_plotter.draw_action(maze.layout)
    root.mainloop()