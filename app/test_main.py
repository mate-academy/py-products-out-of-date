import pytest
import datetime

from unittest import mock

from app.main import outdated_products


@pytest.fixture
def products() -> list:
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


@pytest.mark.parametrize(
    "best_by,result",
    [
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 12), ["salmon", "chicken", "duck"]),
    ]
)
def test_correct_return_outdated_products(
        products: list,
        best_by: datetime.date,
        result: list
) -> None:
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = best_by
        assert outdated_products(products) == result
