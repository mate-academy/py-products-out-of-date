import datetime
from datetime import date

from unittest import mock

import pytest

from app.main import outdated_products


class NewDate(datetime.date):
    @classmethod
    def today(cls) -> date:
        return cls(2022, 2, 2)


datetime.date = NewDate


@pytest.fixture()
def products() -> list[dict[str, str | date | int]]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_should_return_only_outdated_product(products: list) -> None:
    with (
        mock.patch("app.main.datetime.date.today") as mocked_func
    ):

        mocked_func.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == ["duck"]
