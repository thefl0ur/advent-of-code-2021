import csv
import statistics
import timeit
import tracemalloc

from datetime import timedelta
from typing import List

import click
from tabulate import tabulate

from cli.importer import import_puzzles
from cli.helpers import process_input
from cli.options import days_option, part_option


@click.group()
def perfomance_command():
    pass


@perfomance_command.command()
@days_option
@part_option
@click.option(
    '--count', '-c', type=int, default=5, help='Count of reruns for solution')
@click.option('--save', '-s', is_flag=True, default=False)
def perfomance(day, part, count, save):
    """Run perfomance test on puzzle to find out memory and time consumption"""
    days, parts = process_input(day, part)
    puzzles = import_puzzles(days)

    output_data = []

    headers = ['DAY']
    for day_part in parts:
        headers.append(f'MEM {day_part}, Kb')
        headers.append(f'TIME {day_part}')

    steps = len(days)*len(parts) * count * 2
    with click.progressbar(
        length=steps,  label='Running perfomance test', item_show_func=lambda info: info
    ) as bar:
        for day, data in puzzles.items():
            day_stat = [day]

            if "error" in data:
                bar.update(len(parts) * count, f"Day {day}")
                for day_part in parts:
                    day_stat.append('-')
                    day_stat.append('-')
                output_data.append(day_stat)
                continue

            for part in parts:
                current_part = f"part{part}"
                if not hasattr(data["module"], current_part):
                    day_stat.append('-')
                    day_stat.append('-')
                    bar.update(count, f"Day {day} part {part}")
                    continue

                func = getattr(data["module"], current_part)

                execution_time = []
                memory_peaks = []
                for x in range(count):
                    start = timeit.default_timer()
                    func(data['input'])
                    end = timeit.default_timer()
                    execution_time.append(end-start)
                    bar.update(1, f"Day {day} part {part} - Time test")

                for x in range(count):
                    tracemalloc.start()
                    func(data['input'])
                    _, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    memory_peaks.append(peak)
                    bar.update(1, f"Day {day} part {part} - Memory test")

                day_stat.append(statistics.mean(memory_peaks)/(10**3))
                day_stat.append(timedelta(seconds=statistics.mean(execution_time)))

            output_data.append(day_stat)
        bar.update(1, f"Finished")

    print(tabulate(output_data, headers=headers, tablefmt="github"))

    if not save:
        return

    with open('aoc_stat.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(output_data)
