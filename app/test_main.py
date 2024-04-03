import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expected_expired",
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
        )
    ],
    ids=["year-2022,month-2,day-2, expected_expired ['duck']"]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime, products, expected_expired):
    fake_today_date = datetime.date(2022, 2, 2)
    mock_datetime.date.today.return_value = fake_today_date

    real_expired = outdated_products(products)

    assert real_expired == expected_expired
