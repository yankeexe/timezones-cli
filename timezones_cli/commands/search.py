from typing import List

import click
import pycountry

from timezones_cli.utils import (
    extract_fuzzy_country_data,
    get_timezones,
    handle_interaction,
    get_local_time,
    console,
)


@click.command()
@click.argument("query")
def search(query: str):
    """
    Get time based on the entered timezone.
    """
    try:
        # Search with user query.
        # @TODO: Handle list with multiple data.
        data: List = pycountry.countries.search_fuzzy(query)

        # extract alpha2 value
        _, _, alpha_2, _ = extract_fuzzy_country_data(data)

        # Get a list of timezone names.
        result = get_timezones(alpha_2)

        payload: List = []

        # If length is greater than one, show terminal menu.
        if len(result) > 1:
            entry = handle_interaction(result)

            payload.append(entry)

            return get_local_time(payload)
    except LookupError:
        return console.print(
            "Couldn't resolve your query, please try other keywords.:x:"
        )

    return get_local_time(result)
