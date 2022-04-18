from typing import List


def read_data(file_name: str) -> List[int]:
    with open(file_name, 'r') as file:
        return [int(line) for line in file]


def get_increments_count(input_data, window_size):
    return sum(
        [1 if input_data[index] < input_data[index+window_size] else 0
            for index in range(0, len(input_data)-window_size)])


def part1(input_data: str) -> int:
    return get_increments_count(read_data(input_data), 1)


def part2(input_data: str) -> int:
    return get_increments_count(read_data(input_data), 3)
