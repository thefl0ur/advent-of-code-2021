import importlib

import click

from cli.importer import import_puzzles
from cli.helpers import process_input
from cli.options import days_option, part_option


@click.group()
def run_command():
    pass


@run_command.command()
@days_option
@part_option
def run(day, part):
    """Runs a solution of Advent of Code puzzles"""
    days, parts = process_input(day, part)
    puzzles = import_puzzles(days)

    for day, data in puzzles.items():
        print(f"Day {day}")
        if "error" in data:
            print(f"Error: {data['error']}")
            continue

        for part in parts:
            current_part = f"part{part}"
            if not hasattr(data["module"], current_part):
                print(f"no {current_part} found")
                continue

            func = getattr(data["module"], current_part)
            result = func(data['input'])
            print(f"Part {part}: {result}")
