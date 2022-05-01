from typing import List


def read_data(file_name: str) -> List[int]:
    with open(file_name, 'r') as file:
        return list(map(int, file.readline().split(',')))


def calc(file_path: str, days: int) -> int:
    data = [0 for _ in range(9)]

    for init_data in read_data(file_path):
        data[init_data] += 1

    for _ in range(days):
        newborn = 0
        aged = 0
        for index, _ in enumerate(data):
            if index == 0:
                newborn = data[index]
                aged += data[index]
            else:
                data[index-1] = data[index]
            data[index] = 0

        data[6] += aged
        data[8] = newborn

    return sum(data)


def part1(file_path: str) -> int:
    return calc(file_path, days=80)


def part2(file_path: str) -> int:
    return calc(file_path, days=256)
