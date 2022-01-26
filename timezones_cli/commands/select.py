"""
Sub command to select timezone from config file.
"""
import click

from timezones_cli.utils import console, get_local_time, handle_interaction, variables


@click.command()
@click.option(
    "--toggle",
    "-t",
    help="Toggle for 24 hours format",
    type=bool,
    default=False,
    is_flag=True,
)
def select(toggle: bool):
    """
    Interactively select the timezone from your config file to get local time.

    $ tz select
    """
    config_file = variables.config_file
    entry = []

    with open(config_file, "r+") as file:
        data = [line.rstrip() for line in file]

        if not len(data):
            return console.print("Config file contains no timezone:x:")

        entry.append(handle_interaction(data))

        return get_local_time(entry, toggle=toggle)
