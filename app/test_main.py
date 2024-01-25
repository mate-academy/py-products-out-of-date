import datetime
import pytest
from unittest import mock


from app.main import outdated_products


@pytest.mark.parametrize("date_now, product, result",
                         [
                             (
                                 datetime.date(2024, 1, 25),
                                 [
                                     {
                                         "name": "salmon",
                                         "expiration_date":
                                             datetime.date(2024, 1, 25),
                                         "price": 600
                                     }
                                 ],
                                 []
                             ),
                             (
                                 datetime.date(2025, 1, 25),
                                 [
                                     {
                                         "name": "salmon",
                                         "expiration_date":
                                             datetime.date(2024, 1, 24),
                                         "price": 600
                                     }
                                 ],
                                 ["salmon"]
                             ),

                             (
                                 datetime.date(2023, 11, 12),
                                 [
                                     {
                                         "name": "chicken",
                                         "expiration_date":
                                         datetime.date(2024, 1, 25),
                                         "price": 120
                                     },
                                     {
                                         "name": "duck",
                                         "expiration_date":
                                         datetime.date(2023, 11, 13),
                                         "price": 160
                                     },
                                     {
                                         "name": "apple",
                                         "expiration_date":
                                         datetime.date(2023, 11, 11),
                                         "price": 160
                                     },
                                     {
                                         "name": "salmon",
                                         "expiration_date":
                                         datetime.date(2023, 1, 1),
                                         "price": 600
                                     }
                                 ],
                                 ["apple", "salmon"]
                             ),
                         ]
                         )
@mock.patch("datetime.date")
def test_outdated_products(
        date_today_mocked: mock.Mock,
        date_now: datetime,
        product: list,
        result: list | None
) -> None:
    date_today_mocked.today.return_value = date_now
    assert outdated_products(product) == result
