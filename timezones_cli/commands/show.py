"""
Sub command to show datetime from saved timezones.
"""
import sys
from typing import Union, List

import click
from timezones_cli.utils import (
    console,
    get_system_time,
    get_local_time,
    check_config as check_configuration,
)


@click.command()
def show():
    """
    Show time based on the defaults at .tz-cli file.
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

    return get_local_time(check_config)
