import numpy as np
from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text()


def create_matrix_from_text(text: str) -> np.array:
    lines = text.strip().split('\n')
    return np.array([list(line) for line in lines])


def find_xmas(arr: list[str], x: int) -> int:
        try:
            if arr[x+1] == 'M':
                if arr[x+2] == 'A':
                    if arr[x+3] == 'S':
                        return 1
        except IndexError:
            return 0
        return 0


def find_horizontal(matrix: np.array) -> bool:
    count = 0
    for arr in matrix:
        x = np.where(arr == 'X')[0]
        for index in x:
            count += sum([find_xmas(arr=arr, x=index), find_xmas(arr=arr[::-1], x=len(arr)-1-index)])
    return count


def find_vertical(matrix: np.array) -> bool:
    count = 0
    for i in range(matrix.shape[1]):
        arr = matrix[:,i]
        x = np.where(arr== 'X')[0]
        for index in x:
            count += sum([find_xmas(arr=arr, x=index), find_xmas(arr=arr[::-1], x=len(arr)-1-index)])
    return count


def find_diagonal(matrix: np.array) -> bool:
    count = 0
    for i in range(-matrix.shape[0]+1, matrix.shape[1]):
        arr = np.diagonal(matrix, i)
        x = np.where(arr == 'X')[0]
        for index in x:
            count += sum([find_xmas(arr=arr, x=index), find_xmas(arr=arr[::-1], x=len(arr)-1-index)])
    return count


def find_diagonal_reverse(matrix: np.array) -> bool:
    count = 0
    flipped = np.fliplr(matrix)
    for i in range(-flipped.shape[0]+1, flipped.shape[1]):
        arr = np.diagonal(flipped, i)
        x = np.where(arr == 'X')[0]
        for index in x:
            count += sum([find_xmas(arr=arr, x=index), find_xmas(arr=arr[::-1], x=len(arr)-1-index)])
    return count


def main():
    matrix_txt = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    matrix_text = import_data(file_path="./day_04/data/input.txt")
    matrix = create_matrix_from_text(text=matrix_text)
    logger.info(f"Matrix: \n {matrix}")
    count_horizontal = find_horizontal(matrix=matrix)
    count_vertical = find_vertical(matrix=matrix)
    count_diagonal = find_diagonal(matrix=matrix)
    count_diagonal_reverse = find_diagonal_reverse(matrix=matrix)

    logger.info(f"Number of XMAS in horizontal: {count_horizontal}")
    logger.info(f"Number of XMAS in vertical: {count_vertical}")
    logger.info(f"Number of XMAS in diagonal: {count_diagonal}")
    logger.info(f"Number of XMAS in diagonal reverse: {count_diagonal_reverse}")
    logger.info(f"Total number of XMAS: {count_horizontal + count_vertical + count_diagonal + count_diagonal_reverse}")
    


if __name__ == "__main__":
    main()