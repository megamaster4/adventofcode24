import numpy as np
from pathlib import Path

from loguru import logger

def import_data(file_path: str):
    return Path(file_path).read_text()


def create_matrix_from_text(text: str) -> np.array:
    lines = text.strip().split('\n')
    return np.array([list(line) for line in lines])


def main():
    example ="""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
    matrix = create_matrix_from_text(example)
    logger.info(matrix)


if __name__ == "__main__":
    main()