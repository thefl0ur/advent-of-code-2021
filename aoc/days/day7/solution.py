import statistics

from typing import List


def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        data = [int(x) for x in file.readline().split(',')]
    return data


def fiel_consumption(point: int) -> float:
    return point * (point + 1) / 2


def part1(file_path: str) -> int:
    data = read_data(file_path)
    target_point = statistics.median(data)
    return int(sum([abs(x - target_point) for x in data]))


def part2(file_path: str) -> int:
    data = read_data(file_path)
    mean = int(statistics.mean(data))

    return int(
        min(
            [
                sum([fiel_consumption(abs(x - target_point)) for x in data])
                for target_point in [mean - 1, mean, mean + 1]
            ]
        )
    )
