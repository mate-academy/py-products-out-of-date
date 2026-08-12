import pytest
from datetime import date
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        (
            [{
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            }],
            ["salmon"]
        ),
        (
            [{
                "name": "salmon",
                "expiration_date": date(2024, 2, 10),
                "price": 600
            }],
            []
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_datetime: mock.MagicMock,
        products: list,
        expected: list
) -> None:

    mocked_datetime.date.today.return_value = date(2023, 2, 10)
    assert outdated_products(products) == expected
