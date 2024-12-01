import numpy as np

from day_01.main import get_distance

def test_get_distance():
    left = np.array([3, 4, 2, 1, 3, 3])
    right = np.array([4, 3, 5, 3, 9, 3])

    distance = get_distance(left, right)
    assert np.array_equal(distance, np.array([2, 1, 0, 1, 2, 5]))
    assert np.sum(distance) == 11