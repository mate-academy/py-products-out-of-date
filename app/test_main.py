import datetime
from unittest import mock
from pytest import fixture, mark

from app.main import outdated_products


@fixture
def list_of_products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@mark.parametrize(
    "current_date, result", [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2021, 2, 2), []),
        (datetime.date(2023, 2, 2), ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products(
        list_of_products: list[dict],
        current_date: datetime.date,
        result: list[str]
) -> None:
    with (mock.patch("app.main.datetime")) as mock_datetime:
        mock_datetime.date.today.return_value = current_date
        assert outdated_products(list_of_products) == result
