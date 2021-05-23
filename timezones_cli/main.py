""" Entrypoint of the CLI """
import click
from timezones_cli.commands import utc, show, add, search, remove, select


@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(utc)
cli.add_command(show)
cli.add_command(search)
cli.add_command(remove)
cli.add_command(select)
