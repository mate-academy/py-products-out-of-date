import datetime
import pytest
from unittest import mock


from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today,expected_result",
    [
        ([
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
            },
            {
                "name": "torchyn",
                "expiration_date": datetime.date(2022, 2, 11),
                "price": 20
            },
        ], datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
    mocked_datetime_date: mock.Mock,
    products: list[dict],
    today: datetime,
    expected_result: list[str]
) -> None:
    mocked_datetime_date.today.return_value = today
    assert outdated_products(products) == expected_result
