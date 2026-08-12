import pytest
import datetime

from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products_list_with_wrong_expiration_date() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": None,
            "price": 600
        },
        {
            "name": "chicken",
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.fixture()
def products_list() -> list[dict]:
    return [
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


def test_raise_error_expiration_date_incorrect(
        products_list_with_wrong_expiration_date: list[dict]
) -> None:
    with pytest.raises(TypeError):
        outdated_products(products_list_with_wrong_expiration_date)


def test_raise_error_expiration_date_no_exist(
        products_list_with_wrong_expiration_date: list[dict]
) -> None:
    with pytest.raises(TypeError):
        outdated_products(products_list_with_wrong_expiration_date)


@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_today: mock.Mock,
        products_list: list[dict]
) -> None:
    mock_today.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_list) == ["duck"]
