""" Entrypoint of the CLI """
import click

from timezones_cli.commands import add, get, remove, search, select, show, utc


@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(get)
cli.add_command(remove)
cli.add_command(search)
cli.add_command(select)
cli.add_command(show)
cli.add_command(utc)
