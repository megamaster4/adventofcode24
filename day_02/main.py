import numpy as np
from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    data = Path(file_path).read_text().splitlines()
    data_splitted = [list(map(int, i.split())) for i in data]

    return data_splitted


def get_differences_arr(list: list[int]) -> np.array:
    return np.diff(np.array(list))


def check_safety(data: list[list[int]]) -> bool:
    logger.info("Checking differences")
    safe_reports = 0
    for arr in data:
        diffs = get_differences_arr(arr)

        logger.info("Checking safety")
        # The levels are either all increasing or all decreasing.
        all_positive_or_negative = np.all(diffs > 0) | np.all(diffs < 0)
        # Any two adjacent levels differ by at least one and at most three.
        within_range = np.all((1 <= np.abs(diffs)) & (np.abs(diffs) <= 3))

        if all_positive_or_negative & within_range:
            safe_reports += 1

    return safe_reports


def main():
    data = import_data(file_path="./day_02/data/input.txt")
    logger.info(f"Imported data: {data}")

    safe_reports = check_safety(data)
    logger.info(f"Number of safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
