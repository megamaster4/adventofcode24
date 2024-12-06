from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text()


def transform_input(input_string: str) -> list[str]:
    page_ordering_rules, page_numbers = input_string.split(sep='\n\n')
    return page_ordering_rules.split(sep='\n'), page_numbers.split(sep='\n')


def construct_page_order_dict(page_ordering_rules: list[str]) -> dict[str, list[str]]:
    prio_numbers = set(item.split('|')[0] for item in page_ordering_rules)
    return {number: [rule.split('|')[1] for rule in page_ordering_rules if f'{number}|' in rule] for number in prio_numbers}


def check_order(number_order_to_check: list[str], page_order_dict: dict[str, list[str]]) -> bool:
    for index, value in enumerate(number_order_to_check):
        rules = page_order_dict.get(value)
        if rules is None:
            continue
        for index2, number in enumerate(number_order_to_check):
            if number == value:
                continue
            if number in rules:
                if index > index2:
                    return False
    return True


def set_correct_order(incorrect: list[str], numbers: dict[str, list[str]]) -> list[str]:
    while True: 
        for index, number in enumerate(incorrect):
            if numbers.get(number) is None:
                continue
            for rule in numbers.get(number):
                if rule in incorrect:
                    if incorrect.index(rule) < index:
                        incorrect.remove(rule)
                        incorrect.insert(index, rule)
        if check_order(incorrect, numbers):
            return incorrect


def get_middle_sum(correct_rows_list: list[str]) -> int:
    return sum([int(row[int((len(row))/2)]) for row in correct_rows_list])
    


def main():
    data = import_data(file_path='./day_05/data/input.txt')
    page_ordering_rules, page_numbers = transform_input(data)
    numbers = construct_page_order_dict(page_ordering_rules)

    correct_rows = []
    incorrect_rows = []
    for row in page_numbers:
        row_splitted = row.split(',')
        if check_order(row_splitted, numbers):
            correct_rows.append(row_splitted)
        else:
            incorrect_rows.append(row)


    middle_sum = get_middle_sum(correct_rows)
    logger.info(f"The sum of the middle numbers in correct rows is: {middle_sum}")
    
    corrected_rows = []
    for row in incorrect_rows:
        incorrect = row.split(',')
        corrected_rows.append(set_correct_order(incorrect, numbers))

    middle_sum = get_middle_sum(corrected_rows)
    logger.info(f"The sum of the middle numbers in corrected rows is: {middle_sum}")

if __name__ == '__main__':
    main()