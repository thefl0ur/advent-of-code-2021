import os

import pytest

from aoc.days.day12.solution import part1, part2


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day12_test_data.md', 10)]
)
def test_part_1(input, expected):
    result = part1(input)
    assert result == expected


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day12_test_data.md', 36)]
)
def test_part_2(input, expected):
    result = part2(input)
    assert result == expected
