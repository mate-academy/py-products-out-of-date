import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "product_list, today_date, expected",
    [
        (
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160},
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),
        (
            [
                {"name": "beef",
                 "expiration_date": datetime.date(2023, 5, 19),
                 "price": 300},
                {"name": "pork",
                 "expiration_date": datetime.date(2023, 5,
                                                  18), "price": 250},
            ],
            datetime.date(2023, 5, 19),
            ["pork"],
        ),
        (
            [
                {"name": "fish",
                 "expiration_date": datetime.date(2024, 1, 1),
                 "price": 500}
            ],
            datetime.date(2023, 12, 31),
            [],
        ),
    ],
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date: datetime,
                           product_list: list,
                           today_date: datetime,
                           expected: list) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(product_list) == expected
