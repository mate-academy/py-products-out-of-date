import pytest
import datetime
from unittest import mock

from app.main import outdated_products


products_template = [
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
    "date_today,expected_value",
    [
        (
            datetime.date(2022, 1, 25),
            []
        ),
        (
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 6),
            ["chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_product(
        mocked_today: mock.MagicMock,
        date_today: datetime,
        expected_value: list
) -> None:
    mocked_today.date.today.return_value = date_today
    assert outdated_products(products_template) == expected_value
