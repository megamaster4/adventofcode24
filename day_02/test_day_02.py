import numpy as np

from day_02.main import get_differences_arr, check_safety, check_safety_problem_dampener


def test_get_differences_matrix():
    matrix = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    test_diffs = [
        [-1, -2, -2, -1],
        [1, 5, 1, 1],
        [-2, -1, -4, -1],
        [2, -1, 2, 1],
        [-2, -2, 0, -3],
        [2, 3, 1, 2],
    ]

    for arr, diff in zip(matrix, test_diffs):
        calc_diff = get_differences_arr(arr)
        assert np.array_equal(diff, calc_diff)


def test_check_safety():
    matrix = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    safe_reports = 0
    for arr in matrix:
        diffs = get_differences_arr(arr)
        safe_reports += check_safety(diffs)

    assert safe_reports == 2


def test_check_safety_problem_dampener():
    matrix = np.array(
        [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
    )
    safe_reports = 0
    for arr in matrix:
        safe_reports += check_safety_problem_dampener(arr)

    assert safe_reports == 4
