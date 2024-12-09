from day_09.main import translate_disk_map, sort_from_end, checksum


def test_day_09_task_1_translate_disk_map():
    example = """0..111....22222"""
    assert translate_disk_map("12345") == example


def test_day_09_task_1_translate_disk_map_2():
    example = """00...111...2...333.44.5555.6666.777.888899"""
    assert translate_disk_map("2333133121414131402") == example


def test_day_09_task_1_sort():
    example = """0..111....22222"""
    correct = """022111222......"""
    assert sort_from_end(example) == correct


def test_day_09_task_1_sort_2():
    example = """00...111...2...333.44.5555.6666.777.888899"""
    correct = """0099811188827773336446555566.............."""
    assert sort_from_end(example) == correct


def test_day_09_task_1_checksum():
    example = """0099811188827773336446555566.............."""
    assert checksum(example) == 1928