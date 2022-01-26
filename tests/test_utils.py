""" Tests for utils """
from unittest.mock import patch

import pytest
import pytz
from freezegun import freeze_time
from tabulate import tabulate

from timezones_cli import utils


@pytest.mark.usefixtures("country_data")
def test_extract_fuzzy_country_data(country_data):
    """
    Test the extraction of data returned by fuzzy search.
    """

    assert utils.extract_fuzzy_country_data(country_data) == (
        "Nepal",
        "Federal Democratic Republic of Nepal",
        "NP",
        "NPL",
    )


def test_get_timezones():
    """
    Test the timezone names returned with search query.
    """
    assert utils.get_timezones("np") == ["Asia/Kathmandu"]
    assert utils.get_timezones("in") == ["Asia/Kolkata"]


def test_get_timezones_failure():
    """
    Test for system exit when bad search query is provided.
    """
    with pytest.raises(SystemExit):
        assert utils.get_timezones("fail")

    with pytest.raises(SystemExit):
        assert utils.get_timezones("xz")


def test_validate_timezone():
    """
    Tests for valid timezone.
    """
    assert utils.validate_timezone("Asia/Kathmandu") is True
    assert utils.validate_timezone("Asia/Kolkata") is True


def test_validate_timezone_failure():
    """
    Tests for invalid timezones.
    """
    with pytest.raises(SystemExit):
        assert utils.validate_timezone("Python/Tests")
        assert utils.validate_timezone("Asia/Catmandu")


class TestMatchFuzzy:
    def test_match_fuzzy_match(self):
        query = "Europe"
        result = utils.match_fuzzy(query)
        assert result is not None

    def test_match_fuzzy_no_match(self):
        query = "Nepal"
        from timezones_cli.utils import match_fuzzy

        result = match_fuzzy(query)
        assert len(result) == 0


class TestQueryHandler:
    def test_query_handler_use_fuzzy_match(self):
        query = "Africa"
        result = utils.query_handler(query)
        assert "Africa/Asmara" in result

    def test_query_handler_user_fuzzy_search(self):
        query = "np"
        result = utils.query_handler(query)
        assert result == ["Asia/Kathmandu"]


@patch("timezones_cli.utils.console")
@patch("timezones_cli.utils.tzlocal.get_localzone", autospec=True)
def test_get_local_utc_time(mock_localzone, mock_console):
    headers = ["Time Zone", "Local Time", "UTC Time"]
    mock_localzone.return_value = pytz.timezone("Asia/Kathmandu")

    with freeze_time("2022-01-26 07:18:30"):
        utils.get_local_utc_time()

        mock_console.print.assert_called_once_with(
            tabulate(
                [("Asia/Kathmandu", "07:18 AM", "07:18 AM")],
                headers,
                tablefmt="fancy_grid",
            )
        )
