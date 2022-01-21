""" pytest fixtures """
from collections import namedtuple

import pytest


@pytest.fixture(scope="function")
def country_data():
    Country = namedtuple(
        "Country", ["alpha_2", "alpha_3", "name", "numeric", "official_name"]
    )

    return [
        Country(
            alpha_2="NP",
            alpha_3="NPL",
            name="Nepal",
            numeric="524",
            official_name="Federal Democratic Republic of Nepal",
        )
    ]
