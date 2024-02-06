from unittest import mock

import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    ("products", "today_date", "names_product"),
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 6),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 1),
                    "price": 160
                }
            ],
            datetime.date.today(),
            ["chicken", "duck"]
        )
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mock_datime_date: mock.MagicMock,
        products: list,
        today_date: datetime,
        names_product: list
) -> None:
    mock_datime_date.today.return_value = today_date
    assert outdated_products(products) == names_product
