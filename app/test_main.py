import datetime
from unittest.mock import patch
import pytest

from app.main import outdated_products

products = [
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
    "current_date,products_list,result",
    [
        (datetime.date(2022, 2, 1), products, []),
        (datetime.date(2022, 2, 3), products, ["duck"]),
        (datetime.date(2022, 2, 6), products, ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), products, ["salmon", "chicken", "duck"]),
    ],
    ids=[
        "All products are fresh",
        "Outdated only duck",
        "Outdated duck and chicken",
        "Outdated duck, chicken, salmon",
    ]
)
def test_outdated_products(
        current_date: datetime.date,
        products_list: list,
        result: str
) -> None:
    with patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = current_date
        assert outdated_products(products_list) == result
