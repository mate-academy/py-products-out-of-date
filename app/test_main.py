import pytest
import datetime
from unittest import mock
from unittest.mock import MagicMock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        (
                [
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
                ],
                ["duck"]
        ),
        (
                [
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
                        "expiration_date": datetime.date(2022, 2, 8),
                        "price": 160
                    }
                ],
                []
        ),
        (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 1),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2022, 1, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 1, 8),
                        "price": 160
                    }
                ],
                ["salmon", "chicken", "duck"]
        ),
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_date: MagicMock,
        products: list[dict],
        expected: list[str]
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products(products) == expected
