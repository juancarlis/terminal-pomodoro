import logging
import time

import click

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def hide_cursor():
    click.echo('\033[?25l', nl=False)    


def show_cursor():
    click.echo('\033[?25h', nl=False)


def start_stopwatch(minutes: int=9999):

    hide_cursor()

    parsed_time: str = '00:00:00'

    try: 
        total_seconds = minutes * 60
        for second in range(0, total_seconds+1):

            m, s = divmod(second, 60)
            h, m = divmod(m, 60)

            parsed_time = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
            click.echo(f'\rTime: {parsed_time}', nl=False)
            time.sleep(1)
        click.echo('\nTiempo finalizado. ')
    except KeyboardInterrupt:
        click.echo(f'\nEl conteo finaliza en {parsed_time}')
    finally: 
        show_cursor()


if __name__ == '__main__':
    start_stopwatch()
