from datetime import timedelta
from typing import List

import click
import yappi

from cli.importer import import_puzzles
from cli.helpers import process_input
from cli.options import days_option, part_option


@click.group()
def profile_command():
    pass


@profile_command.command()
@days_option
@part_option
def profile(day, part):
    """Run yappi profiler"""
    days, parts = process_input(day, part)
    puzzles = import_puzzles(days)

    for day, data in puzzles.items():
        if "error" in data:
            print(f"error: {data['error']}")
            continue

        for part in parts:
            current_part = f"part{part}"
            if not hasattr(data["module"], current_part):
                print(f"no {current_part} found")
                continue

            func = getattr(data["module"], current_part)
            yappi.start()
            func(data['input'])
            yappi.stop()
            yappi.get_func_stats(
                filter_callback=lambda x: 'aoc' in x.module).print_all()
            yappi.clear_stats()
