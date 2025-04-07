import datetime
from unittest import mock
from app.main import outdated_products

REAL_DATE = datetime.date


@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date: mock.Mock) -> None:
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = lambda *args, **kwargs: REAL_DATE(*args, **kwargs)

    products = [
        {
            "name": "salmon",
            "expiration_date": REAL_DATE(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": REAL_DATE(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": REAL_DATE(2022, 2, 1),
            "price": 160
        }
    ]
    expected = ["duck"]
    assert outdated_products(products) == expected


@mock.patch("app.main.datetime.date")
def test_expiration_day_today_not_outdated(mock_date: mock.Mock) -> None:
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = lambda *args, **kwargs: REAL_DATE(*args, **kwargs)
    products = [
        {
            "name": "juice",
            "expiration_date": REAL_DATE(2022, 2, 2),
            "price": 10
        }
    ]

    expected = []
    assert outdated_products(products) == expected
