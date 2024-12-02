import numpy as np
from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    data = Path(file_path).read_text().splitlines()
    data_splitted = [list(map(int, i.split())) for i in data]

    return data_splitted


def get_differences_arr(list: list[int]) -> np.array:
    return np.diff(np.array(list))


def check_safety(data: list[int]) -> int:
    # The levels are either all increasing or all decreasing.
    all_positive_or_negative = np.all(data > 0) | np.all(data < 0)
    # Any two adjacent levels differ by at least one and at most three.
    within_range = np.all((1 <= np.abs(data)) & (np.abs(data) <= 3))

    if all_positive_or_negative & within_range:
        return 1
    else:
        return 0


def check_safety_problem_dampener(data: list[int]) -> int:
    diffs = get_differences_arr(data)
    if check_safety(diffs):
        return 1
    else:
        for index, value in enumerate(data):
            data_2 = np.delete(data, index)
            diffs_2 = get_differences_arr(data_2)
            if check_safety(diffs_2):
                return 1
            else:
                continue
        return 0


def main():
    data = import_data(file_path="./day_02/data/input.txt")
    logger.info("Imported data")

    safe_reports = 0
    for arr in data:
        diffs = get_differences_arr(arr)
        safe_reports += check_safety(diffs)
    logger.info(f"Number of safe reports for task 1: {safe_reports}")

    safe_reports = 0
    for arr in data:
        safe_reports += check_safety_problem_dampener(arr)
    logger.info(f"Number of safe reports for task 2: {safe_reports}")


if __name__ == "__main__":
    main()
