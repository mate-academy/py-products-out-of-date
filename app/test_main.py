from datetime import date
from unittest import mock

from app.main import outdated_products


def test_function_datetime_when_all_products_are_fresh() -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date(2022, 2, 1)
        result = outdated_products([
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ])

        assert result == []


def test_function_datetime_all_products_are_outdated() -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date(2022, 2, 11)
        result = outdated_products([
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ])

        assert result == ["salmon", "chicken", "duck"]
