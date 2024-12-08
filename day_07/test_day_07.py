from day_07.main import split_test_value_operation, evaluate_expressions


from loguru import logger

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
    total = 0
    for key, numbers in operations.items():
        logger.info(f"Evaluating for target: {key} with numbers: {numbers}")
        combination_counter = [0]
        if not evaluate_expressions(numbers, key, combination_counter=combination_counter):
            logger.info(f"No valid expression found for target: {key}")
        else:
            logger.info(f"Valid expression found for target: {key}")
            total += key
        logger.info(f"Combinations: {combination_counter[0]}")

    assert total == 3749


def test_day_07_single():
    # 34 + 60 + 8 + 98 + 8 * 385 * 65  = 5205200
    example = """38998774089: 1 9 3 9 3 5 2 417 8 63 7 2"""
    operations = split_test_value_operation(example)
    total = 0
    for key, numbers in operations.items():
        logger.info(f"Evaluating for target: {key} with numbers: {numbers}")
        combination_counter = [0]
        if not evaluate_expressions(numbers, key, combination_counter=combination_counter):
            logger.info(f"No valid expression found for target: {key}")
        else:
            logger.info(f"Valid expression found for target: {key}")
            total += key
        logger.info(f"Combinations: {combination_counter[0]}")
    assert total == 0