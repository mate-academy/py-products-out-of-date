import pytest
import datetime
from unittest import mock
from app.main import outdated_products

today = datetime.date(2023, 2, 16)


@pytest.mark.parametrize(
    "products, result", [
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }], ["salmon"]),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2024, 2, 10),
            "price": 600
        }], []),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 16),
            "price": 600
        }], []),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 15),
            "price": 600
        }], ["salmon"]),

    ])
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_datetime_date_today: mock,
        products: list[dict],
        result: list[str]
) -> None:
    mocked_datetime_date_today.today.return_value = today
    assert outdated_products(products) == result
