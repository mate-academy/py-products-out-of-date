import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 11, 7),
                }
            ],
            []
        ),
        (
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 4, 5),
                    "price": 120
                },
            ],
            ["chicken"]
        ),
        (
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 5, 5),
                    "price": 160
                }
            ],
            []
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_date: mock.MagicMock,
        products: list,
        result: list
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 5, 5)
    assert outdated_products(products) == result
