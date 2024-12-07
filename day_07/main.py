from itertools import combinations
import operator
from pathlib import Path


from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text()


def split_test_value_operation(text: str):
    return_dict = {}
    for line in text.split('\n'):
        testvalue, operation = line.split(':')
        return_dict[int(testvalue)] = list(map(int, operation.split()))
    return return_dict


def add_operators(operations: dict):
    total = 0
    ops = {'+': operator.add, '*': operator.mul}
    for testvalue, operation in operations.items():
        operators = '+*'*(len(operation)-1)
        combs = set(combinations(operators, len(operation)-1))
        for comb in combs:
            evaluated = ops[comb[0]](operation[0], operation[1])
            string_evaluated = f"{operation[0]} {comb[0]} {operation[1]} "
            for index in range(1, len(comb)):
                evaluated = ops[comb[index]](evaluated, operation[index+1])
                string_evaluated += f"{comb[index]} {operation[index+1]} "
                if evaluated > testvalue:
                    break
            if evaluated == testvalue:
                logger.info(f"{string_evaluated} = {testvalue}")
                total += testvalue
                logger.debug(f"Total: {total}")
                break
    return total


def main():
    data = import_data("day_07/data/input.txt")
    operations = split_test_value_operation(data)
    total = add_operators(operations)
    logger.info("Previous: 3312271364788")
    logger.info(f"Total: {total}")




if __name__ == "__main__":
    main()