import datetime
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_out(mocked_date: datetime) -> None:

    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)

    print("Inside test", datetime.datetime.today())
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]
    ) == ["duck"]
