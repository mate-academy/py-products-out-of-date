import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 8, 20),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 8, 15),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 8, 8),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "test_date,expected_result",
    [
        (datetime.date(2023, 8, 8), []),
        (datetime.date(2023, 8, 9), ["duck"]),
        (datetime.date(2023, 8, 16), ["chicken", "duck"]),
        (datetime.date(2023, 8, 21), ["salmon", "chicken", "duck"]),
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mock_datetime: mock,
        products: list,
        test_date: type[datetime],
        expected_result: list
) -> None:
    mock_datetime.today.return_value = test_date
    assert outdated_products(products) == expected_result
