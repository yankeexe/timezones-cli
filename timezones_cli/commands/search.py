import typing as t

import click

from timezones_cli.utils import (
    console,
    get_local_time,
    handle_interaction,
    query_handler,
    tz_abbreviation_handler,
)
from timezones_cli.utils.validators import TzAbbrev


@click.command()
@click.argument("query", type=TzAbbrev())
@click.option(
    "--zone",
    "-z",
    help="define timezone short codes",
    is_flag=True,
)
@click.option(
    "--toggle",
    "-t",
    help="Toggle for 24 hours format",
    is_flag=True,
)
def search(query: str, zone: bool, toggle: bool):
    """
    Get time based on the entered timezone or country code

    - using country code (either 2 or 3 letters):

        $ tz search US

        $ tz search USA

    - using timezone:

        $ tz search Asia/Kathmandu

    - using fuzzy text: (example: Ireland)

        $ tz search Irela

    - using timezone shortcodes (--zone or -z flag):

        $ tz search pst -z

        $ tz search ist -z

        $ tz search jst -z

        $ tz search cest -z

        $ tz search +0545 -z

        $ tz search +05 -z
    """
    try:
        if zone:
            result = tz_abbreviation_handler(query)
        else:
            result = query_handler(query)

            # If length is greater than one, show terminal menu.
            if isinstance(result, t.List) and len(result) > 1:
                result = handle_interaction(result)

        return get_local_time(result, query, toggle=toggle)
    except LookupError:
        return console.print(
            "Couldn't resolve your query, please try other keywords.:x:"
        )
