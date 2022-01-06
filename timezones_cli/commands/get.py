from collections import defaultdict
from datetime import datetime as dt
from zoneinfo import ZoneInfo, available_timezones

import click
from rich.console import Console

from timezones_cli.utils import get_local_time

console = Console()


@click.command()
@click.argument("query")
def get(query: str):
    now = dt.utcnow()
    tz_abbrev = lambda tz: ZoneInfo(tz).tzname(now)
    tz_map = defaultdict(list)

    for tz in available_timezones():
        tz_map[tz_abbrev(tz)].append(tz)
    tz_map = {k: sorted(v) for k, v in tz_map.items()}

    try:
        data = tz_map[query.upper()]
        get_local_time([data[0]])
    except KeyError:
        console.print(
            f"[bold red]:x: Could not find datetime for query: [green]{query}[/green][/bold red]"
        )
