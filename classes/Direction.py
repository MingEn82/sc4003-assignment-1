from typing import Tuple

class Direction:
    # Class attributes for the singleton instances.
    LEFT: "Direction" = None
    RIGHT: "Direction" = None
    UP: "Direction" = None
    DOWN: "Direction" = None

    def __init__(self, vector: Tuple[int, int], icon: str):
        self.vector = vector
        self.icon = icon

    def __str__(self):
        return self.icon

    def rotate_clockwise(self):
        if self is Direction.LEFT:
            return Direction.UP
        if self is Direction.UP:
            return Direction.RIGHT
        if self is Direction.RIGHT:
            return Direction.DOWN
        if self is Direction.DOWN:
            return Direction.LEFT
        raise ValueError("Invalid direction for rotation.")

    def rotate_anticlockwise(self):
        if self is Direction.LEFT:
            return Direction.DOWN
        if self is Direction.DOWN:
            return Direction.RIGHT
        if self is Direction.RIGHT:
            return Direction.UP
        if self is Direction.UP:
            return Direction.LEFT
        raise ValueError("Invalid direction for rotation.")

    def __eq__(self, other):
        if not isinstance(other, Direction):
            return NotImplemented
        return self.vector == other.vector and self.icon == other.icon

# Initialize the singleton instances.
Direction.LEFT = Direction(vector=(0, -1), icon="←")
Direction.RIGHT = Direction(vector=(0, 1), icon="→")
Direction.UP = Direction(vector=(-1, 0), icon="↑")
Direction.DOWN = Direction(vector=(1, 0), icon="↓")
