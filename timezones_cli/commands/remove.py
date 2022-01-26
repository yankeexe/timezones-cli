"""
Sub command to remove saved timezones from config file.
"""
from typing import Optional

import click

from timezones_cli.utils import (
    console,
    print_help_msg,
    remove_timezone,
    validate_timezone,
)


@click.command()
@click.option("--name", "-n", help="Name of the timezone", type=str)
@click.option(
    "--interactive",
    "-i",
    help="Delete timezones in interactive mode.",
    is_flag=True,
)
def remove(name: Optional[str], interactive: bool):
    """
    Remove timezone to the config file.

    $ tz remove "Asia/Kolkata"

    $ tz remove -i
    """
    exists = interactive or name

    if not exists:
        return print_help_msg(remove)

    if name and interactive:
        return console.print("Cannot use both flags at the same time.:x:")

    if name:
        validate_timezone(name)

    remove_timezone(interactive, name)
