import time
import click


class Stopwatch:
    
    @staticmethod
    def _hide_cursor():
        click.echo('\033[?25l', nl=False)    

    @staticmethod
    def _show_cursor():
        click.echo('\033[?25h', nl=False)
    
    @staticmethod
    def start(minutes: int=9999):

        Stopwatch._hide_cursor()
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
            Stopwatch._show_cursor()
