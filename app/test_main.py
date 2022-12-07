import datetime
import pytest
from app.main import outdated_products


@pytest.fixture()
def product_template() -> list:
    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 12, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 12, 6),
            "price": 160
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 12, 7),
            "price": 160
        },
    ]
    return product_list


def test_first_name_is_none(product_template: product_template) -> None:
    assert outdated_products(product_template) == ["chicken", "duck"]
