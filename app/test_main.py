from unittest import mock

import pytest

from datetime import date

from app.main import outdated_products


@pytest.fixture()
def mocked_datetime() -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        yield mocked_date


def test_products_out_of_date(mocked_datetime: mocked_datetime) -> None:
    mocked_datetime.date.today.return_value = date(2022, 2, 2)
    res = outdated_products(
        [
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
        ]
    )

    assert res == ["duck"]
