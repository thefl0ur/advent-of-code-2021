import os

import pytest

from aoc.days.day9.solution import part1, part2


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day9_test_data.md', 15)]
)
def test_part_1(input, expected):
    result = part1(input)
    assert result == expected


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day9_test_data.md', 1134)]
)
def test_part_2(input, expected):
    result = part2(input)
    assert result == expected
