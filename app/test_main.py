import pytest
import datetime
from typing import List
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize("products, today_date, expected_products",
                         [([{"name": "salmon",
                             "expiration_date": datetime.date(2022, 2, 10),
                             "price": 600},
                            {"name": "chicken",
                             "expiration_date": datetime.date(2022, 2, 5),
                             "price": 120},
                            {"name": "duck",
                             "expiration_date": datetime.date(2022, 2, 1),
                             "price": 160},
                            {"name": "pork",
                             "expiration_date": datetime.date(2022, 2, 8),
                             "price": 140}],
                           datetime.date(2022, 2, 8),
                           ["chicken", "duck"])])
@mock.patch("datetime.date")
def test_outdated_products(mocked_date: mock.MagicMock,
                           products: List[dict],
                           today_date: datetime,
                           expected_products: list) -> None:
    mocked_date.today.return_value = today_date
    assert outdated_products(products) == expected_products
