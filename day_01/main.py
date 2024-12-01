import numpy as np
from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    data = Path(file_path).read_text().split()
    return [int(i) for i in data]


def assign_data(data: list[int]):
    left = np.array([])
    right = np.array([])
    for index, value in enumerate(data):
        if index % 2 == 0:
            left = np.append(left, value)
        else:
            right = np.append(right, value)
    return left, right


def get_distance(left, right):
    distance = np.abs(np.sort(left) - np.sort(right))
    return distance


def get_indices_of_number(data: np.array, number: int) -> np.array:
    return np.where(data == number)


def get_similarity(left: np.array, right: np.array) -> int:
    similarity = np.array([])
    for i in left:
        counts = get_indices_of_number(right, i)
        similarity = np.append(similarity, i * len(counts[0]))
    return similarity


def main():
    logger.info("Import data")
    data = import_data(file_path="./day_01/data/input.txt")
    left, right = assign_data(data)
    logger.info(
        f"Assigned data, lenght of left: {len(left)}, lenght of right: {len(right)}"
    )
    distance = get_distance(left, right)
    sum_of_distance = np.sum(distance)
    logger.info(f"Calculated sum of distance: {sum_of_distance}")
    similarity = get_similarity(left, right)
    sum_of_similarity = np.sum(similarity)
    logger.info(f"Calculated similarity score: {sum_of_similarity}")


if __name__ == "__main__":
    main()
