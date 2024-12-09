import numpy as np
from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text()


def export_data(file_path: str, data: np.array):
    # Write numpy array matrix to text file
    data = '\n'.join(''.join(map(str, row)) for row in data)
    Path(file_path).write_text(data)


def create_matrix_from_text(text: str) -> np.array:
    lines = text.strip().split('\n')
    return np.array([list(line) for line in lines])


def build_antenna_points(matrix: np.array) -> dict:
    all_antenna = np.unique(matrix)
    antenna_points = {}
    for antenna in all_antenna:
        if antenna == '.':
            continue
        if antenna in antenna_points:
            antenna_points[antenna].append(np.where(matrix == antenna))
        else:
            antenna_points[antenna] = [np.where(matrix == antenna)]
    return antenna_points


def process_antenna_points(matrix, antenna, unique_antenna):
    unique_locations = []
    for antenna_list in antenna.values():
        for antenna_coords in antenna_list:
            for index in range(len(antenna_coords[0])):
                for index_2 in range(len(antenna_coords[0])):
                    if index == index_2:
                        continue
                    y1, x1 = antenna_coords[0][index], antenna_coords[1][index]
                    logger.info(f"y1: {y1}, x1: {x1}")
                    y2, x2 = antenna_coords[0][index_2], antenna_coords[1][index_2]
                    logger.info(f"y2: {y2}, x2: {x2}")
                    dist_y, dist_x = calc_manhattan_distance(y1, x1, y2, x2)
                    logger.info(f"Distance between antennas: {dist_y}, {dist_x}")
                    # Decide which point is higher and which is lower
                    # If the distance between the two points is greater in the y direction
                    # then the point with the higher y value is the antinode
                    antinode_1 = []
                    antinode_2 = []
                    if y1 < y2:
                        antinode_1.append(-dist_y)
                        antinode_2.append(dist_y)
                    else:
                        antinode_1.append(dist_y)
                        antinode_2.append(-dist_y)
                    if x1 < x2:
                        antinode_1.append(-dist_x)
                        antinode_2.append(dist_x)
                    else:
                        antinode_1.append(dist_x)
                        antinode_2.append(-dist_x)

                    for point, antinode in zip([[y1, x1], [y2, x2]], [antinode_1, antinode_2]):
                        new_y, new_x = point[0] + antinode[0], point[1] + antinode[1]
                        if 0 <= new_y < matrix.shape[0] and 0 <= new_x < matrix.shape[1]:
                            if matrix[new_y, new_x] == '.':
                                matrix[new_y, new_x] = '#'
                                if [new_y, new_x] not in unique_locations:
                                    unique_locations.append([new_y, new_x])
                            if matrix[new_y, new_x] in unique_antenna and [new_y, new_x] not in unique_locations:
                                unique_locations.append([new_y, new_x])
                        else:
                            continue
    return matrix, unique_locations


def process_antenna_points_2(matrix, antenna, unique_antenna):
    unique_locations = []
    for antenna_list in antenna.values():
        for antenna_coords in antenna_list:
            for index in range(len(antenna_coords[0])):
                for index_2 in range(len(antenna_coords[0])):
                    if index == index_2:
                        continue
                    y1, x1 = antenna_coords[0][index], antenna_coords[1][index]
                    logger.info(f"y1: {y1}, x1: {x1}")
                    y2, x2 = antenna_coords[0][index_2], antenna_coords[1][index_2]
                    logger.info(f"y2: {y2}, x2: {x2}")
                    dist_y, dist_x = calc_manhattan_distance(y1, x1, y2, x2)
                    logger.info(f"Distance between antennas: {dist_y}, {dist_x}")
                    # Decide which point is higher and which is lower
                    # If the distance between the two points is greater in the y direction
                    # then the point with the higher y value is the antinode
                    if [y1, x1] not in unique_locations:
                        unique_locations.append([y1, x1])
                    if [y2, x2] not in unique_locations:
                        unique_locations.append([y2, x2])
                    for i in range(1, 100):
                        antinode_1 = []
                        antinode_2 = []
                        if y1 < y2:
                            antinode_1.append(-dist_y*i)
                            antinode_2.append(dist_y*i)
                        else:
                            antinode_1.append(dist_y*i)
                            antinode_2.append(-dist_y*i)
                        if x1 < x2:
                            antinode_1.append(-dist_x*i)
                            antinode_2.append(dist_x*i)
                        else:
                            antinode_1.append(dist_x*i)
                            antinode_2.append(-dist_x*i)

                        for point, antinode in zip([[y1, x1], [y2, x2]], [antinode_1, antinode_2]):
                            new_y, new_x = point[0] + antinode[0], point[1] + antinode[1]
                            if 0 <= new_y < matrix.shape[0] and 0 <= new_x < matrix.shape[1]:
                                if matrix[new_y, new_x] == '.':
                                    matrix[new_y, new_x] = '#'
                                    if [new_y, new_x] not in unique_locations:
                                        unique_locations.append([new_y, new_x])
                                if matrix[new_y, new_x] in unique_antenna and [new_y, new_x] not in unique_locations:
                                    unique_locations.append([new_y, new_x])
                            else:
                                continue
    return matrix, unique_locations


def calc_manhattan_distance(y1: int, x1: int, y2: int, x2: int) -> int:
    return abs(y1 - y2), abs(x1 - x2)


def main():
    data = import_data("day_08/data/input.txt")
    matrix = create_matrix_from_text(data)
    antenna_points = build_antenna_points(matrix)
    
    result_matrix, unique_locations = process_antenna_points(matrix, antenna_points, antenna_points.keys())
    logger.info(f"Matrix after processing:\n{result_matrix}")
    logger.info(f"Number of unique locations: {len(unique_locations)}")
    
    
    data = import_data("day_08/data/input.txt")
    matrix = create_matrix_from_text(data)
    antenna_points = build_antenna_points(matrix)

    result_matrix, unique_locations = process_antenna_points_2(matrix, antenna_points, antenna_points.keys())
    logger.info(f"Matrix after processing:\n{result_matrix}")
    logger.info(f"Number of unique locations: {len(unique_locations)}")




if __name__ == '__main__':
    main()