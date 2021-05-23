"""
Sub command to select timezone from config file.
"""
import click
from timezones_cli.utils import variables
from timezones_cli.utils import console, handle_interaction, get_local_time


@click.command()
def select():
    """
    Interactively select the timezone from your config file to get local time.
    """
    config_file = variables.config_file
    entry = []

    with open(config_file, "r+") as file:
        data = [line.rstrip() for line in file]

        if not len(data):
            return console.print("Config file contains no timezone:x:")

        entry.append(handle_interaction(data))

        return get_local_time(entry)
