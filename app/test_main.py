import datetime

from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mock_date: mock.MagicMock) -> None:
    mock_date.date.today.return_value = datetime.date(2023, 9, 13)

    # All products are expired
    list1 = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 11),
            "price": 120
        }
    ]
    products1 = outdated_products(list1)
    assert products1 == ["salmon", "chicken"]

    # Some products are expired
    list2 = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 15),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 11),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2023, 9, 20),
            "price": 200
        }
    ]
    products2 = outdated_products(list2)
    assert products2 == ["chicken"]

    # No products are expired
    list3 = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 15),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 20),
            "price": 120
        }
    ]
    products3 = outdated_products(list3)
    assert products3 == []

    # Product expires today, not outdated
    list4 = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 13),
            "price": 600
        }
    ]
    products4 = outdated_products(list4)
    assert products4 == []
