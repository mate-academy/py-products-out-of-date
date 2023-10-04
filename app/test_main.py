import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products_sample() -> list[dict]:
    yield [
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
    "date,expired_products",
    [
        (
            datetime.date(2021, 10, 10),
            []
        ),
        (
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 5),
            ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_today: callable,
        products_sample: list[dict],
        date: datetime.date,
        expired_products: list
) -> None:
    mocked_today.date.today.return_value = date
    assert outdated_products(products_sample) == expired_products
