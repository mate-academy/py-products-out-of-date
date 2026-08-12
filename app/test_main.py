import pytest
import datetime
from app.main import outdated_products
from unittest import mock


@pytest.mark.parametrize("products, expected_result", [
    ([{
        "name": "salmon",
        "expiration_date": datetime.date(2021, 2, 10),
        "price": 600
    }], ["salmon"]),
    ([{
        "name": "chicken",
        "expiration_date": datetime.date(2023, 1, 1),
        "price": 120
    }], []),
    ([{
        "name": "duck",
        "expiration_date": datetime.date(2022, 3, 2),
        "price": 160
    }], []),
    ([{
        "name": "apple",
        "expiration_date": datetime.date(2022, 1, 2),
        "price": 160
    }], ["apple"]),
    ([{
        "name": "potato",
        "expiration_date": datetime.date(2022, 3, 2),
        "price": 160
    }], []),
    ([{
        "name": "strawberry",
        "expiration_date": datetime.date(2022, 2, 2),
        "price": 160
    }], []),
    ([{
        "name": "pineapple",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }], ["pineapple"]),
    ([{
        "name": "plum",
        "expiration_date": datetime.date(2022, 2, 3),
        "price": 160
    }], [])
])
def test_outdated_products(
        products: list,
        expected_result: list | None
) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == expected_result
