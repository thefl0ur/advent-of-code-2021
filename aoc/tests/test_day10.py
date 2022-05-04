import os

import pytest

from aoc.days.day10.solution import part1, part2


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day10_test_data.md', 26397)]
)
def test_part_1(input, expected):
    result = part1(input)
    assert result == expected


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day10_test_data.md', 288957)]
)
def test_part_2(input, expected):
    result = part2(input)
    assert result == expected
