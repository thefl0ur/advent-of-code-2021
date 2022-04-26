from collections import Counter
from typing import List, Tuple

from bitarray import bitarray
from bitarray.util import ba2int

CO_2_CRITERIA = (0, 1)
OXYGEN_CRITERIA = (1, 0)


def get_column(matrix: List[List[int]], column_index: int) -> List[int]:
    return [row[column_index] for row in matrix]


def part1(file_path: str) -> int:
    with open(file_path, 'r') as file:
        original_data = [line.strip() for line in file]

    data = bitarray([
        int(Counter(get_column(original_data, index)).most_common(1)[0][0]) for
        index in range(len(original_data[0]))
    ])
    return ba2int(data) * ba2int(~data)


def get_criteria_bit(line: List[int], bits: Tuple[int, int] = CO_2_CRITERIA) -> int:
    return bits[0] if sum(line) >= (len(line)/2) else bits[1]


# TODO instead of temp_data list use list of indexes
def get_rating(
    data: List[List[int]], index: int = 0, bits: Tuple[int, int] = OXYGEN_CRITERIA
) -> List[List[int]]:
    if len(data) == 1:
        return data

    most_common_value = get_criteria_bit(get_column(data, index), bits)
    temp_data = [line for line in data if line[index] == most_common_value]

    index += 1
    return get_rating(temp_data, index, bits)


def part2(file_path: str) -> int:
    with open(file_path, 'r') as file:
        original_data = [list(map(int, line.strip())) for line in file]

    oxy_raw_data = get_rating(original_data, bits=OXYGEN_CRITERIA)
    co2_raw_data = get_rating(original_data, bits=CO_2_CRITERIA)

    oxy = ba2int(bitarray(x for x in oxy_raw_data[0]))
    co2 = ba2int(bitarray(x for x in co2_raw_data[0]))

    return oxy * co2
