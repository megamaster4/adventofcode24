import numpy as np

from day_06.main import guard_walk, guard_walk_2, get_distinct_positions


def test_day_06_task_1():
    example = np.array([
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
    ])

    y_start, x_start = np.where(example == '^')
    y = y_start[0]
    x = x_start[0]
    walk_matrix = guard_walk(np.copy(example), y, x)
    distinct_positions = get_distinct_positions(walk_matrix)

    assert distinct_positions == 41


def test_day_06_task_2():
    example = np.array([
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
    ])

    y_start, x_start = np.where(example == '^')
    y = y_start[0]
    x = x_start[0]
    walk_matrix = guard_walk(np.copy(example), y, x)
    y_x, x_x = np.where(walk_matrix == 'X')
    loops = 0
    for i, j in zip(y_x, x_x):
        matrix = np.copy(example)
        if matrix[i,j] == '#':
            continue
        matrix[i, j] = 'O'
        loops += guard_walk_2(matrix, y, x, direction_marker=True)
    assert loops == 6
