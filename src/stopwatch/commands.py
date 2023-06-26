import click

from src.stopwatch.models import Stopwatch


@click.group()
def stopwatch():
    """Manages stopwatch."""
    pass


@stopwatch.command()
@click.option(
        '-l', 
        '--limit', 
        type=int, 
        prompt=False, 
        default=9999,
        required=False,
        help='Set a time limit'
        )
def start(limit):
    """Starts time tracking. """
    Stopwatch.start(minutes=limit)

all = stopwatch
