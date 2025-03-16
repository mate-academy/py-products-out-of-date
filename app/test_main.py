import datetime
import pytest
from freezegun import freeze_time
from app.main import outdated_products


@pytest.mark.parametrize(
    "product_list, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120},
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),
    ]
)
def test_outdated_products(
        product_list: list,
        today_date: datetime,
        expected: list
) -> None:
    freezer = freeze_time("2022-02-02")
    freezer.start()
    assert outdated_products(product_list) == expected
    freezer.start()
