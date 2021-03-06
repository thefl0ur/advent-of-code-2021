import click

from cli.commands.run_command import run_command
from cli.commands.perfomance_command import perfomance_command
from cli.commands.profile_command import profile_command
from cli.commands.test_command import test_command
from cli.commands.create_command import create_command

cli = click.CommandCollection(sources=[run_command, perfomance_command, profile_command, test_command, create_command])

if __name__ == '__main__':
    cli()
