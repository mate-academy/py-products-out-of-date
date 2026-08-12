from unittest import mock
import datetime
from app.main import outdated_products

products = ([
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
])


@mock.patch("app.main.datetime")
def test_all_products_outdated(mocked_datetime_date: mock.MagicMock) -> None:

    mocked_datetime_date.date.today.return_value = datetime.date(2022, 2, 5)

    assert outdated_products(products) == ["duck"]
