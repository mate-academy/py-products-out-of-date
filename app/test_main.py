from unittest import mock
from unittest.mock import MagicMock
import datetime
from app.main import outdated_products

real_date = datetime.date


@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date: MagicMock) -> None:
    mock_date.today.return_value = real_date(2022, 2, 2)
    mock_date.side_effect = lambda *args, **kwargs: real_date(*args, **kwargs)
    list_products = [{
        "name": "salmon",
        "expiration_date": real_date(2022, 2, 10),
        "price": 600},
        {
        "name": "chicken",
        "expiration_date": real_date(2022, 2, 2),
        "price": 120},
        {
        "name": "duck",
        "expiration_date": real_date(2022, 2, 1),
        "price": 160}
    ]

    result = outdated_products(list_products)
    assert result == ["duck"]
