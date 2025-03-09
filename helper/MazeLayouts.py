from classes.States import State

def get_q1_maze():
    pos = State(reward=1, is_terminal=True)
    neg = State(reward=-1, is_terminal=True)
    reg = State(reward=-0.05)
    wal = State(reward=0, is_wall=True)

    return [
        [pos, wal, pos, reg, reg, pos],
        [reg, neg, reg, pos, wal, neg],
        [reg, reg, neg, reg, pos, reg],
        [reg, reg, reg, neg, reg, pos],
        [reg, wal, wal, wal, neg, reg],
        [reg, reg, reg, reg, reg, reg]
    ]
