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
        for operation in numbers:
            if not evaluate_expressions(operation, key, combination_counter=combination_counter):
                logger.info(f"No valid expression found for target: {key}")
            else:
                logger.info(f"Valid expression found for target: {key}")
                total += key
            logger.info(f"Combinations: {combination_counter[0]}")

    assert total == 3749


def test_day_07_task_2():
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
        for operation in numbers:
            if not evaluate_expressions(operation, key, combination_counter=combination_counter, concat=True):
                logger.info(f"No valid expression found for target: {key}")
            else:
                logger.info(f"Valid expression found for target: {key}")
                total += key
            logger.info(f"Combinations: {combination_counter[0]}")

    assert total == 11387