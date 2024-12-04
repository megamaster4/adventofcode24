import re
from pathlib import Path

from loguru import logger

def import_data(file_path: str):
    return Path(file_path).read_text()


def find_correct_sections(memory: str) -> list:
    return re.findall(pattern=r"mul\([0-9]{0,3},[0-9]{0,3}\)", string=memory)


def find_correct_sections_do_dont(memory: str) -> list:
    return re.findall(pattern=r"mul\([0-9]{0,3},[0-9]{0,3}\)|don't\(\)|do\(\)", string=memory)


def assign_do_dont(memory: list[str]) -> str:
    trigger = True
    corrected_memory = []
    for item in memory:
        if "don't" in item:
            trigger = False
        elif "do" in item:
            trigger = True
        else:
            if trigger:
                corrected_memory.append(item)
    return corrected_memory


def multiply_numbers(correct_memory: str) -> int:
    return int(correct_memory.split(",")[0][4:]) * int(correct_memory.split(",")[1][:-1])


def main():
    memory = import_data(file_path="./day_03/data/input.txt")

    regex = find_correct_sections(memory=memory)
    mult = sum(multiply_numbers(correct_memory=item) for item in regex)
    logger.info(f"The sum of all correct memory in task 1 is: {mult}")

    regex = find_correct_sections_do_dont(memory=memory)
    assign_memory = assign_do_dont(memory=regex)
    mult = sum(multiply_numbers(correct_memory=item) for item in assign_memory)
    logger.info(f"The sum of all correct memory in task 2 is: {mult}")


if __name__ == "__main__":
    main()