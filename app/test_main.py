import datetime
from typing import Any

from app.main import outdated_products


def test_outdated_products_with_yesterday_expiration(mocker: Any) -> None:
    mocked_today = datetime.date(2023, 10, 27)
    yesterday = mocked_today - datetime.timedelta(days=1)
    mocker.patch("app.main.datetime.date.today", return_value=mocked_today)

    products = [
        {"name": "bread", "expiration_date": yesterday},
    ]

    assert outdated_products(products) == ["bread"], \
        "Product that expired yesterday should be considered outdated"


def test_outdated_products_with_none_expired(mocker: Any) -> None:
    mocked_today = datetime.date(2023, 10, 27)
    mocker.patch("app.main.datetime.date.today", return_value=mocked_today)

    products = [
        {"name": "milk", "expiration_date": datetime.date(2023, 10, 27)},
        {"name": "cheese", "expiration_date": datetime.date(2023, 10, 28)},
    ]

    assert outdated_products(products) == []


def test_outdated_products_with_all_expired(mocker: Any) -> None:
    mocked_today = datetime.date(2023, 10, 27)
    mocker.patch("app.main.datetime.date.today", return_value=mocked_today)

    products = [
        {"name": "bread", "expiration_date": datetime.date(2023, 10, 25)},
        {"name": "yogurt", "expiration_date": datetime.date(2023, 10, 26)},
    ]

    assert outdated_products(products) == ["bread", "yogurt"]


def test_outdated_products_with_empty_list() -> None:
    assert outdated_products([]) == []


def test_outdated_products_with_one_expiring_today(mocker: Any) -> None:
    mocked_today = datetime.date(2023, 10, 27)
    mocker.patch("app.main.datetime.date.today", return_value=mocked_today)

    products = [{"name": "milk", "expiration_date": mocked_today}]

    assert outdated_products(products) == [], \
        "Product expiring today should not be considered outdated"


def test_outdated_products_from_readme_example(mocker: Any) -> None:
    mocked_today = datetime.date(2022, 2, 2)
    mocker.patch("app.main.datetime.date.today", return_value=mocked_today)
    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10)},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5)},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1)},
    ]
    assert outdated_products(products) == ["duck"]
