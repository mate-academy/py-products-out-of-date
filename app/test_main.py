import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products_basic_scenario(
    mock_datetime: mock.MagicMock
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
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
    assert outdated_products(products) == ["duck"]


@mock.patch("app.main.datetime")
def test_outdated_products_boundary_condition(
    mock_datetime: mock.MagicMock
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 50
        }
    ]
    assert outdated_products(products) == []


@mock.patch("app.main.datetime")
def test_outdated_products_all_expired(
    mock_datetime: mock.MagicMock
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2023, 1, 1)
    products = [
        {"name": "bread", "expiration_date": datetime.date(2022, 12, 31)},
        {"name": "butter", "expiration_date": datetime.date(2022, 12, 30)}
    ]
    assert outdated_products(products) == ["bread", "butter"]


@mock.patch("app.main.datetime")
def test_outdated_products_empty_list(
    mock_datetime: mock.MagicMock
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products([]) == []
