from classes.MDP import ValueIteration, PolicyIteration, ModifiedPolicyIteration
from helper.MazeLayouts import get_q1_maze

if __name__ == "__main__":
    q1_maze = get_q1_maze()

    vi_solver = ValueIteration(q1_maze, discount=0.99)
    vi_solver.solve(error=1e-4)
    vi_solver.print_actions()
    vi_solver.print_utilities()
    print()

    pi_solver = PolicyIteration(q1_maze, discount=0.99)
    pi_solver.solve()
    pi_solver.print_actions()
    pi_solver.print_utilities()
    print()

    mpi_solver = ModifiedPolicyIteration(q1_maze, discount=0.99)
    mpi_solver.solve(error=0.1)
    mpi_solver.print_actions()
    mpi_solver.print_utilities()
    print()