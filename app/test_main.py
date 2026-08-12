import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_date: mock.Mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    test_data = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
        }
    ]
    assert outdated_products(test_data) == ["duck"]
