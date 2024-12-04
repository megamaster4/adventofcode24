import numpy as np

from loguru import logger

def create_matrix_from_text(text: str) -> np.array:
    lines = text.strip().split('\n')
    return np.array([list(line) for line in lines])





def find_xmas_both(arr: np.array, x: int) -> bool:
    logger.debug(f"Array: {arr}")
    logger.debug(f"X: {x}")
    def find_xmas(arr: list[str], x: int) -> int:
        try:
            if arr[x+1] == 'M':
                if arr[x+2] == 'A':
                    if arr[x+3] == 'S':
                        return 1
        except IndexError:
            return 0
        return 0
    return sum([find_xmas(arr=arr, x=x), find_xmas(arr=np.flip(arr), x=len(arr)-1-x)])



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


    matrix = create_matrix_from_text(text=matrix_txt)
    logger.info(f"Matrix: \n {matrix}")
    y, x = np.where(matrix == 'X')
    count_horizontal = 0
    count_vertical = 0
    count_diagonal_1 = 0
    count_diagonal_2 = 0
    for row, column in zip(y, x):
        logger.debug(f'Row: {row}')
        logger.debug(f'Column: {column}')
        count_horizontal += find_xmas_both(arr=matrix[row], x=column)
        count_vertical += find_xmas_both(arr=matrix[:, column], x=row)
        diagonal_1 = np.diagonal(matrix, offset=column-row)
        count_diagonal_1 += find_xmas_both(arr=diagonal_1, x=column)
        diagonal_2 = np.diagonal(np.flipud(matrix), offset=(matrix.shape[1] - 1 - column) - row)
        count_diagonal_2 += find_xmas_both(arr=diagonal_2, x=row)



    logger.info(f"Number of XMAS in horizontal: {count_horizontal}")
    logger.info(f"Number of XMAS in vertical: {count_vertical}")
    logger.info(f"Number of XMAS in diagonal: {count_diagonal_1}")
    logger.info(f"Number of XMAS in diagonal: {count_diagonal_2}")
    logger.info(f"Total number of XMAS: {count_horizontal + count_vertical + count_diagonal_1 + count_diagonal_2}")
    


if __name__ == "__main__":
    main()