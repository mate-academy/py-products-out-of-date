import datetime

from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_date_equals_today(mock_date):
    mock_date.date.today.return_value = datetime.date.today()
    product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 7, 22),
            "price": 600
        }]
    assert outdated_products(product) == []


@mock.patch("app.main.datetime")
def test_date_equals_yesterday(mock_date):  #
    mock_date.date.today.return_value = datetime.date(2022, 7, 6)
    product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 7, 10),
            "price": 600
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 7, 5),
            "price": 160

        }]
    assert outdated_products(product) == ["duck"]
