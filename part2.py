import tkinter as tk
from classes.MDP import ValueIteration, PolicyIteration, ModifiedPolicyIteration
from classes.Plotters import GridWorldPlotter, ComplexityPlotter
from helper.MazeLayouts import generate_random_maze

if __name__ == "__main__":
    root = tk.Tk()
    cell_size = 90
    font_size = 20
    maze_plotter = GridWorldPlotter(root, cell_size=cell_size, cols=3)
    maze_plotter.pack()

    plotter = ComplexityPlotter()
    for s in range(5, 21, 3):
        maze = generate_random_maze(size=(s,s))
        maze_plotter.draw_maze(maze, title=f"Size = {s}",  cell_size=cell_size, font_size=font_size)

        solver = ValueIteration(maze, discount=0.99)
        plotter.add_data("Value Iteration", s, solver.solve, error=1e-4)

        solver = PolicyIteration(maze, discount=0.99)
        plotter.add_data("Policy Iteration", s, solver.solve)

        solver = ModifiedPolicyIteration(maze, discount=0.99)
        plotter.add_data("Modified Policy Iteration", s, solver.solve, k=50)

        # Scale cell size down to ensure overall size is the same
        cell_size = cell_size / (s + 3) * s
        font_size = int(font_size / (s + 3) * s)

    plotter.plot_times()
    plotter.plot_iterations()

    root.mainloop()