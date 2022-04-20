from pathlib import Path

import click
import pytest

from cli.helpers import get_tests_folder, process_input
from cli.options import days_option, part_option


@click.group()
def test_command():
    pass


@test_command.command()
@days_option
@part_option
def test(day, part):
    """Run tests"""
    days, parts = process_input(day, part)

    tests = ['-q', '--no-header', '--tb=no', '--show-capture=no']
    for day in days:
        path = Path(f"{get_tests_folder()}/test_day{day}.py")

        if not path.exists():
            print(f"Day {day} not found")
            continue

        if len(parts) == 1:
            path = f"{path}::test_part_{parts[0]}"
        tests.append(path)

    pytest.main(tests)
