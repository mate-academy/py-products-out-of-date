import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: patch) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products_1 = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1), "price": 160},
    ]
    assert outdated_products(products_1) == ["duck"]
    products_2 = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 1), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 1), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1), "price": 160},
    ]
    assert outdated_products(products_2) == ["salmon", "chicken", "duck"]
    products_3 = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 5), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 10), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 15), "price": 160},
    ]
    assert outdated_products(products_3) == []
    products_4 = []
    assert outdated_products(products_4) == []
    products_5 = [{"name": "salmon",
                   "expiration_date": datetime.date(2022, 2, 2), "price": 600}]
    assert outdated_products(products_5) == []
    products_6 = [{"name": "salmon",
                   "expiration_date": datetime.date(2022, 2, 10),
                   "price": 600}]
    assert outdated_products(products_6) == []
    products_7 = [{"name": "salmon",
                   "expiration_date": datetime.date(2022, 1, 30),
                   "price": 600}]
    assert outdated_products(products_7) == ["salmon"]
