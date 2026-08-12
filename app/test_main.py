import datetime
import pytest
from .main import outdated_products


@pytest.mark.parametrize(
    "product_date",
    [
        (datetime.date.today() - datetime.timedelta(days=1)),
        (datetime.date(2022, 7, 5)),
    ]
)
def test_outdated_products_with_correct_date(product_date: datetime) -> None:
    products = [{
        "name": "salmon",
        "expiration_date": product_date,
        "price": 600
    }]

    result = outdated_products(products)
    assert result == ["salmon"]


@pytest.mark.parametrize(
    "product_date",
    [
        (datetime.date.today()),
        (datetime.date(2028, 7, 5)),
    ]
)
def test_outdated_products_with_incorrect_date(product_date: datetime) -> None:
    products = [{
        "name": "salmon",
        "expiration_date": product_date,
        "price": 600
    }]

    result = outdated_products(products)
    assert result != ["salmon"]
