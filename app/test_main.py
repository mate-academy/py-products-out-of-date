import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_no_outdated_products(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
    ]
    result = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_one_outdated_product(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]
    result = outdated_products(products)
    assert result == ["duck"]


@patch("app.main.datetime")
def test_multiple_outdated_products(mock_datetime: datetime) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 6)
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]
    result = outdated_products(products)
    assert sorted(result) == sorted(["salmon", "chicken", "duck"])


@patch("app.main.datetime")
def test_product_expiration_today_is_not_outdated(
        mock_datetime: datetime
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 5)
    products = [
        {
            "name": "beef",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 300
        },
    ]
    result = outdated_products(products)
    assert result == []
