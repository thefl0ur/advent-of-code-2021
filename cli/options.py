import click

days_option = click.option(
    '-d', '--day', type=click.IntRange(1, 25), help='Run solution for specified day')

part_option = click.option(
    '-p', '--part', type=click.IntRange(1, 2), help='Run solution for specified part of puzzle')
