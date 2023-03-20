import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {"name": "sal", "expire_date": datetime.date(2022, 2, 10), "price": 6},
        {"name": "chic", "expire_date": datetime.date(2022, 2, 5), "price": 2},
        {"name": "duck", "expire_date": datetime.date(2022, 2, 1), "price": 1}]


@mock.patch("app.main.datetime")
def test_outdated_products(
    mock_date: None,
    products: list
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
