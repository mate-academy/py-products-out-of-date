from app.main import outdated_products
from unittest import mock
import datetime
@mock.patch("datetime.date.today")
@mock.patch("datetime.date")
def test_expiration_date(mock_date,mock_date_exp):
    mock_date.return_value = 2022-11-24
    mock_date_exp.return_value = 2022-11-24
    product = [{
        "name": "chicken",
        "expiration_date": datetime.date(2023, 2, 5),
        "price": 120
    }]
    outdated_products(product)
    assert outdated_products(product) == []


@mock.patch("datetime.date.today")
@mock.patch("datetime.date")
def test_expiration_date2(mock_date,mock_date_exp):
    mock_date.return_value = 2022-11-25
    mock_date_exp.return_value = 2022-11-24
    product = [{
        "name": "chicken",
        "expiration_date": datetime.date(2023, 2, 5),
        "price": 120
    }]
    outdated_products(product)
    assert outdated_products(product) == ["chicken"]