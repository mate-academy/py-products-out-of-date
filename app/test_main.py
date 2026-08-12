import datetime
from unittest import mock

import pytest

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
    "different_date, expected_result",
    [
        ((2022, 1, 1), []),
        ((2022, 2, 2), ["duck"]),
        ((2022, 2, 6), ["duck", "chicken"]),
        ((2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products_with_different_date(
        different_date: tuple[int, int, int],
        expected_result: str,
        products: list) -> None:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date(different_date[0],
                                                          different_date[1],
                                                          different_date[2])
        assert sorted(outdated_products(products)) == sorted(expected_result)
