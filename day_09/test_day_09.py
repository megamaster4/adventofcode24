from day_09.main import translate_disk_map, sort_from_end, checksum


def test_day_09_task_1_translate_disk_map():
    example = ['0', '.', '.', '1', '1', '1', '.', '.', '.', '.', '2', '2', '2', '2', '2']
    assert translate_disk_map("12345") == example


def test_day_09_task_1_translate_disk_map_2():
    example = ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9']
    assert translate_disk_map("2333133121414131402") == example


def test_day_09_task_1_translate_disk_map_3():
    example = ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9', '10', '10', '10']
    assert translate_disk_map("233313312141413140203") == example


def test_day_09_task_1_sort():
    example = ['0', '.', '.', '1', '1', '1', '.', '.', '.', '.', '2', '2', '2', '2', '2']
    correct = ['0', '2', '2', '1', '1', '1', '2', '2', '2', '.', '.', '.', '.', '.', '.']
    assert sort_from_end(example) == correct


def test_day_09_task_1_sort_2():
    example = ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9']
    correct = ['0', '0', '9', '9', '8', '1', '1', '1', '8', '8', '8', '2', '7', '7', '7', '3', '3', '3', '6', '4', '4', '6', '5', '5', '5', '5', '6', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    assert sort_from_end(example) == correct


def test_day_09_task_1_sort_3():
    example = ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9', '10', '10', '10']
    correct = ['0', '0', '10', '10', '10', '1', '1', '1', '9', '9', '8', '2', '8', '8', '8', '3', '3', '3', '7', '4', '4', '7', '5', '5', '5', '5', '7', '6', '6', '6', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    assert sort_from_end(example) == correct


def test_day_09_task_1_checksum():
    example = ['0', '0', '9', '9', '8', '1', '1', '1', '8', '8', '8', '2', '7', '7', '7', '3', '3', '3', '6', '4', '4', '6', '5', '5', '5', '5', '6', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    assert checksum(example) == 1928