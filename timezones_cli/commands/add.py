"""
Sub command to add timezones for quick glance.
"""

from typing import List

import click

from timezones_cli.utils import check_config, console, validate_timezone, variables


@click.command()
@click.argument("timezone")
def add(timezone: str):
    """
    Add timezone to the config file.
    """
    validate_timezone(timezone)
    config_file = variables.config_file

    if not check_config():
        with open(config_file, "w+") as newfile:
            pass

    with open(config_file, "r+") as file:
        data: List = [line.rstrip() for line in file]

        if timezone in data:
            return console.print(
                f"[bold green]Timezone already exists:[/bold green] [bold red]{timezone}:x:[/bold red]"
            )

        # Read file
        file.read()

        # Add to the end of the file.
        file.write(f"{timezone}\n")
        console.print(
            f"[bold green]New timezone added successfully:[/bold green] [bold blue]{timezone}[/bold blue] :white_check_mark:"
        )
