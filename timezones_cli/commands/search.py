import typing as t

import click

from timezones_cli.utils import (
    console,
    get_local_time,
    handle_interaction,
    query_handler,
)


@click.command()
@click.argument("query")
@click.option(
    "--toggle",
    "-t",
    help="Toggle for 24 hours format",
    type=bool,
    default=False,
    is_flag=True,
)
def search(query: str, toggle: bool):
    """
    Get time based on the entered timezone.

    $ tz search US

    $ tz search Africa
    """
    try:
        result = query_handler(query)

        # If length is greater than one, show terminal menu.
        if isinstance(result, t.List) and len(result) > 1:
            entries = handle_interaction(result)

            return get_local_time(entries, toggle=toggle)
    except LookupError:
        return console.print(
            "Couldn't resolve your query, please try other keywords.:x:"
        )

    return get_local_time(result, toggle=toggle)
