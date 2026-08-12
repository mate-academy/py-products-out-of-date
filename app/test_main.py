import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
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
    "date, result",
    [
        pytest.param(datetime.date(2022, 1, 15), []),
        pytest.param(datetime.date(2022, 2, 1), []),
        pytest.param(datetime.date(2022, 2, 5), ["duck"]),
        pytest.param(datetime.date(2022, 2, 10), ["chicken", "duck"]),
        pytest.param(datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products(
        date: datetime,
        result: list,
        products: list
) -> None:
    with (mock.patch("app.main.datetime")) as mocked_date:
        mocked_date.date.today.return_value = date
        assert outdated_products(products) == result
