import importlib
import os

from pathlib import Path
from typing import List

from cli.helpers import get_day_folder


class ImportError(Exception):
    def __init__(self, reason: str):
        self.reason = reason


def import_puzzles(days: List[int]):
    out = dict()
    for day in days:
        module = None
        puzzle_input = None
        out[day] = {}
        try:
            module, puzzle_input = import_puzzle(day)
        except ImportError as exc:
            out[day]["error"] = exc.reason

        out[day]["module"] = module
        out[day]["input"] = puzzle_input

    return out


def import_puzzle(day_number: int):
    module = None
    try:
        module = importlib.import_module(f"aoc.days.day{day_number}.solution")
    except ModuleNotFoundError:
        raise ImportError(reason="No module found")

    if not hasattr(module, f"part1") and not hasattr(module, f"part2"):
        raise ImportError(reason="No solutions found")

    puzzle_input_path = f"{get_day_folder(day_number)}/data/input.md"
    puzzle_input_file = Path(puzzle_input_path)
    if not puzzle_input_file.exists():
        raise ImportError(reason="No input data found")

    return (module, puzzle_input_path)
