""" Entrypoint of the CLI """
import sys

from typing import List, Optional, Union

import click
import pycountry
from rich.console import Console

from timezones_cli import utils
from timezones_cli.utils import variables


console = Console()


@click.group()
def cli():
    pass


@cli.command()
def show():
    """
    Show time based on the defaults at .tz-cli file.
    """
    check_config: Union[List, bool] = utils.check_config()

    if not check_config:
        console.print(
            "File is empty or No configuration file is present in your system.:x:\n",
            style="bold red",
        )
        console.print(
            "Use `tz add` to create and add timezone to your config file.:memo:\n",
            style="bold green",
        )

        console.print(
            f"Your system datetime is: {utils.get_system_time()}",
            style="bold yellow",
        )
        sys.exit()

    return utils.get_local_time(check_config)


@cli.command()
@click.argument("query")
def search(query: str):
    """
    Get time based on the entered timezone.
    """
    try:
        # Search with user query.
        # TODO: Handle list with multiple data.
        data: List = pycountry.countries.search_fuzzy(query)

        # extract alpha2 value
        _, _, alpha_2, _ = utils.extract_fuzzy_country_data(data)

        # Get a list of timezone names.
        result = utils.get_timezones(alpha_2)

        payload: List = []

        # If length is greater than one, show terminal menu.
        if len(result) > 1:
            entry = utils.handle_interaction(result)

            payload.append(entry)

            return utils.get_local_time(payload)
    except LookupError:
        return console.print(
            "Couldn't resolve your query, please try other keywords.:x:"
        )

    return utils.get_local_time(result)


@cli.command()
@click.argument("timezone")
def add(timezone: str):
    """
    Add timezone to the config file.
    """
    utils.validate_timezone(timezone)
    config_file = variables.config_file

    if not utils.check_config():
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


@cli.command()
@click.option("--name", "-n", help="Name of the timezone", type=str)
@click.option(
    "--interactive", "-i", help="Delete timezones in interactive mode.", is_flag=True
)
def remove(name: Optional[str], interactive: bool):
    """
    Remove timezone to the config file.
    """
    exists = interactive or name

    if not exists:
        return utils.print_help_msg(remove)

    if name and interactive:
        return console.print("Cannot use both flags at the same time.:x:")

    if name:
        utils.validate_timezone(name)

    utils.remove_timezone(interactive, name)


@cli.command()
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

        entry.append(utils.handle_interaction(data))

        return utils.get_local_time(entry)
