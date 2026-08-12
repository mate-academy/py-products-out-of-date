import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_function_return_list(mocked_date: mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 10)
    product = [{"name": "salmon",
                "expiration_date": datetime.date(2023, 2, 10),
                "price": 600
                }]
    assert isinstance(outdated_products(product), list)


@mock.patch("app.main.datetime")
def test_function_return_outdated_product(mocked_date: mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 10, 30)
    product = [{"name": "salmon",
                "expiration_date": datetime.date(2022, 10, 29),
                "price": 600
                }]
    assert outdated_products(product) == ["salmon"]


@mock.patch("app.main.datetime")
def test_function_dont_return_not_outdated_product(mocked_date: mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 10)
    product = [{"name": "salmon",
                "expiration_date": datetime.date(2023, 10, 29),
                "price": 600
                }]
    assert outdated_products(product) == []


@mock.patch("app.main.datetime")
def test_expiration_day_is_today_is_not_outdated(mocked_date: mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 10, 29)
    product = [{"name": "salmon",
                "expiration_date": datetime.date(2022, 10, 29),
                "price": 600
                }]
    assert outdated_products(product) == []
