import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "dict_in, result, date",
    [
        ([
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
             }], ["duck"], datetime.date(2022, 2, 2)),
        ([
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
             }], [], datetime.date(2022, 1, 29)),
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_date, dict_in, result, date):
    mock_date.date.today.return_value = date
    assert outdated_products(dict_in) == result
