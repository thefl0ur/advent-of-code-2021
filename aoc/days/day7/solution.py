import statistics

from typing import List


def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        data = [int(x) for x in file.readline().split(',')]
    return data


def part1(file_path: str) -> int:
    data = read_data(file_path)
    target_point = statistics.median(data)
    return sum([abs(x - target_point) for x in data])


def part2(file_path: str) -> int:
    raise NotImplemented('No code for day7 part 2')
