"""
Sub command to get UTC times
"""
import sys

import click

from timezones_cli.utils import (
    console,
    get_local_utc_time,
    get_utc_time,
    validate_time,
    validate_timezone,
)


@click.command()
@click.argument("time", required=False)
@click.argument("timezone", required=False)
def utc(time, timezone):
    """
    Convert a specific time from any timezone to UTC.

    > Hours are calculated in 24 hours format. You can specify 'AM' or 'PM' if you are using 12 hours format.

    EXAMPLE: \n

    $ tz utc # show current system time in UTC.

    $ tz utc "8:15" "Asia/Kathmandu" # will be evaluated as AM, following the 24 hour format.

    $ tz utc "20:15" "Asia/Kathmandu" # will be evaluated as PM despite any suffix, following the 24 hour format.

    $ tz utc "8:15 PM" "Asia/Kathmandu" # will be evaluated as specified.
    """
    if not time or not timezone:
        get_local_utc_time()

    try:
        validate_timezone(timezone)
        hour, minute, time_suffix = validate_time(time)
    except Exception:
        console.print("[bold red]:x:Invalid input value[/bold red]")
        sys.exit(0)

    time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)} {time_suffix}"

    return get_utc_time(hour, minute, timezone, time)
