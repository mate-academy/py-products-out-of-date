import datetime
from unittest.mock import MagicMock, patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_only_one_product_have_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [{"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160}
                ]
    result = outdated_products(products)
    assert result


@patch("app.main.datetime")
def test_all_products_have_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [{"name": "salmon",
                 "expiration_date": datetime.date(2021, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 1, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160}
                ]
    result = outdated_products(products)
    assert result == ["salmon", "chicken", "duck"]


@patch("app.main.datetime")
def test_no_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [{"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2023, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 3, 1),
                 "price": 160}
                ]
    result = outdated_products(products)
    assert result == []
