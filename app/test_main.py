import datetime
from unittest.mock import patch

import pytest

from app import main


TODAY = datetime.date(2022, 2, 2)


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return TODAY


@patch("app.main.datetime.date", FakeDate)
@pytest.mark.parametrize(
    "products,expected_names",
    [
        (
            [
                {
                    "name": "rotted_orange",
                    "expiration_date": datetime.date(2014, 1, 2),
                },
                {
                    "name": "old_milk",
                    "expiration_date": datetime.date(2022, 2, 1),
                },
                {
                    "name": "mediocre_rice",
                    "expiration_date": datetime.date(2022, 2, 2),
                },
                {
                    "name": "good_ketchup",
                    "expiration_date": datetime.date(2022, 3, 10),
                },
            ],
            ["rotted_orange", "old_milk"],
        ),
    ],
)
def test_outdated_products(
    products: list[dict],
    expected_names: list[str],
) -> None:
    result = main.outdated_products(products)
    assert result == expected_names
