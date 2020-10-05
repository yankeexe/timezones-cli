""" Tests for utils """
import pytest

from timezones_cli import utils
from tests.fixtures import country_data


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
    assert utils.validate_timezone("Asia/Kathmandu") == True
    assert utils.validate_timezone("Asia/Kolkata") == True


def test_validate_timezone_failure():
    """
    Tests for invalid timezones.
    """
    with pytest.raises(SystemExit):
        assert utils.validate_timezone("Python/Tests")
        assert utils.validate_timezone("Asia/Catmandu")
