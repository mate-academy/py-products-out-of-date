from unittest import mock
import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today_date, result",
    [
        ([
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
            },
            {
                "name": "nuts",
                "expiration_date": datetime.date(2022, 2, 6),
                "price": 160
            }
        ], datetime.date(2022, 2, 6), ["chicken", "duck"])
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        date_today_mocked: mock.Mock,
        products: list,
        today_date: datetime,
        result: list
) -> None:
    date_today_mocked.today.return_value = today_date
    assert outdated_products(products) == result
