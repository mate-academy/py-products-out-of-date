import pytest
from datetime import date
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
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


@pytest.mark.parametrize("today, result",
                         [
                             (date(2022, 1, 2), []),
                             (date(2022, 2, 1), []),
                             (date(2022, 2, 2), ["duck"]),
                             (date(2022, 2, 6), ["chicken", "duck"]),
                             (date(2022, 3, 1), ["salmon", "chicken", "duck"])
                         ],
                         ids=[
                             "all products are ok",
                             "Product date equals today is not outdated",
                             "duck is outdated",
                             "chicken and duck are outdated",
                             "all products are outdated"
                         ])
@mock.patch("datetime.date")
def test_outdated(mocked_date: date,
                  today: date,
                  result: list,
                  products: list) -> None:
    mocked_date.today.return_value = today
    assert outdated_products(products) == result
