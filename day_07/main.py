from itertools import combinations, product
import operator
from pathlib import Path


from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text()


def split_test_value_operation(text: str):
    return_dict = {}
    for line in text.strip().split('\n'):
        if line.strip():  # Skip empty lines
            testvalue, operation = line.split(':')
            return_dict[int(testvalue)] = list(map(int, operation.strip().split()))
    return return_dict


def evaluate_expressions(numbers, target, current_value=0, index=0, current_expression=None, combination_counter=None):
    if current_expression is None:
        current_expression = []
    if combination_counter is None:
        combination_counter = [0]

    if index == 0:
        current_value = numbers[0]
        current_expression = [numbers[0]]
        index += 1

    if index == len(numbers):
        combination_counter[0] += 1
        if current_value == target:
            logger.info(f"Expression: {' '.join(map(str, current_expression))} = {current_value}")
            return True
        return False

    add_result = evaluate_expressions(numbers, target, current_value + numbers[index], index + 1,
                                      current_expression + ['+', numbers[index]], combination_counter)
    mul_result = evaluate_expressions(numbers, target, current_value * numbers[index], index + 1,
                                      current_expression + ['*', numbers[index]], combination_counter)

    return add_result or mul_result


def main():
    data = import_data("day_07/data/input.txt")
    operations = split_test_value_operation(data)
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

    logger.info("Previous: 3312271364788")
    logger.info(f"Total: {total}")




if __name__ == "__main__":
    main()