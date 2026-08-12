import pytest

from unittest import mock
from .main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": (2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": (2022, 2, 2),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": (2022, 2, 1),
        "price": 160
    }
]

result = ["duck"]


@pytest.mark.parametrize(
    "products,fake_date,result",
    [
        (products, (2022, 2, 2), result)
    ]
)
@mock.patch("app.main.datetime.date")
def test_product(
        mocked_time: mock.MagicMock,
        fake_date: tuple,
        products: list,
        result: list
) -> None:
    mocked_time.today.return_value = fake_date
    assert outdated_products(products) == result
