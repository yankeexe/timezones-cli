import typing as t

import click
import pycountry

from timezones_cli.utils import (
    console,
    extract_fuzzy_country_data,
    get_local_time,
    get_timezones,
    handle_interaction,
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
        # Search with user query.
        # @TODO: Handle list with multiple data.
        data: t.List = pycountry.countries.search_fuzzy(query)

        # extract alpha2 value
        _, _, alpha_2, _ = extract_fuzzy_country_data(data)

        # Get a list of timezone names.
        result = get_timezones(alpha_2)

        payload: t.List = []

        # If length is greater than one, show terminal menu.
        if len(result) > 1:
            entry = handle_interaction(result)

            payload.append(entry)
            return get_local_time(payload, toggle=toggle)
    except LookupError:
        return console.print(
            "Couldn't resolve your query, please try other keywords.:x:"
        )

    return get_local_time(result, toggle=toggle)
