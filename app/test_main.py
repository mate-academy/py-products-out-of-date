from unittest import mock
import datetime

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_should_return_empty_list(mock_datetime: mock.MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 3, 10),
            "price": 600
        }, ]
    assert outdated_products(product) == []
