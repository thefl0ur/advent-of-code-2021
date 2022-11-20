from collections import defaultdict, Counter
from typing import DefaultDict, Dict, Tuple

Pair = DefaultDict[str, int]
InsertionRule = Dict[str, str]


def read_data(filename) -> Tuple[str, InsertionRule]:
    file = open(filename, 'r')
    template = file.__next__().strip()
    file.__next__()
    replacements = dict([(line[0:2], line[6]) for line in file])
    file.close()

    return (template, replacements)


def generate(pairs: Pair, rules: InsertionRule, cntr: Counter) -> Tuple[Pair, Counter]:
    result = defaultdict(int)

    for pair, num in pairs.items():
        new_element = rules[pair]
        cntr[new_element] += num

        result[f'{pair[0]}{new_element}'] += num
        result[f'{new_element}{pair[1]}'] += num

    return result, cntr


def solution(file_path: str, repeats: int) -> int:
    base_template, replacements = read_data(file_path)
    pairs = defaultdict(int)
    index = 0
    while index < len(base_template) - 1:
        pairs[base_template[index: index + 2]] = 1
        index += 1

    cntr = Counter(base_template)

    for _ in range(repeats):
        pairs, cntr = generate(pairs, replacements, cntr)

    items = cntr.most_common()
    return items[0][1] - items[-1][1]


def part1(file_path: str) -> int:
    return solution(file_path, 10)


def part2(file_path: str) -> int:
    return solution(file_path, 40)
