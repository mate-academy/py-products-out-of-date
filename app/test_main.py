import datetime
from unittest import mock
from unittest.mock import patch

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "mock_today,actual_product,expected_product",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160},
            ],
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 11),
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160},
            ],
            ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 1),
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160},
            ],
            []
        )
    ]
)
def test_outdated_products(mock_today: mock.MagicMock,
                           actual_product: list,
                           expected_product: list) -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = mock_today
        mock_date.side_effect = lambda * args, **kwargs: datetime.date(
            *args, **kwargs)
        assert outdated_products(actual_product) == expected_product
