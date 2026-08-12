import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_one_expired_product(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 1, 1)
    mock_datetime.date.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 1, 1),
            "price": 50},
        {
            "name": "bread",
            "expiration_date": datetime.date(2025, 1, 1),
            "price": 20
        }
    ]
    result = outdated_products(products)
    assert result == ["milk"]


@patch("app.main.datetime")
def test_empty_product_list(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 1, 1)
    mock_datetime.date.side_effect =\
        lambda *args, **kwargs: datetime.date(*args, **kwargs)

    products = []
    result = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_all_expired_product_list(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 1, 1)
    mock_datetime.date.side_effect =\
        lambda *args, **kwargs: datetime.date(*args, **kwargs)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 1, 1),
            "price": 50
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2023, 1, 1),
            "price": 20
        }
    ]

    result = outdated_products(products)
    assert result == ["milk", "bread"]


@patch("app.main.datetime")
def test_all_good_product_list(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 1, 1)
    mock_datetime.date.side_effect =\
        lambda *args, **kwargs: datetime.date(*args, **kwargs)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2025, 1, 1),
            "price": 50
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2025, 1, 1),
            "price": 20
        }
    ]

    result = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_equal_today_product_list(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 1, 1)
    mock_datetime.date.side_effect =\
        lambda *args, **kwargs: datetime.date(*args, **kwargs)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2024, 1, 1),
            "price": 50
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2025, 1, 1),
            "price": 20
        }
    ]

    result = outdated_products(products)
    assert result == []
