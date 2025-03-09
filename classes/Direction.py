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

    @classmethod
    def Left(cls):
        return cls.LEFT

    @classmethod
    def Right(cls):
        return cls.RIGHT

    @classmethod
    def Up(cls):
        return cls.UP

    @classmethod
    def Down(cls):
        return cls.DOWN

    def rotate_clockwise(self):
        if self is Direction.LEFT:
            return Direction.Up()
        if self is Direction.UP:
            return Direction.Right()
        if self is Direction.RIGHT:
            return Direction.Down()
        if self is Direction.DOWN:
            return Direction.Left()
        raise ValueError("Invalid direction for rotation.")

    def rotate_anticlockwise(self):
        if self is Direction.LEFT:
            return Direction.Down()
        if self is Direction.DOWN:
            return Direction.Right()
        if self is Direction.RIGHT:
            return Direction.Up()
        if self is Direction.UP:
            return Direction.Left()
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
