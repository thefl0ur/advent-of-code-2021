import os

import pytest

from aoc.days.day11.solution import part1, part2


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day11_test_data.md', 1656)]
)
def test_part_1(input, expected):
    result = part1(input)
    assert result == expected


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day11_test_data.md', 195)]
)
def test_part_2(input, expected):
    result = part2(input)
    assert result == expected
