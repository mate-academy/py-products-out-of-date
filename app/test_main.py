import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_should_return_correct_list(
        mock_datetime: mock.MagicMock
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    prod_list = [
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
        }
    ]
    assert outdated_products(prod_list) == ["duck"]
