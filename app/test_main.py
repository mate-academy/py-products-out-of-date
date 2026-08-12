import pytest

import datetime

from app.main import outdated_products

from unittest import mock

from typing import Any


@pytest.fixture()
def template() -> list[dict]:
    return [
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


def test_for_outdated_products(template: Any) -> None:
    with (mock.patch("app.main.datetime") as mock_datetime):
        # Mock the datetime.date.today() method
        mock_datetime.date.today.return_value = datetime.date(
            2022, 2, 2
        )

        result = outdated_products(template)
        assert result == ["duck"]
