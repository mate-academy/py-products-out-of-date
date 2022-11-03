import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_product(mock_func: mock) -> None:
    mock_func.date.today.return_value = datetime.date(2022, 11, 1)
    assert outdated_products([{"name": "salmon",
                               "expiration_date": datetime.date(2022, 11, 3),
                               "price": 600},
                              {"name": "chicken",
                               "expiration_date": datetime.date(2022, 11, 2),
                               "price": 120},
                              {"name": "duck",
                               "expiration_date": datetime.date(2022, 11, 1),
                               "price": 160}]) == []
