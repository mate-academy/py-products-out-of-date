from app.main import outdated_products
import pytest
from unittest import mock
import datetime


@pytest.fixture(scope="function")
def get_products() -> list[dict]:
    products = [
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
    yield products
    del products


@pytest.mark.parametrize(
    "day, expected_result",
    [
        pytest.param(10, ["chicken", "duck"],
                     id="expiration day yesterday outdated"),
        pytest.param(2, ["duck"],
                     id="expiration day today not outdated"),
    ]
)
def test_outdated_products_logic(
        get_products: list[dict],
        day: int,
        expected_result: list
) -> None:

    datetime_mock = mock.Mock(wraps=datetime.date)
    datetime_mock.today.return_value = datetime.date(2022, 2, day)
    with mock.patch("datetime.date", new=datetime_mock):
        assert outdated_products(get_products) == expected_result
