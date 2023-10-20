import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def test_products() -> list:
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
    "current_date, expected",
    [
        (
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            datetime.date(2022, 4, 17),
            ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2021, 2, 2),
            []
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_date: mock,
                           current_date: datetime,
                           test_products: list,
                           expected: list) -> None:
    mock_date.date.today.return_value = current_date
    assert outdated_products(test_products) == expected
