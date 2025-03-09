import tkinter as tk
from classes.MDP import ValueIteration, PolicyIteration, ModifiedPolicyIteration
from classes.Plotters import GridWorldPlotter, ComplexityPlotter
from helper.MazeLayouts import get_q1_maze, generate_random_maze

def part_1():
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
    mpi_solver.solve(error=50)
    mpi_solver.plot_utilities()
    maze_plotter.draw_estimated_utilities(mpi_solver.layout, mpi_solver.utilities, title="Modified Policy Iteration", font_size=9)
    maze_plotter.draw_action(mpi_solver.layout, mpi_solver.policy, title="Modified Policy Iteration", font_size=20)

    root.mainloop()

def part_2():
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
        plotter.add_data("Modified Iteration", s, solver.solve, error=50)

        # Scale cell size down to ensure overall size is the same
        cell_size = cell_size / (s + 3) * s
        font_size = int(font_size / (s + 3) * s)

    plotter.plot_times()
    plotter.plot_iterations()

    root.mainloop()

if __name__ == "__main__":
    # part_1()
    part_2()