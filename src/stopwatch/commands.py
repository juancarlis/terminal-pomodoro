import click

from src.stopwatch.models import Stopwatch


@click.group(invoke_without_command=True)
@click.pass_context
def stopwatch(ctx):
    """Manages stopwatch."""
    if ctx.invoked_subcommand is None:
        ctx.invoke(start)


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
