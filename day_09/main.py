from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text().strip()


def translate_disk_map(file_blocks: str) -> list[str]:
    output = []
    id = 0
    for index, block in enumerate(file_blocks):
        if index % 2 == 0:
            output.extend([str(id) for i in range(int(block))])
            id += 1
        else:
            output.extend(["." for i in range(int(block))])
    return output


def sort_from_end(list_disk_map: list[str]) -> list[str]:
    n = len(list_disk_map)
    
    dot_ptr = 0
    digit_ptr = n - 1
    
    while dot_ptr < digit_ptr:
        while list_disk_map[dot_ptr] != '.':
            dot_ptr += 1
    
        while digit_ptr >= 0 and list_disk_map[digit_ptr] == '.':
            digit_ptr -= 1
        
        if dot_ptr < digit_ptr:
            list_disk_map[dot_ptr], list_disk_map[digit_ptr] = list_disk_map[digit_ptr], list_disk_map[dot_ptr]
    
    return list_disk_map


def checksum(list_disk_map: list[str]):
    final_sum = 0
    for id, block in enumerate(list_disk_map):
        if block != '.':
            final_sum += id * int(block)
        else:
            break
    return final_sum


def main():
    data = import_data("day_09/data/input.txt")
    logger.info(data)
    disk_map = translate_disk_map(data)
    logger.info(disk_map)
    sorted_disk_map = sort_from_end(disk_map)
    logger.info(sorted_disk_map)
    checksum_value = checksum(sorted_disk_map)
    logger.info(checksum_value)

if __name__ == "__main__":
    main()