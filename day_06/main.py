import numpy as np
from pathlib import Path

from loguru import logger

def import_data(file_path: str):
    return Path(file_path).read_text()


def create_matrix_from_text(text: str) -> np.array:
    lines = text.strip().split('\n')
    return np.array([list(line) for line in lines])


def direction_delta(direction: int, direction_marker: bool = False) -> tuple:
    direction_corrected = direction % 360
    if direction_corrected == 0:
        return -1, 0, '|' if direction_marker else 'X'
    elif direction_corrected == 90:
        return 0, 1, '-' if direction_marker else 'X'
    elif direction_corrected == 180:
        return 1, 0, '|' if direction_marker else 'X'
    elif direction_corrected == 270:
        return 0, -1, '-' if direction_marker else 'X'
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
        y_delta, x_delta, marker = direction_delta(direction)
        y = y + y_delta
        x = x + x_delta  
        if y < 0 or y >= matrix.shape[0] or x < 0 or x >= matrix.shape[1]:
            return matrix
        elif matrix[y, x] in '#':
            direction += 90
            y -= y_delta
            x -= x_delta
            if marker != 'X':
                matrix[y, x] = '+'
        else:
            matrix[y, x] = marker


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


if __name__ == "__main__":
    main()