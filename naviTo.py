# naviTo
# 0.1565 s
# 1631 op

# Generate_data
# 0.1284s
# 1341 op

# 2,76% faster then "moveTo.py" after ~30 moves

def Generate_data(size=get_world_size()):
    move_x = dict()
    move_y = dict()
    for start in range(size):
        for end in range(size):
            difference = (end - start) % size
            move_x[start, end] = list()
            move_y[start, end] = list()
            if (size//2) > difference:
                for i in range(difference):
                    move_x[start, end].append(East)
                    move_y[start, end].append(North)
            else:
                for i in range(size-difference):
                    move_x[start, end].append(West)
                    move_y[start, end].append(South)
    return move_x,move_y

def loadData(size=get_world_size()):
    if size == 3:
        return {
            (0, 0): [],
            (0, 1): [West, West],
            (0, 2): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): []
        }, {
            (0, 0): [],
            (0, 1): [South, South],
            (0, 2): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): []
        }
    elif size == 4:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [West, West],
            (0, 3): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (3, 0): [East],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [South, South],
            (0, 3): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (3, 0): [North],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): []
        }
    elif size == 5:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [West, West, West],
            (0, 3): [West, West],
            (0, 4): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [West, West, West],
            (1, 4): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (2, 4): [West, West, West],
            (3, 0): [West, West, West],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): [],
            (3, 4): [East],
            (4, 0): [East],
            (4, 1): [West, West, West],
            (4, 2): [West, West],
            (4, 3): [West],
            (4, 4): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [South, South, South],
            (0, 3): [South, South],
            (0, 4): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [South, South, South],
            (1, 4): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (2, 4): [South, South, South],
            (3, 0): [South, South, South],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): [],
            (3, 4): [North],
            (4, 0): [North],
            (4, 1): [South, South, South],
            (4, 2): [South, South],
            (4, 3): [South],
            (4, 4): []
        }
    elif size == 6:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [East, East],
            (0, 3): [West, West, West],
            (0, 4): [West, West],
            (0, 5): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [East, East],
            (1, 4): [West, West, West],
            (1, 5): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (2, 4): [East, East],
            (2, 5): [West, West, West],
            (3, 0): [West, West, West],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): [],
            (3, 4): [East],
            (3, 5): [East, East],
            (4, 0): [East, East],
            (4, 1): [West, West, West],
            (4, 2): [West, West],
            (4, 3): [West],
            (4, 4): [],
            (4, 5): [East],
            (5, 0): [East],
            (5, 1): [East, East],
            (5, 2): [West, West, West],
            (5, 3): [West, West],
            (5, 4): [West],
            (5, 5): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [North, North],
            (0, 3): [South, South, South],
            (0, 4): [South, South],
            (0, 5): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [North, North],
            (1, 4): [South, South, South],
            (1, 5): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (2, 4): [North, North],
            (2, 5): [South, South, South],
            (3, 0): [South, South, South],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): [],
            (3, 4): [North],
            (3, 5): [North, North],
            (4, 0): [North, North],
            (4, 1): [South, South, South],
            (4, 2): [South, South],
            (4, 3): [South],
            (4, 4): [],
            (4, 5): [North],
            (5, 0): [North],
            (5, 1): [North, North],
            (5, 2): [South, South, South],
            (5, 3): [South, South],
            (5, 4): [South],
            (5, 5): []
        }
    elif size == 7:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [East, East],
            (0, 3): [West, West, West, West],
            (0, 4): [West, West, West],
            (0, 5): [West, West],
            (0, 6): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [East, East],
            (1, 4): [West, West, West, West],
            (1, 5): [West, West, West],
            (1, 6): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (2, 4): [East, East],
            (2, 5): [West, West, West, West],
            (2, 6): [West, West, West],
            (3, 0): [West, West, West],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): [],
            (3, 4): [East],
            (3, 5): [East, East],
            (3, 6): [West, West, West, West],
            (4, 0): [West, West, West, West],
            (4, 1): [West, West, West],
            (4, 2): [West, West],
            (4, 3): [West],
            (4, 4): [],
            (4, 5): [East],
            (4, 6): [East, East],
            (5, 0): [East, East],
            (5, 1): [West, West, West, West],
            (5, 2): [West, West, West],
            (5, 3): [West, West],
            (5, 4): [West],
            (5, 5): [],
            (5, 6): [East],
            (6, 0): [East],
            (6, 1): [East, East],
            (6, 2): [West, West, West, West],
            (6, 3): [West, West, West],
            (6, 4): [West, West],
            (6, 5): [West],
            (6, 6): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [North, North],
            (0, 3): [South, South, South, South],
            (0, 4): [South, South, South],
            (0, 5): [South, South],
            (0, 6): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [North, North],
            (1, 4): [South, South, South, South],
            (1, 5): [South, South, South],
            (1, 6): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (2, 4): [North, North],
            (2, 5): [South, South, South, South],
            (2, 6): [South, South, South],
            (3, 0): [South, South, South],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): [],
            (3, 4): [North],
            (3, 5): [North, North],
            (3, 6): [South, South, South, South],
            (4, 0): [South, South, South, South],
            (4, 1): [South, South, South],
            (4, 2): [South, South],
            (4, 3): [South],
            (4, 4): [],
            (4, 5): [North],
            (4, 6): [North, North],
            (5, 0): [North, North],
            (5, 1): [South, South, South, South],
            (5, 2): [South, South, South],
            (5, 3): [South, South],
            (5, 4): [South],
            (5, 5): [],
            (5, 6): [North],
            (6, 0): [North],
            (6, 1): [North, North],
            (6, 2): [South, South, South, South],
            (6, 3): [South, South, South],
            (6, 4): [South, South],
            (6, 5): [South],
            (6, 6): []
        }
    elif size == 8:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [East, East],
            (0, 3): [East, East, East],
            (0, 4): [West, West, West, West],
            (0, 5): [West, West, West],
            (0, 6): [West, West],
            (0, 7): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [East, East],
            (1, 4): [East, East, East],
            (1, 5): [West, West, West, West],
            (1, 6): [West, West, West],
            (1, 7): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (2, 4): [East, East],
            (2, 5): [East, East, East],
            (2, 6): [West, West, West, West],
            (2, 7): [West, West, West],
            (3, 0): [West, West, West],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): [],
            (3, 4): [East],
            (3, 5): [East, East],
            (3, 6): [East, East, East],
            (3, 7): [West, West, West, West],
            (4, 0): [West, West, West, West],
            (4, 1): [West, West, West],
            (4, 2): [West, West],
            (4, 3): [West],
            (4, 4): [],
            (4, 5): [East],
            (4, 6): [East, East],
            (4, 7): [East, East, East],
            (5, 0): [East, East, East],
            (5, 1): [West, West, West, West],
            (5, 2): [West, West, West],
            (5, 3): [West, West],
            (5, 4): [West],
            (5, 5): [],
            (5, 6): [East],
            (5, 7): [East, East],
            (6, 0): [East, East],
            (6, 1): [East, East, East],
            (6, 2): [West, West, West, West],
            (6, 3): [West, West, West],
            (6, 4): [West, West],
            (6, 5): [West],
            (6, 6): [],
            (6, 7): [East],
            (7, 0): [East],
            (7, 1): [East, East],
            (7, 2): [East, East, East],
            (7, 3): [West, West, West, West],
            (7, 4): [West, West, West],
            (7, 5): [West, West],
            (7, 6): [West],
            (7, 7): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [North, North],
            (0, 3): [North, North, North],
            (0, 4): [South, South, South, South],
            (0, 5): [South, South, South],
            (0, 6): [South, South],
            (0, 7): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [North, North],
            (1, 4): [North, North, North],
            (1, 5): [South, South, South, South],
            (1, 6): [South, South, South],
            (1, 7): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (2, 4): [North, North],
            (2, 5): [North, North, North],
            (2, 6): [South, South, South, South],
            (2, 7): [South, South, South],
            (3, 0): [South, South, South],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): [],
            (3, 4): [North],
            (3, 5): [North, North],
            (3, 6): [North, North, North],
            (3, 7): [South, South, South, South],
            (4, 0): [South, South, South, South],
            (4, 1): [South, South, South],
            (4, 2): [South, South],
            (4, 3): [South],
            (4, 4): [],
            (4, 5): [North],
            (4, 6): [North, North],
            (4, 7): [North, North, North],
            (5, 0): [North, North, North],
            (5, 1): [South, South, South, South],
            (5, 2): [South, South, South],
            (5, 3): [South, South],
            (5, 4): [South],
            (5, 5): [],
            (5, 6): [North],
            (5, 7): [North, North],
            (6, 0): [North, North],
            (6, 1): [North, North, North],
            (6, 2): [South, South, South, South],
            (6, 3): [South, South, South],
            (6, 4): [South, South],
            (6, 5): [South],
            (6, 6): [],
            (6, 7): [North],
            (7, 0): [North],
            (7, 1): [North, North],
            (7, 2): [North, North, North],
            (7, 3): [South, South, South, South],
            (7, 4): [South, South, South],
            (7, 5): [South, South],
            (7, 6): [South],
            (7, 7): []
        }
    elif size == 9:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [East, East],
            (0, 3): [East, East, East],
            (0, 4): [West, West, West, West, West],
            (0, 5): [West, West, West, West],
            (0, 6): [West, West, West],
            (0, 7): [West, West],
            (0, 8): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [East, East],
            (1, 4): [East, East, East],
            (1, 5): [West, West, West, West, West],
            (1, 6): [West, West, West, West],
            (1, 7): [West, West, West],
            (1, 8): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (2, 4): [East, East],
            (2, 5): [East, East, East],
            (2, 6): [West, West, West, West, West],
            (2, 7): [West, West, West, West],
            (2, 8): [West, West, West],
            (3, 0): [West, West, West],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): [],
            (3, 4): [East],
            (3, 5): [East, East],
            (3, 6): [East, East, East],
            (3, 7): [West, West, West, West, West],
            (3, 8): [West, West, West, West],
            (4, 0): [West, West, West, West],
            (4, 1): [West, West, West],
            (4, 2): [West, West],
            (4, 3): [West],
            (4, 4): [],
            (4, 5): [East],
            (4, 6): [East, East],
            (4, 7): [East, East, East],
            (4, 8): [West, West, West, West, West],
            (5, 0): [West, West, West, West, West],
            (5, 1): [West, West, West, West],
            (5, 2): [West, West, West],
            (5, 3): [West, West],
            (5, 4): [West],
            (5, 5): [],
            (5, 6): [East],
            (5, 7): [East, East],
            (5, 8): [East, East, East],
            (6, 0): [East, East, East],
            (6, 1): [West, West, West, West, West],
            (6, 2): [West, West, West, West],
            (6, 3): [West, West, West],
            (6, 4): [West, West],
            (6, 5): [West],
            (6, 6): [],
            (6, 7): [East],
            (6, 8): [East, East],
            (7, 0): [East, East],
            (7, 1): [East, East, East],
            (7, 2): [West, West, West, West, West],
            (7, 3): [West, West, West, West],
            (7, 4): [West, West, West],
            (7, 5): [West, West],
            (7, 6): [West],
            (7, 7): [],
            (7, 8): [East],
            (8, 0): [East],
            (8, 1): [East, East],
            (8, 2): [East, East, East],
            (8, 3): [West, West, West, West, West],
            (8, 4): [West, West, West, West],
            (8, 5): [West, West, West],
            (8, 6): [West, West],
            (8, 7): [West],
            (8, 8): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [North, North],
            (0, 3): [North, North, North],
            (0, 4): [South, South, South, South, South],
            (0, 5): [South, South, South, South],
            (0, 6): [South, South, South],
            (0, 7): [South, South],
            (0, 8): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [North, North],
            (1, 4): [North, North, North],
            (1, 5): [South, South, South, South, South],
            (1, 6): [South, South, South, South],
            (1, 7): [South, South, South],
            (1, 8): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (2, 4): [North, North],
            (2, 5): [North, North, North],
            (2, 6): [South, South, South, South, South],
            (2, 7): [South, South, South, South],
            (2, 8): [South, South, South],
            (3, 0): [South, South, South],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): [],
            (3, 4): [North],
            (3, 5): [North, North],
            (3, 6): [North, North, North],
            (3, 7): [South, South, South, South, South],
            (3, 8): [South, South, South, South],
            (4, 0): [South, South, South, South],
            (4, 1): [South, South, South],
            (4, 2): [South, South],
            (4, 3): [South],
            (4, 4): [],
            (4, 5): [North],
            (4, 6): [North, North],
            (4, 7): [North, North, North],
            (4, 8): [South, South, South, South, South],
            (5, 0): [South, South, South, South, South],
            (5, 1): [South, South, South, South],
            (5, 2): [South, South, South],
            (5, 3): [South, South],
            (5, 4): [South],
            (5, 5): [],
            (5, 6): [North],
            (5, 7): [North, North],
            (5, 8): [North, North, North],
            (6, 0): [North, North, North],
            (6, 1): [South, South, South, South, South],
            (6, 2): [South, South, South, South],
            (6, 3): [South, South, South],
            (6, 4): [South, South],
            (6, 5): [South],
            (6, 6): [],
            (6, 7): [North],
            (6, 8): [North, North],
            (7, 0): [North, North],
            (7, 1): [North, North, North],
            (7, 2): [South, South, South, South, South],
            (7, 3): [South, South, South, South],
            (7, 4): [South, South, South],
            (7, 5): [South, South],
            (7, 6): [South],
            (7, 7): [],
            (7, 8): [North],
            (8, 0): [North],
            (8, 1): [North, North],
            (8, 2): [North, North, North],
            (8, 3): [South, South, South, South, South],
            (8, 4): [South, South, South, South],
            (8, 5): [South, South, South],
            (8, 6): [South, South],
            (8, 7): [South],
            (8, 8): []
        }
    elif size == 10:
        return {
            (0, 0): [],
            (0, 1): [East],
            (0, 2): [East, East],
            (0, 3): [East, East, East],
            (0, 4): [East, East, East, East],
            (0, 5): [West, West, West, West, West],
            (0, 6): [West, West, West, West],
            (0, 7): [West, West, West],
            (0, 8): [West, West],
            (0, 9): [West],
            (1, 0): [West],
            (1, 1): [],
            (1, 2): [East],
            (1, 3): [East, East],
            (1, 4): [East, East, East],
            (1, 5): [East, East, East, East],
            (1, 6): [West, West, West, West, West],
            (1, 7): [West, West, West, West],
            (1, 8): [West, West, West],
            (1, 9): [West, West],
            (2, 0): [West, West],
            (2, 1): [West],
            (2, 2): [],
            (2, 3): [East],
            (2, 4): [East, East],
            (2, 5): [East, East, East],
            (2, 6): [East, East, East, East],
            (2, 7): [West, West, West, West, West],
            (2, 8): [West, West, West, West],
            (2, 9): [West, West, West],
            (3, 0): [West, West, West],
            (3, 1): [West, West],
            (3, 2): [West],
            (3, 3): [],
            (3, 4): [East],
            (3, 5): [East, East],
            (3, 6): [East, East, East],
            (3, 7): [East, East, East, East],
            (3, 8): [West, West, West, West, West],
            (3, 9): [West, West, West, West],
            (4, 0): [West, West, West, West],
            (4, 1): [West, West, West],
            (4, 2): [West, West],
            (4, 3): [West],
            (4, 4): [],
            (4, 5): [East],
            (4, 6): [East, East],
            (4, 7): [East, East, East],
            (4, 8): [East, East, East, East],
            (4, 9): [West, West, West, West, West],
            (5, 0): [West, West, West, West, West],
            (5, 1): [West, West, West, West],
            (5, 2): [West, West, West],
            (5, 3): [West, West],
            (5, 4): [West],
            (5, 5): [],
            (5, 6): [East],
            (5, 7): [East, East],
            (5, 8): [East, East, East],
            (5, 9): [East, East, East, East],
            (6, 0): [East, East, East, East],
            (6, 1): [West, West, West, West, West],
            (6, 2): [West, West, West, West],
            (6, 3): [West, West, West],
            (6, 4): [West, West],
            (6, 5): [West],
            (6, 6): [],
            (6, 7): [East],
            (6, 8): [East, East],
            (6, 9): [East, East, East],
            (7, 0): [East, East, East],
            (7, 1): [East, East, East, East],
            (7, 2): [West, West, West, West, West],
            (7, 3): [West, West, West, West],
            (7, 4): [West, West, West],
            (7, 5): [West, West],
            (7, 6): [West],
            (7, 7): [],
            (7, 8): [East],
            (7, 9): [East, East],
            (8, 0): [East, East],
            (8, 1): [East, East, East],
            (8, 2): [East, East, East, East],
            (8, 3): [West, West, West, West, West],
            (8, 4): [West, West, West, West],
            (8, 5): [West, West, West],
            (8, 6): [West, West],
            (8, 7): [West],
            (8, 8): [],
            (8, 9): [East],
            (9, 0): [East],
            (9, 1): [East, East],
            (9, 2): [East, East, East],
            (9, 3): [East, East, East, East],
            (9, 4): [West, West, West, West, West],
            (9, 5): [West, West, West, West],
            (9, 6): [West, West, West],
            (9, 7): [West, West],
            (9, 8): [West],
            (9, 9): []
        }, {
            (0, 0): [],
            (0, 1): [North],
            (0, 2): [North, North],
            (0, 3): [North, North, North],
            (0, 4): [North, North, North, North],
            (0, 5): [South, South, South, South, South],
            (0, 6): [South, South, South, South],
            (0, 7): [South, South, South],
            (0, 8): [South, South],
            (0, 9): [South],
            (1, 0): [South],
            (1, 1): [],
            (1, 2): [North],
            (1, 3): [North, North],
            (1, 4): [North, North, North],
            (1, 5): [North, North, North, North],
            (1, 6): [South, South, South, South, South],
            (1, 7): [South, South, South, South],
            (1, 8): [South, South, South],
            (1, 9): [South, South],
            (2, 0): [South, South],
            (2, 1): [South],
            (2, 2): [],
            (2, 3): [North],
            (2, 4): [North, North],
            (2, 5): [North, North, North],
            (2, 6): [North, North, North, North],
            (2, 7): [South, South, South, South, South],
            (2, 8): [South, South, South, South],
            (2, 9): [South, South, South],
            (3, 0): [South, South, South],
            (3, 1): [South, South],
            (3, 2): [South],
            (3, 3): [],
            (3, 4): [North],
            (3, 5): [North, North],
            (3, 6): [North, North, North],
            (3, 7): [North, North, North, North],
            (3, 8): [South, South, South, South, South],
            (3, 9): [South, South, South, South],
            (4, 0): [South, South, South, South],
            (4, 1): [South, South, South],
            (4, 2): [South, South],
            (4, 3): [South],
            (4, 4): [],
            (4, 5): [North],
            (4, 6): [North, North],
            (4, 7): [North, North, North],
            (4, 8): [North, North, North, North],
            (4, 9): [South, South, South, South, South],
            (5, 0): [South, South, South, South, South],
            (5, 1): [South, South, South, South],
            (5, 2): [South, South, South],
            (5, 3): [South, South],
            (5, 4): [South],
            (5, 5): [],
            (5, 6): [North],
            (5, 7): [North, North],
            (5, 8): [North, North, North],
            (5, 9): [North, North, North, North],
            (6, 0): [North, North, North, North],
            (6, 1): [South, South, South, South, South],
            (6, 2): [South, South, South, South],
            (6, 3): [South, South, South],
            (6, 4): [South, South],
            (6, 5): [South],
            (6, 6): [],
            (6, 7): [North],
            (6, 8): [North, North],
            (6, 9): [North, North, North],
            (7, 0): [North, North, North],
            (7, 1): [North, North, North, North],
            (7, 2): [South, South, South, South, South],
            (7, 3): [South, South, South, South],
            (7, 4): [South, South, South],
            (7, 5): [South, South],
            (7, 6): [South],
            (7, 7): [],
            (7, 8): [North],
            (7, 9): [North, North],
            (8, 0): [North, North],
            (8, 1): [North, North, North],
            (8, 2): [North, North, North, North],
            (8, 3): [South, South, South, South, South],
            (8, 4): [South, South, South, South],
            (8, 5): [South, South, South],
            (8, 6): [South, South],
            (8, 7): [South],
            (8, 8): [],
            (8, 9): [North],
            (9, 0): [North],
            (9, 1): [North, North],
            (9, 2): [North, North, North],
            (9, 3): [North, North, North, North],
            (9, 4): [South, South, South, South, South],
            (9, 5): [South, South, South, South],
            (9, 6): [South, South, South],
            (9, 7): [South, South],
            (9, 8): [South],
            (9, 9): []
        }
    
move_x2, move_y2 = loadData()
def naviTo(x, y):
    for fx in move_x2[get_pos_x(), x]:
        move(fx)
    for fy in move_y2[get_pos_y(), y]:
        move(fy)

def bench():
    # set_farm_size(5)
    # set_execution_speed(2)
    clear()
    start = get_time()

    naviTo(6,6)
    # move_x2, move_y2 = loadData()
    # move_x2,move_y2 = Generate_data()
    quick_print(str(get_time()-start))
    
    clear()
    start = get_op_count()

    naviTo(6,6)
    # move_x2, move_y2 = loadData()
    # move_x2,move_y2 = Generate_data()
    quick_print(get_op_count()-start-4)
bench()