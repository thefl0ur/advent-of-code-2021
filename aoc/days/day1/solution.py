from aoc.days.day1.helpers import read_data
from aoc.days.day1.sonar_sweep import SonarSweep


def part1(input_data: str) -> int:
    sonar = SonarSweep(read_data(input_data), 1)
    return sonar.get_increments_count()


def part2(input_data: str) -> int:
    sonar = SonarSweep(read_data(input_data), 3)
    return sonar.get_increments_count()
