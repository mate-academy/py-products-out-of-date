import datetime
from unittest import mock

import pytest

from app.main import outdated_products


real_date = datetime.date


@pytest.mark.parametrize(
    "products, result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: mock.MagicMock,
        products: list[dict],
        result: list[str]
) -> None:

    mock_date.today.return_value = real_date(2022, 2, 2)
    mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)

    assert outdated_products(products) == result
