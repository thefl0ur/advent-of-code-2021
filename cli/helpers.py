import os

ALL_DAYS = [d for d in range(1, 26)]
ALL_PARTS = [p for p in range(1, 3)]


def process_input(day, part):
    if not day and not part:
        day = ALL_DAYS
        part = ALL_PARTS

    if not part:
        part = ALL_PARTS

    if isinstance(day, int):
        day = [day]

    if isinstance(part, int):
        part = [part]

    return (day, part)


def get_day_folder(date):
    return f"{os.getcwd()}/aoc/days/day{date}"


def get_tests_folder():
    return f"{os.getcwd()}/aoc/tests"


def get_templates_folder():
    return f"{os.getcwd()}/cli/templates"


def get_root():
    return os.getcwd()
