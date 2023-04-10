import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def mock_today() -> None:
    with mock.patch("datetime.datetime") as mocked_function:
        yield mocked_function


@pytest.mark.parametrize(
    "products,result",
    [
        (
            [
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
            ],
            ["duck"]
        ),
    ]
)
def test_outdated_products(mock_today: mock.Mock,
                           products: list[dict],
                           result: list[str]) -> None:
    mock_today.return_value = datetime.date(2022, 2, 5)
    assert outdated_products(products) == result
