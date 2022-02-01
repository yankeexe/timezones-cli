"""
Sub command to add timezones for quick glance.
"""

from typing import List

import click

from timezones_cli.utils import (
    check_config,
    console,
    handle_interaction,
    query_handler,
    variables,
)


@click.command()
@click.argument("query")
def add(query: str):
    """
    Add timezone to the config file.
    """
    added_timezones = []
    existing_timezones = []
    line_break = "\n"
    timezones = query_handler(query)

    if len(timezones) > 1:
        timezones = handle_interaction(timezones)

    config_file = variables.config_file

    if not check_config():
        with open(config_file, "w+"):
            pass

    with open(config_file, "r+") as file:
        data: List = [line.rstrip() for line in file]

        for timezone in timezones:
            if timezone in data:
                existing_timezones.append(f"[bold red]{timezone}:x:[/bold red]")
                continue

            file.read()
            # Add to the end of the file.
            file.write(f"{timezone}\n")
            added_timezones.append(
                f"[bold blue]{timezone}[/bold blue] :white_check_mark:"
            )

    if existing_timezones:
        console.print(
            f"[bold yellow]Timezone/s already exists:[/bold yellow]\n{line_break.join(existing_timezones)}"
        )

    if added_timezones:
        console.print(
            f"[bold green]New timezone/s added successfully:[/bold green]\n{line_break.join(added_timezones)}"
        )
