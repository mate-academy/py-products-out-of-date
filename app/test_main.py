import pytest
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expiration_date,result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": (2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": (2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": (2022, 2, 1),
                    "price": 160
                },
                {
                    "name": "beef",
                    "expiration_date": (2022, 2, 2),
                    "price": 600
                },
            ],
            (2022, 2, 2),
            ["duck"]

        )
    ]
)
def test_outdated_products(
        products: list,
        expiration_date: set,
        result: list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = expiration_date
        assert outdated_products(products) == result
