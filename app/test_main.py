import pytest
from unittest import mock
from app.main import outdated_products
from datetime import date


@pytest.fixture(scope="module")
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize("today_date, result", [
    ((2022, 2, 15), ["salmon", "chicken", "duck"]),
    ((2022, 2, 6), ["chicken", "duck"]),
    ((2022, 2, 4), ["duck"]),
    ((2022, 2, 1), []),
    ((2022, 1, 25), [])
])
def test_outdated_products(
        products: list,
        today_date: tuple,
        result: list
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(*today_date)

        assert outdated_products(products) == result
