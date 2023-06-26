import click

from src.stopwatch import commands as stopwatch_commands


@click.group()
def cli():
    pass


cli.add_command(stopwatch_commands.all)
