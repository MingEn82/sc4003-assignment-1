import tkinter as tk
from classes.MDP import ValueIteration, PolicyIteration, ModifiedPolicyIteration
from classes.Plotters import GridWorldPlotter
from helper.MazeLayouts import get_q1_maze

if __name__ == "__main__":
    root = tk.Tk()
    maze_plotter = GridWorldPlotter(root, cell_size=70, cols=4)
    maze_plotter.pack()

    q1_maze = get_q1_maze()
    maze_plotter.draw_maze(q1_maze, font_size=15)

    vi_solver = ValueIteration(q1_maze, discount=0.99)
    vi_solver.solve(error=1e-4)
    vi_solver.plot_utilities()
    maze_plotter.draw_estimated_utilities(vi_solver.layout, vi_solver.utilities, title="Value Iteration", font_size=9)
    maze_plotter.draw_action(vi_solver.layout, vi_solver.policy, title="Value Iteration", font_size=20)

    pi_solver = PolicyIteration(q1_maze, discount=0.99)
    pi_solver.solve()
    pi_solver.plot_utilities()
    maze_plotter.draw_estimated_utilities(pi_solver.layout, pi_solver.utilities, title="Policy Iteration", font_size=9)
    maze_plotter.draw_action(pi_solver.layout, pi_solver.policy, title="Policy Iteration", font_size=20)

    mpi_solver = ModifiedPolicyIteration(q1_maze, discount=0.99)
    mpi_solver.solve(k=50)
    mpi_solver.plot_utilities()
    maze_plotter.draw_estimated_utilities(mpi_solver.layout, mpi_solver.utilities, title="Modified Policy Iteration", font_size=9)
    maze_plotter.draw_action(mpi_solver.layout, mpi_solver.policy, title="Modified Policy Iteration", font_size=20)

    root.mainloop()