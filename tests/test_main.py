from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products_template():
    yield [{"name": "salmon",
            "expiration_date": 5,
            "price": 600},
           {"name": "chicken",
            "expiration_date": 10,
            "price": 120}]


@mock.patch("datetime.date")
def test_should_return_empty_list_if_expiration_date_is_higher(
        mock_date, products_template
):
    mock_date.today.return_value = 1
    assert outdated_products(products_template) == []


@mock.patch("datetime.date")
def test_should_ignore_item_if_expiration_date_equal_today_date(
        mock_date, products_template
):
    mock_date.today.return_value = 10
    assert outdated_products(products_template) == ["salmon"]


@mock.patch("datetime.date")
def test_should_return_all_items_if_expiration_date_is_lower(
        mock_date, products_template
):
    mock_date.today.return_value = 15
    assert outdated_products(products_template) == ["salmon", "chicken"]
