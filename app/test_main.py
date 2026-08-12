import datetime
from unittest import mock
import pytest
from app.main import outdated_products

product_list = [
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
]


@pytest.mark.parametrize(
    "list_of_products, date, result",
    [
        (product_list, datetime.date(2022, 2, 2), ["duck"])
    ]
)
@mock.patch("app.main.datetime")
def test_for_check_outdated_product(out_of_date: mock,
                                    list_of_products: list[dict],
                                    date: datetime,
                                    result: list[dict]) -> None:
    out_of_date.date.today.return_value = date
    assert (
        outdated_products(product_list) == ["duck"]
    )
