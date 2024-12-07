from day_07.main import split_test_value_operation, add_operators


def test_day_07_task_1():
    example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    operations = split_test_value_operation(example)
    total = add_operators(operations)
    assert total == 3749


def test_day_07_single():
    # 34 + 60 + 8 + 98 + 8 * 385 * 65  = 5205200
    example = """5205200: 34 60 8 98 8 385 65"""
    operations = split_test_value_operation(example)
    total = add_operators(operations)
    assert total == 5205200