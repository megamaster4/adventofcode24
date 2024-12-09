from pathlib import Path

from loguru import logger


def import_data(file_path: str):
    return Path(file_path).read_text()


def translate_disk_map(file_blocks: str):
    output = ""
    id = 0
    for index, block in enumerate(file_blocks):
        if index % 2 == 0:
            output += f"{id}" * int(block)
            id += 1
        else:
            output += "." * int(block)
    return output


def get_last_int(disk_map: list[str]):
    for index, block in enumerate(disk_map[::-1]):
        if block.isdigit():
            return index + 1
        else:
            continue


def sort_from_end(disk_map: str):
    list_disk_map = list(disk_map)
    try:
        for idx, block in enumerate(list_disk_map):
            if block != '.':
                continue
            else:
                index = -1
                while True:
                    if list_disk_map[index] != '.':
                        list_disk_map[idx] = list_disk_map[index]
                        list_disk_map[index] = '.'
                        break
                    elif (len(list_disk_map) + index - 1) < idx:
                        break
                    else:
                        index -= 1
    except IndexError:
        pass
    for i in range(len(list_disk_map), len(disk_map)):
        list_disk_map.append('.')
    return "".join(list_disk_map)


def checksum(disk_map: str):
    final_sum = 0
    for id, block in enumerate(disk_map):
        if block != '.':
            final_sum += id * int(block)
    return final_sum
    

def main():
    data = import_data("day_09/data/input.txt")
    disk_map = translate_disk_map(data)
    logger.info(disk_map)
    sorted_disk_map = sort_from_end(disk_map)
    logger.info(sorted_disk_map)
    checksum_value = checksum(sorted_disk_map)
    logger.info(checksum_value)

if __name__ == "__main__":
    main()