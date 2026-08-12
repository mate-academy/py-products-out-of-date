import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture
def prepare_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]
    return products


@pytest.fixture()
def mock_datatime() -> None:
    with mock.patch("app.main.datetime") as mock_date:
        yield mock_date


def test_outdated_product(prepare_products: callable,
                          mock_datatime: mock.MagicMock) -> None:
    mock_datatime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(prepare_products) == ["duck"]
