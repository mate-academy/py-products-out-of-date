from unittest import mock
import datetime

from .main import outdated_products


def test_result_of_input() -> None:
    assert outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2023, 6, 20),
        "price": 600},
        {
        "name": "chicken",
        "expiration_date": datetime.date(2023, 6, 21),
        "price": 120},
        {
        "name": "duck",
        "expiration_date": datetime.date(2023, 6, 1),
        "price": 160}]
    ) == ["salmon", "duck"]


@mock.patch("app.main.datetime")
def test_datetime_has_calling(mocked_date: datetime) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
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
    assert outdated_products(products) == ["duck"]
