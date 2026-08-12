import datetime

from app.main import outdated_products
from pytest import fixture
from unittest.mock import MagicMock
from typing import List


@fixture
def product() -> List[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date.today(),
            "price": 600
        }
    ]


def test_should_return_empty_list(
        product: MagicMock
) -> None:
    assert outdated_products(product) == []
    product[0]["expiration_date"] = (datetime.date.today()
                                     + datetime.timedelta(days=1))
    assert outdated_products(product) == []


def test_should_return_salmon(
        product: MagicMock
) -> None:
    product[0]["expiration_date"] = (datetime.date.today()
                                     - datetime.timedelta(days=1))
    assert outdated_products(product) == ["salmon"]
