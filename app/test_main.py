from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize("all_products, today, outdated", [
    ([{
        "name": "salmon",
        "expiration_date": (2022, 2, 10),
        "price": 600
    }, {
        "name": "chicken",
        "expiration_date": (2022, 2, 5),
        "price": 120
    }, {
        "name": "duck",
        "expiration_date": (2022, 2, 1),
        "price": 160
    }], (2022, 2, 2), ["duck"]),
    ([{
        "name": "milk",
        "expiration_date": (2022, 3, 10),
        "price": 80
    }, {
        "name": "bread",
        "expiration_date": (2022, 2, 28),
        "price": 60
    }], (2022, 2, 2), []),
    ([{
        "name": "yogurt",
        "expiration_date": (2022, 1, 15),
        "price": 40
    }, {
        "name": "cheese",
        "expiration_date": (2022, 1, 20),
        "price": 90
    }, {
        "name": "cream",
        "expiration_date": (2022, 1, 30),
        "price": 50
    }], (2022, 2, 2), ["yogurt", "cheese", "cream"]
    )])
@mock.patch("app.main.datetime.date")
def test_outdated_products(
    mock_datetime: mock.MagicMock,
    all_products: list,
    today: tuple,
    outdated: list
) -> None:
    for product in all_products:
        mock_datetime.date.return_value = product["expiration_date"]
    mock_datetime.today.return_value = today
    assert outdated_products(all_products) == outdated
