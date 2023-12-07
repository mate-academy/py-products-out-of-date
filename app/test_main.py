import datetime
from unittest import mock
from datetime import date
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "date,data_products,expected_result", ([

        (date(2023, 11, 7), [

            {
                "name": "salmon",
                "expiration_date": datetime.date(2023, 11, 6),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2023, 11, 6),
                "price": 120},
            {
                "name": "duck",
                "expiration_date": datetime.date(2023, 11, 6),
                "price": 160
            }
        ], ["salmon", "chicken", "duck"]),

    ]))
def test_outdated_yesterday_outdated(date: date,
                                     data_products: list[dict],
                                     expected_result: list) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date
        result = outdated_products(data_products)
        assert result == expected_result


@pytest.mark.parametrize(
    "date,data_products,expected_result", ([

        (date(2023, 11, 7), [

            {
                "name": "salmon",
                "expiration_date": datetime.date(2023, 11, 7),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2023, 11, 7),
                "price": 120},
            {
                "name": "duck",
                "expiration_date": datetime.date(2023, 11, 7),
                "price": 160
            }
        ], []),

    ]))
def test_outdated_products_all_outdated(date: date,
                                        data_products: list[dict],
                                        expected_result: list) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date
        result = outdated_products(data_products)
        assert result == expected_result
