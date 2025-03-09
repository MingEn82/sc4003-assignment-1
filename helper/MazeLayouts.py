from typing import Tuple
import numpy as np
from classes.States import State

pos = State(reward=1, is_terminal=True)
neg = State(reward=-1, is_terminal=True)
reg = State(reward=-0.05)
wal = State(reward=0, is_wall=True)

def get_q1_maze():
    return [
        [pos, wal, pos, reg, reg, pos],
        [reg, neg, reg, pos, wal, neg],
        [reg, reg, neg, reg, pos, reg],
        [reg, reg, reg, neg, reg, pos],
        [reg, wal, wal, wal, neg, reg],
        [reg, reg, reg, reg, reg, reg]
    ]

def generate_random_maze(size:Tuple[int, int]):
    return np.random.choice([pos, neg, reg, wal], size=size, p=[0.1, 0.1, 0.7, 0.1])