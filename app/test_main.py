import datetime
from app.main import outdated_products
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "products,mock_today_date,result",
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
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160
                }
            ],
            datetime.date(2022, 2, 2),
            []
        )
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products_frozen_date(
        mock_date: datetime.date,
        products: list[dict],
        mock_today_date: datetime.date,
        result: list[str]
) -> None:
    mock_date.today.return_value = mock_today_date
    assert (
        outdated_products(products) == result
    ), "Result is not as expected"
