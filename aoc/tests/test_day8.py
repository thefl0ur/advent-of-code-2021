import os

import pytest

from aoc.days.day8.solution import part1, part2


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day8_test_data.md', 26)]
)
def test_part_1(input, expected):
    result = part1(input)
    assert result == expected


@pytest.mark.parametrize(
    ['input', 'expected'], [(f'{os.getcwd()}/aoc/tests/artefacts/day8_test_data.md', 61229)]
)
def test_part_2(input, expected):
    result = part2(input)
    assert result == expected
