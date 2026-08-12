import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


# Тест, коли деякі продукти прострочені
@patch("app.main.datetime")
def test_some_products_outdated(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),  # реальна дата
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),  # реальна дата
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),  # реальна дата
            "price": 160
        }
    ]

    result = outdated_products(products)
    assert result == ["duck"]


# Тест, коли всі продукти прострочені
@patch("app.main.datetime")
def test_all_products_outdated(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 11)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),  # реальна дата
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),  # реальна дата
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),  # реальна дата
            "price": 160
        }
    ]

    result = outdated_products(products)
    assert result == ["salmon", "chicken", "duck"]


# Тест, коли жоден продукт не прострочений
@patch("app.main.datetime")
def test_no_products_outdated(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),  # реальна дата
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),  # реальна дата
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 2),  # реальна дата
            "price": 160
        }
    ]

    result = outdated_products(products)
    assert result == []


# Тест, коли список продуктів порожній
@patch("app.main.datetime")
def test_empty_product_list(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)

    products = []

    result = outdated_products(products)
    assert result == []
