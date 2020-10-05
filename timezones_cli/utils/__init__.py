""" Utils for sub commands """
import os
import sys
from datetime import datetime
from typing import List, NamedTuple, Optional, Tuple, Union

import pytz
import click
import pycountry
from tabulate import tabulate
from rich.console import Console
from simple_term_menu import TerminalMenu

from timezones_cli.utils import variables

console = Console()


def check_config() -> Union[List, bool]:
    """
    Check for GitHub credential in config file.
    Return if exists.
    """
    config_file: str = variables.config_file

    if os.path.exists(config_file):
        with open(config_file) as file:
            # Remove new line character "\n"
            return [line.rstrip() for line in file]

    return False


def remove_timezone(interactive: bool, name: Optional[str] = None):
    """
    Remove timezones based on the argument.
    """
    config_file: str = variables.config_file
    entry: Optional[str]

    if not check_config():
        console.print(
            "No configuration file found in your system.:x:\n", style="bold red"
        )
        console.print(
            "Use `tz add` to create and add timezone to your config file.:memo:",
            style="bold green",
        )
        sys.exit()

    with open(config_file, "r+") as file:
        data: List = [line.rstrip() for line in file]

        if not len(data):
            console.print("Config file contains no timezone:x:", style="bold red")
            sys.exit()

        if interactive:
            entry = handle_interaction(data)
        else:
            entry = name

        # Check timezone existence in non-interactive mode.
        if entry not in data:
            console.print(
                f"Timezone not found in your config file.:x:", style="bold red"
            )
            sys.exit()

        # Clear file content.
        file.seek(0)
        file.truncate(0)

        for line in data:
            if not line == entry:
                file.write(f"{line}\n")

        console.print(
            f"[bold green]Timezone removed:[bold green] [bold blue]{entry}[/bold blue] :white_check_mark:"
        )


def handle_interaction(data: List) -> str:
    """
    Display interactive menu on the terminal.
    """
    try:
        terminal_menu = TerminalMenu(data)
        menu_entry_index: Optional[int] = terminal_menu.show()

        # Check for None value when user presses `esc` or `ctrl + c`
        if menu_entry_index is None:
            raise KeyboardInterrupt

    except KeyboardInterrupt:
        console.print("Exit:x:")
        sys.exit()

    return data[menu_entry_index]


def extract_fuzzy_country_data(fuzzy_result: List) -> Tuple[str, str, str, str]:
    """
    Extract data from the Named tuple returned by
    fuzzy searching.
    """
    country_data: NamedTuple = fuzzy_result[0]

    name: str = getattr(country_data, "name", None)
    alpha_2: str = getattr(country_data, "alpha_2", None)
    alpha_3: str = getattr(country_data, "alpha_3", None)
    official_name: str = getattr(country_data, "official_name", None)

    return name, official_name, alpha_2, alpha_3


def get_local_time(timezones: List):
    """
    Get localtime based on passed timezones.
    """
    headers: List = ["Timezone", "Local Date time"]
    rows: List = []
    for zone in timezones:
        validate_timezone(zone)
        timezone = pytz.timezone(zone)
        time_data = datetime.now(timezone)
        rows.append((zone, time_data.strftime("%B %Y %A %I:%M:%S %p")))

    console.print(tabulate(rows, headers, tablefmt="fancy_grid"))


def get_system_time():
    """
    System date and time.
    """
    time = datetime.now()
    return time.strftime(("%B %Y %A %I:%M:%S"))


def get_timezones(country_code: str) -> List:
    """
    Return timezones based on the country code provided.
    """
    len_country_code: int = len(country_code)

    if len_country_code not in (2, 3):
        console.print("Invalid country code:x:", style="bold red")
        sys.exit()

    if len_country_code == 2:
        data = pycountry.countries.get(alpha_2=country_code)
    else:
        data = pycountry.countries.get(alpha_3=country_code)

    if not data:
        console.print("Invalid country code.:x:", style="bold red")
        sys.exit()

    return pytz.country_timezones[country_code]


def validate_timezone(timezone: str) -> bool:
    """
    Validate timezone passed.
    """
    try:
        pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        console.print(
            f"[bold green]Invalid timezone name:[/bold green] [bold red]{timezone}:x:[/bold red]"
        )
        sys.exit()

    return True


def print_help_msg(command):
    """
    Get help message.
    """
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))
