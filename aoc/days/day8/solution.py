from typing import List


def read(path) -> List[str]:
    data = []
    with open(path) as f:
        for line in f:
            data.append(line.rstrip())
    return data


def part1(file_path: str) -> int:
    return sum(
        sum(
            [
                1 if len(x) in [3, 4, 2, 7] else 0
                for x in [x.strip() for x in line.split('|')[1].strip().split(' ')]
            ]
        )
        for line in read(file_path)
    )


def part2(file_path: str) -> int:
    raise NotImplemented('No code for day8 part 2')
