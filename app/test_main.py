import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def mock_time() -> None:
    with mock.patch("app.main.datetime") as mocked_get_current_date:
        yield mocked_get_current_date


@pytest.fixture()
def products_list() -> list[dict]:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 10, 9),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 10, 11),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 10, 10),
            "price": 160
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2023, 8, 9),
            "price": 220
        },
        {
            "name": "eggs",
            "expiration_date": datetime.date(2023, 11, 1),
            "price": 68
        }
    ]
    return products


def test_(products_list: pytest.fixture, mock_time: pytest.fixture) -> None:
    mock_time.date.today.return_value = datetime.date(2023, 10, 10)
    result = outdated_products(products_list)
    assert result == ["salmon", "beef"]
