import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]


@pytest.mark.parametrize(
    "today,expected",
    [
        (datetime.date(2022, 1, 1), []),
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 3, 1), ["salmon", "chicken", "duck"]),
    ],
    ids=[
        "should return empty list when all products are fresh",
        "should not return product when today is expiration date",
        "should return product when expiration date has passed",
        "should return several outdated products",
        "should return all products when all are outdated",
    ],
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mock_datetime: mock.MagicMock,
    today: datetime.date,
    expected: list[str],
    products: list[dict],
) -> None:
    mock_datetime.date.today.return_value = today
    assert outdated_products(products) == expected, (
        f"Should return {expected} when today is {today}"
    )


@mock.patch("app.main.datetime")
def test_should_return_empty_list_when_no_products(
    mock_datetime: mock.MagicMock,
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products([]) == [], (
        "Should return empty list when there are no products"
    )


@mock.patch("app.main.datetime")
def test_today_should_be_called(
    mock_datetime: mock.MagicMock,
    products: list[dict],
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    outdated_products(products)
    mock_datetime.date.today.assert_called()
