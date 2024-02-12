import pytest
from unittest import mock
from datetime import date

from app.main import outdated_products


@pytest.mark.parametrize(
    "product, result",
    [
        (
            [
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
            ],
            ["duck"])
    ]
)
@mock.patch("app.main.datetime")
def test_products(
        mock_datetime: mock.MagicMock,
        product: list,
        result: list,
) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 2)
    assert outdated_products(product) == result
