import datetime

import pytest
from _pytest.monkeypatch import MonkeyPatch
from _pytest.fixtures import FixtureRequest

from app.main import outdated_products


@pytest.fixture(params=[
    (
        (2024, 2, 2),
        [(2022, 2, 10), (2022, 2, 5), (2022, 2, 1)],
        ["salmon", "chicken", "duck"]
    ),
    (
        (2022, 2, 2),
        [(2022, 2, 10), (2022, 2, 5), (2022, 2, 1)],
        ["duck"]
    ),
    (
        (2025, 10, 2),
        [(2025, 11, 10), (2025, 2, 5), (2025, 12, 1)],
        ["chicken"]
    ),
    (
        (2012, 2, 28),
        [(2012, 2, 1), (2022, 3, 5), (2022, 3, 1)],
        ["salmon"]
    ),
    (
        (1997, 6, 20),
        [(1997, 7, 10), (1997, 6, 20), (1997, 6, 21)],
        []
    ),
    (
        (4022, 12, 31),
        [(4023, 1, 1), (4023, 2, 5), (8322, 12, 31)],
        []
    )
])
def products_template(
        request: FixtureRequest,
        monkeypatch: MonkeyPatch
) -> tuple:
    today_tuple = request.param[0]
    date_list = request.param[1]

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(*today_tuple)

    monkeypatch.setattr(datetime, "date", MockDate)

    products_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(*date_list[0]),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(*date_list[1]),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(*date_list[2]),
        }
    ]

    return products_list, request.param[2]


def test_outdated_products(products_template: tuple) -> None:
    products, expected_expired = products_template
    actual_expired = outdated_products(products)
    assert sorted(actual_expired) == sorted(expected_expired)
