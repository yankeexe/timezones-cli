"""
Sub command to show datetime from saved timezones.
"""
import sys
from typing import List, Union

import click

from timezones_cli.utils import check_config as check_configuration
from timezones_cli.utils import console, get_local_time, get_system_time


@click.command()
@click.option(
    "--toggle",
    "-t",
    help="Toggle for 24 hours format",
    type=bool,
    default=False,
    is_flag=True,
)
def show(toggle: bool):
    """
    Show time based on the defaults at .tz-cli file.

    $ tz show
    """
    check_config: Union[List, bool] = check_configuration()

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
            f"Your system datetime is: {get_system_time()}",
            style="bold yellow",
        )
        sys.exit()

    return get_local_time(check_config, toggle=toggle)
