import numpy as np
from pathlib import Path

from loguru import logger

def import_data(file_path: str):
    return Path(file_path).read_text()


def create_matrix_from_text(text: str) -> np.array:
    lines = text.strip().split('\n')
    return np.array([list(line) for line in lines])


def direction_delta(direction: int) -> tuple:
    direction_corrected = direction % 360
    if direction_corrected == 0:
        return -1, 0
    elif direction_corrected == 90:
        return 0, 1
    elif direction_corrected == 180:
        return 1, 0
    elif direction_corrected == 270:
        return 0, -1
    else:
        raise ValueError(f"Invalid direction: {direction}")


def direction_checker(matrix: np.array, y: int, x: int, direction: int) -> bool:
    y_left, x_left, _ = direction_delta(direction + 90)
    if matrix[y + y_left, x + x_left] in '|-+':
        return [y, x]


# if direction_marker and matrix[y, x] != '+':
#             loop_check = direction_checker(matrix, y, x, direction)
#             if loop_check:
#                 loop_points.append(loop_check)

def guard_walk(matrix: np.array, y: int, x: int) -> np.array:
    matrix[y, x] = 'X'
    direction = 0
    while True:
        y_delta, x_delta = direction_delta(direction)
        y = y + y_delta
        x = x + x_delta  
        if y < 0 or y >= matrix.shape[0] or x < 0 or x >= matrix.shape[1]:
            return matrix
        elif matrix[y, x] in '#':
            direction += 90
            y -= y_delta
            x -= x_delta
        else:
            matrix[y, x] = 'X'


def guard_walk_2(matrix: np.array, y: int, x: int, direction_marker: bool = True) -> np.array:
    matrix[y, x] = 'X'
    direction = 0
    for i in range(7500):
        y_delta, x_delta = direction_delta(direction)
        y = y + y_delta
        x = x + x_delta  
        if y < 0 or y >= matrix.shape[0] or x < 0 or x >= matrix.shape[1]:
            return 0
        elif matrix[y, x] in '#O':
            direction += 90
            y -= y_delta
            x -= x_delta
        else:
            matrix[y, x] = 'X'
    logger.info(f"Loop detected at {y}, {x}")
    return 1


def get_distinct_positions(matrix: np.array) -> list:
    return len(np.where(matrix == 'X')[0])


def main():
    data = import_data("./day_06/data/input.txt")
    matrix = create_matrix_from_text(data)
    y_start, x_start = np.where(matrix == '^')
    y = y_start[0]
    x = x_start[0]
    walk_matrix = guard_walk(np.copy(matrix), y, x)
    distinct_positions = get_distinct_positions(walk_matrix)

    logger.info(f"Distinct positions: {distinct_positions}")

    y_x, x_x = np.where(walk_matrix == 'X')
    loops = 0
    for i, j in zip(y_x, x_x):
        task2_matrix = np.copy(matrix)
        if task2_matrix[i,j] == '#':
            continue
        task2_matrix[i, j] = 'O'
        loops += guard_walk_2(task2_matrix, y, x, direction_marker=True)
    
    logger.info(f"Distinct loops: {loops}")

if __name__ == "__main__":
    main()