from pathlib import Path

import click

from mako.template import Template

from cli.options import days_option
from cli.helpers import get_day_folder, get_root, get_templates_folder, get_tests_folder


ROOT = 'aoc'
ROOT_DAYS = f'{ROOT}/days'
ROOT_TESTS = f'{ROOT}/tests'
ROOT_TESTS_DATA = f'{ROOT_TESTS}/artefacts'

FOLDERS = (ROOT, ROOT_DAYS, ROOT_TESTS, ROOT_TESTS_DATA)


@click.group()
def create_command():
    pass


@create_command.command()
@days_option
@click.option('--force', '-f', is_flag=True, default=False)
def create(day, force):
    """creates fordes and files for specified puzzle"""
    check_and_create_root()

    puzzle_folder = Path(get_day_folder(day))
    if not puzzle_folder.exists():
        puzzle_folder.mkdir()

    puzzle_data_folder = Path(get_day_folder(day)) / 'data'
    if not puzzle_data_folder.exists():
        puzzle_data_folder.mkdir()

    solution_file = Path(get_day_folder(day)) / "solution.py"
    create_file(
        solution_file, template_file=f"{get_templates_folder()}/solution.tpl",
        force=force, day_number=day
    )

    input_file = Path(get_day_folder(day)) / 'data' / "input.md"
    create_file(input_file)

    test_file = Path(get_tests_folder()) / f"test_day{day}.py"
    create_file(test_file, template_file=f"{get_templates_folder()}/test.tpl", day_number=day)

    test_data_file = Path(get_tests_folder()) / 'artefacts' / f"day{day}_test_data.md"
    create_file(test_data_file)


def check_and_create_root():
    root = get_root()
    for folder in FOLDERS:
        path = Path(root) / folder

        if not path.exists:
            path.mkdir()


def create_file(file_path: Path, force=False, template_file=None, **kwargs):
    if file_path.exists() and not force:
        print(f"{file_path} already exists. Skipping")
        return

    if not template_file:
        file_path.touch(exist_ok=not(force))
        return

    template_object = Template(filename=template_file)
    file_path.write_text(template_object.render(**kwargs))
