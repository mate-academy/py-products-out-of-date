import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
    yield [
        {
            "name": "salmon",
            "expiration_date": None,
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 10, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 10, 10),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "expiration_dates, expected_result",
    [
        pytest.param(
            [datetime.date(2022, 10, 10)], [],
            id="No outdated products"
        ),
        pytest.param(
            [datetime.date(2022, 10, 6)], [],
            id="expiration date == today"
        ),
        pytest.param(
            [datetime.date(2022, 10, 5)], ["salmon"],
            id="One product is outdated"
        ),
        pytest.param(
            [datetime.date(2022, 10, 5),
             datetime.date(2022, 10, 5),
             datetime.date(2022, 10, 5)],
            ["salmon", "chicken", "duck"],
            id="All product is outdated"
        )
    ]

)
def test_outdated_products(
        mock_today: callable,
        products: list[dict],
        expiration_dates: list[object],
        expected_result: list[str]
) -> None:

    mock_today.date.today.return_value = datetime.date(2022, 10, 6)
    for i, date in enumerate(expiration_dates):
        products[i]["expiration_date"] = date

    assert outdated_products(products) == expected_result
