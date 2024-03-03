import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_of_date(mocked_function: mock) -> None:
    # with mock.patch('app.main.datetime') as mock_datetime:
    #     mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    mocked_function.date.today.return_value = datetime.date(2022, 2, 2)
    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 3),
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
    assert outdated_products(product_list) == ["duck"]
