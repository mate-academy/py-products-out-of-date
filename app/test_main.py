from app.main import outdated_products
import datetime


def test_should_return_one_product() -> None:

    assert outdated_products([{"name": "duck",
                               "expiration_date": datetime.date(2022, 2, 1),
                               "price": 160}]) == ["duck"]


def test_with_date_equals_today() -> None:
    assert outdated_products([{"name": "duck",
                               "expiration_date": datetime.date.today(),
                               "price": 160}]) == []


def test_with_date_equals_yesterday() -> None:
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    assert outdated_products([{"name": "duck",
                               "expiration_date": yesterday,
                               "price": 160}]) == ["duck"]
