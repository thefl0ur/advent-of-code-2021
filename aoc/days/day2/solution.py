from aoc.days.day2.helpers import read_data
from aoc.days.day2.dive import Dive, DiveAim


def part1(input_data: str) -> int:
    dive = Dive(read_data(input_data))
    return dive.calculcate_position()


def part2(input_data: str) -> int:
    dive = DiveAim(read_data(input_data))
    return dive.calculcate_position()
