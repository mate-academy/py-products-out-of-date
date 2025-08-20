from typing import Generator
from unittest import mock

import datetime
import pytest

from app.main import outdated_products


@pytest.fixture()
def products_fixture() -> list:
    products = [
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
    return products


@pytest.fixture()
def mocking_datetime(
    request: pytest.FixtureRequest.instance,
) -> Generator[mock.MagicMock, None, None]:
    datetime_value = request.param
    with mock.patch("app.main.datetime.date") as mock_today:
        mock_today.today.return_value = datetime_value
        yield mock_today


@pytest.mark.parametrize(
    "mocking_datetime, expected",
    [
        pytest.param(
            datetime.date(2021, 12, 19),
            [],
        ),
        pytest.param(
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
        ),
        pytest.param(
            datetime.date(2022, 2, 5),
            ["duck"],
        ),
    ],
    indirect=["mocking_datetime"],
)
def test_outdated_products(
    products_fixture: list[dict],
    mocking_datetime: mock.MagicMock,
    expected: list[str],
) -> None:
    assert outdated_products(products_fixture) == expected
